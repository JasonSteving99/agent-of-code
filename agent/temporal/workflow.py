import asyncio
from datetime import timedelta

from pydantic import BaseModel
from temporalio import workflow
from temporalio.common import RetryPolicy
from temporalio.exceptions import ApplicationError


# Imports passed through Temporal's sandbox without overriding stdlib.
with workflow.unsafe.imports_passed_through():
    from agent.adventofcode.contextualize_examples import ExamplesContext
    from agent.adventofcode.debug.DebuggingPrompt import DebuggingPrompt
    from agent.adventofcode.extract_examples import AoCProblemExtractedExamples
    from agent.adventofcode.generate_code.generate_implementation import (
        GenerateImplementationOutput,
    )
    from agent.adventofcode.generate_code.generate_unit_tests import (
        GenerateUnitTestsOutput,
    )
    from agent.temporal.activities import (
        AoCProblem,
        CommitChangesArgs,
        DebugUnitTestFailuresArgs,
        ExtractExamplesArgs,
        ExtractedProblemPart,
        GeneratedSolutionRes,
        GetExamplesContextArgs,
        GetGeneratedImplementationArgs,
        GetGeneratedUnitTestsArgs,
        PlanImplRefactoringArgs,
        SubmitSolutionArgs,
        TestResults,
        commit_changes,
        debug_unit_test_failures,
        extract_examples,
        extract_problem_part,
        get_examples_context,
        get_generated_implementation,
        get_generated_unit_tests,
        plan_impl_refactoring,
        run_generated_solution,
        run_generated_tests,
        submit_solution,
    )
    from os.path import join as path_join

# Independent attempts starting from scratch.
_MAX_PROBLEM_PART_ATTEMPTS = 3
# Debugging loop iterations.
_MAX_UNIT_TEST_FIX_ITERATIONS = 6


class SolveAoCProblemWorkflowArgs(BaseModel):
    year: int
    day: int
    solutions_dir: str


class SolveAoCProblemWorkflowResult(BaseModel):
    part_1_solution: GeneratedSolutionRes
    # Only populated if part 1 was solved successfully.
    part_2_solution: GeneratedSolutionRes | None


@workflow.defn
class SolveAoCProblemWorkflow:
    @workflow.run
    async def run(self, args: SolveAoCProblemWorkflowArgs) -> SolveAoCProblemWorkflowResult:
        solve_aoc_part_1_problem_req = AoCProblem(year=args.year, day=args.day, part=1)
        problem_part = await self._scrape_problem_part(solve_aoc_part_1_problem_req)

        # Start by solving part 1.
        part_1_solution = await self._solve_part(
            solve_aoc_part_1_problem_req,
            problem_part,
            solutions_dir=path_join(args.solutions_dir, "part1"),
        )
        if isinstance(part_1_solution.result, GeneratedSolutionRes.Failure):
            # If we weren't even able to solve part 1, we can't move on to part 2.
            return SolveAoCProblemWorkflowResult(
                part_1_solution=part_1_solution, part_2_solution=None
            )

        # Now move on to solving part 2.
        solve_aoc_part_2_problem_req = AoCProblem(year=args.year, day=args.day, part=2)
        problem_part = await self._scrape_problem_part(solve_aoc_part_2_problem_req)
        part_2_solution = await self._solve_part(
            solve_aoc_part_2_problem_req,
            problem_part,
            solutions_dir=path_join(args.solutions_dir, "part2"),
        )

        # Return the solutions we were able to get.
        return SolveAoCProblemWorkflowResult(
            part_1_solution=part_1_solution, part_2_solution=part_2_solution
        )

    async def _scrape_problem_part(self, problem_req: AoCProblem) -> ExtractedProblemPart:
        return await workflow.execute_activity(
            extract_problem_part,
            problem_req,
            start_to_close_timeout=timedelta(seconds=15),
            retry_policy=RetryPolicy(
                maximum_attempts=5,
                # Try being a good citizen and don't spam retries to AoC's servers.
                initial_interval=timedelta(seconds=5),
                maximum_interval=timedelta(seconds=30),
            ),
        )

    async def _solve_part(
        self,
        solve_aoc_problem_req: AoCProblem,
        problem_part: ExtractedProblemPart,
        solutions_dir: str,
    ) -> GeneratedSolutionRes:
        # Some of the prompts get modified to extract solutions to part 2.
        solve_part_2 = solve_aoc_problem_req.part == 2

        extracted_examples = await workflow.execute_activity(
            extract_examples,
            ExtractExamplesArgs(extracted_problem_part=problem_part, solve_part_2=solve_part_2),
            start_to_close_timeout=timedelta(seconds=60),
            retry_policy=RetryPolicy(maximum_attempts=5),
        )

        examples_context = await workflow.execute_activity(
            get_examples_context,
            GetExamplesContextArgs(
                extracted_problem_part=problem_part,
                extracted_examples=extracted_examples,
                solve_part_2=solve_part_2,
            ),
            start_to_close_timeout=timedelta(seconds=60),
            retry_policy=RetryPolicy(maximum_attempts=5),
        )

        for i in range(_MAX_PROBLEM_PART_ATTEMPTS):
            # Since I don't think I should show the unit tests to the LLM when asking it to generate
            # the implementation, I can just go ahead and generate the initial implementation
            # concurrently.
            unit_tests, implementation = await asyncio.gather(
                workflow.execute_activity(
                    get_generated_unit_tests,
                    GetGeneratedUnitTestsArgs(
                        examples=extracted_examples, examples_context=examples_context
                    ),
                    start_to_close_timeout=timedelta(seconds=60),
                    retry_policy=RetryPolicy(maximum_attempts=5),
                ),
                workflow.execute_activity(
                    get_generated_implementation,
                    GetGeneratedImplementationArgs(
                        extracted_problem_part=problem_part,
                        examples_context=examples_context,
                        solve_part_2=solve_part_2,
                    ),
                    start_to_close_timeout=timedelta(seconds=60),
                    retry_policy=RetryPolicy(maximum_attempts=5),
                ),
            )

            # Commit these initial tests and implementation files right away before executing any
            # tests. At this point, we're just ensuring that we can actually track the progress that
            # this agent makes since it'll be really interesting to go back through and evaluate
            # this later on.
            await workflow.execute_activity(
                commit_changes,
                CommitChangesArgs(
                    aoc_problem=solve_aoc_problem_req,
                    solutions_dir=solutions_dir,
                    unit_tests=unit_tests.generated_unit_tests,
                    implementation=implementation.generated_implementation,
                    problem_input=problem_part.problem_input,
                    commit_message="Initial Attempt",
                ),
                start_to_close_timeout=timedelta(seconds=60),
                retry_policy=RetryPolicy(maximum_attempts=5),
            )

            # Now, actually run the generated unit tests to see if we're gonna be able to move
            # forward. We'll iterate on making changes to the tests and the implementation itself
            # until we can get these tests to pass, before we'll move on to executing the full
            # solution on the overall problem input.
            try:
                unit_tests, implementation = await iteratively_make_unit_tests_pass(
                    solve_aoc_problem_req=solve_aoc_problem_req,
                    solutions_dir=solutions_dir,
                    problem_part=problem_part,
                    extracted_examples=extracted_examples,
                    examples_context=examples_context,
                    unit_tests=unit_tests,
                    implementation=implementation,
                )
            except ApplicationError as e:
                if i + 1 < _MAX_PROBLEM_PART_ATTEMPTS:
                    workflow.logger.warning(f"{e.message}...Retrying...")
                    continue
                raise e

            problem_solution_result = await workflow.execute_activity(
                run_generated_solution,
                solve_aoc_problem_req,
                start_to_close_timeout=timedelta(minutes=5),
                # Don't allow any retries for execution of the actual problem solution.
            )

            match problem_solution_result.result:
                case GeneratedSolutionRes.Failure:
                    raise ApplicationError(
                        "Problem solution threw an exception! Need to figure out how to correct it."
                    )
                case GeneratedSolutionRes.Success(output=output):
                    # Check if the solution is actually valid.
                    is_correct_solution = await workflow.execute_activity(
                        submit_solution,
                        SubmitSolutionArgs(
                            aoc_problem=solve_aoc_problem_req,
                            solution=output,
                            base_dir=solutions_dir,
                        ),
                        start_to_close_timeout=timedelta(seconds=15),
                        retry_policy=RetryPolicy(
                            maximum_attempts=5,
                            # Try being a good citizen and don't spam retries to AoC's servers.
                            initial_interval=timedelta(seconds=5),
                            maximum_interval=timedelta(seconds=30),
                        ),
                    )
                    if is_correct_solution:
                        # If the solution is correct, then we're done!
                        break
                    # Otherwise, potentially try again.
                case _:
                    raise ValueError("Unexpected result type!")

        return problem_solution_result


async def iteratively_make_unit_tests_pass(
    solve_aoc_problem_req: AoCProblem,
    solutions_dir: str,
    problem_part: ExtractedProblemPart,
    extracted_examples: AoCProblemExtractedExamples,
    examples_context: ExamplesContext,
    unit_tests: GenerateUnitTestsOutput,
    implementation: GenerateImplementationOutput,
) -> tuple[GenerateUnitTestsOutput, GenerateImplementationOutput]:
    # Run an initial test to see where we're at. Maybe we get lucky and it works first try.
    unit_test_results = await _run_unit_tests(solve_aoc_problem_req)

    attempt = 0
    while True:
        attempt += 1
        match unit_test_results.result:
            case TestResults.Failure() as test_failure:
                if attempt >= _MAX_UNIT_TEST_FIX_ITERATIONS:
                    break  # Failed too many times, fallthrough to throwing exception.

                theorized_solution = await workflow.execute_activity(
                    debug_unit_test_failures,
                    DebugUnitTestFailuresArgs(
                        problem_html=problem_part.problem_html,
                        examples_context=examples_context,
                        unit_tests_src=unit_tests.generated_unit_tests,
                        generated_impl_src=implementation.generated_implementation,
                        error_msg=test_failure.err_msg,
                    ),
                    start_to_close_timeout=timedelta(seconds=60),
                    retry_policy=RetryPolicy(maximum_attempts=3),
                )
                if theorized_solution.optional_theorized_implementation_fix:
                    # Use the theorized solution to plan a refactoring.
                    impl_refactoring_plan = await workflow.execute_activity(
                        plan_impl_refactoring,
                        PlanImplRefactoringArgs(
                            examples=extracted_examples,
                            examples_context=examples_context,
                            generated_impl_src=implementation.generated_implementation,
                            theorized_solution=theorized_solution,
                        ),
                        start_to_close_timeout=timedelta(seconds=60),
                        retry_policy=RetryPolicy(maximum_attempts=3),
                    )

                async def fix_unit_tests() -> GenerateUnitTestsOutput:
                    return await workflow.execute_activity(
                        get_generated_unit_tests,
                        GetGeneratedUnitTestsArgs(
                            examples=extracted_examples,
                            examples_context=examples_context,
                            debugging_prompt=DebuggingPrompt(
                                prior_msg_history=unit_tests.prompt_history,
                                error_msg=test_failure.err_msg,
                                theorized_solution=theorized_solution,
                                impl_refactoring_plan=None,
                            ),
                        ),
                        start_to_close_timeout=timedelta(seconds=60),
                        retry_policy=RetryPolicy(maximum_attempts=5),
                    )

                async def fix_implementation() -> GenerateImplementationOutput:
                    return await workflow.execute_activity(
                        get_generated_implementation,
                        GetGeneratedImplementationArgs(
                            extracted_problem_part=problem_part,
                            examples_context=examples_context,
                            solve_part_2=solve_aoc_problem_req.part == 2,
                            debugging_prompt=DebuggingPrompt(
                                prior_msg_history=implementation.prompt_history,
                                error_msg=test_failure.err_msg,
                                theorized_solution=theorized_solution,
                                impl_refactoring_plan=impl_refactoring_plan,
                            ),
                        ),
                        start_to_close_timeout=timedelta(seconds=60),
                        retry_policy=RetryPolicy(maximum_attempts=5),
                    )
                    # TODO(steving) Reconsider if this may be helpful.
                    # return GenerateImplementationOutput(
                    #     # Let's just keep the context short for now and only include the original
                    #     # prompt and the latest implementation.
                    #     prompt_history=[res.prompt_history[0], res.prompt_history[-1]],
                    #     generated_implementation=res.generated_implementation,
                    # )

                # Determine which source files the LLM wants to make changes to. Separate cases
                # for now literally just to execute these in parallel if LLM decides it needs to
                # update BOTH files at the same time.
                if (
                    theorized_solution.optional_theorized_unit_test_fix
                    and theorized_solution.optional_theorized_implementation_fix
                ):
                    unit_tests, implementation = await asyncio.gather(
                        fix_unit_tests(), fix_implementation()
                    )
                if theorized_solution.optional_theorized_unit_test_fix:
                    unit_tests = await fix_unit_tests()
                if theorized_solution.optional_theorized_implementation_fix:
                    implementation = await fix_implementation()

                await workflow.execute_activity(
                    commit_changes,
                    CommitChangesArgs(
                        aoc_problem=solve_aoc_problem_req,
                        solutions_dir=solutions_dir,
                        unit_tests=unit_tests.generated_unit_tests,
                        implementation=implementation.generated_implementation,
                        problem_input=problem_part.problem_input,
                        commit_message=f"""Unit Test Failure Fixes (#{attempt})

### Addressing the following unit test failures:
```json
{test_failure.model_dump_json(indent=4)}
```

### Theorized solution:
```json
{theorized_solution.model_dump_json(indent=4)}
```{f"""
### Implementation refactoring plan:
{impl_refactoring_plan.model_dump_json(indent=4)}
""" if theorized_solution.optional_theorized_implementation_fix else ""}
""",
                    ),
                    start_to_close_timeout=timedelta(seconds=60),
                    retry_policy=RetryPolicy(maximum_attempts=5),
                )

                # Finally, rerun the tests against the latest changes.
                unit_test_results = await _run_unit_tests(solve_aoc_problem_req)
            case _:
                # The tests passed! Return the latest updated source code.
                return unit_tests, implementation

    raise ApplicationError(
        f"Failed to pass unit tests after {_MAX_UNIT_TEST_FIX_ITERATIONS} debugging iterations."
    )


async def _run_unit_tests(solve_aoc_problem_req: AoCProblem) -> TestResults:
    return await workflow.execute_activity(
        run_generated_tests,
        solve_aoc_problem_req,
        start_to_close_timeout=timedelta(seconds=30),
        # Don't allow any retries for these unit tests.
    )
