import asyncio
from datetime import timedelta

from temporalio import workflow
from temporalio.common import RetryPolicy

# Imports passed through Temporal's sandbox without overriding stdlib.
with workflow.unsafe.imports_passed_through():
    from agent.temporal.activities import (
        AoCProblem,
        CommitChangesArgs,
        GeneratedSolutionRes,
        TestResults,
        commit_changes,
        extract_examples,
        extract_problem_part,
        get_examples_context,
        get_generated_implementation,
        get_generated_unit_tests,
        run_generated_solution,
        run_generated_tests,
    )


@workflow.defn
class SolveAoCProblemWorkflow:
    @workflow.run
    async def run(self, solve_aoc_problem_req: AoCProblem, solutions_dir: str) -> str:
        workflow.logger.info(
            f"Running SolveAoCProblemWorkflow with parameter {solve_aoc_problem_req}"
        )
        problem_part = await workflow.execute_activity(
            extract_problem_part,
            solve_aoc_problem_req,
            start_to_close_timeout=timedelta(seconds=15),
            retry_policy=RetryPolicy(
                maximum_attempts=5,
                # Try being a good citizen and don't spam retries to AoC's servers.
                initial_interval=timedelta(seconds=5),
                maximum_interval=timedelta(seconds=30),
            ),
        )

        extracted_examples = await workflow.execute_activity(
            extract_examples,
            problem_part,
            start_to_close_timeout=timedelta(seconds=20),
            retry_policy=RetryPolicy(maximum_attempts=5),
        )

        examples_context = await workflow.execute_activity(
            get_examples_context,
            args=[problem_part, extracted_examples],
            start_to_close_timeout=timedelta(seconds=20),
            retry_policy=RetryPolicy(maximum_attempts=5),
        )

        # Since I don't think I should show the unit tests to the LLM when asking it to generate the
        # implementation, I can just go ahead and generate the initial implementation concurrently.
        unit_tests, implementation = await asyncio.gather(
            workflow.execute_activity(
                get_generated_unit_tests,
                args=[extracted_examples, examples_context],
                start_to_close_timeout=timedelta(seconds=20),
                retry_policy=RetryPolicy(maximum_attempts=5),
            ),
            workflow.execute_activity(
                get_generated_implementation,
                args=[problem_part, examples_context],
                start_to_close_timeout=timedelta(seconds=20),
                retry_policy=RetryPolicy(maximum_attempts=5),
            ),
        )

        # Commit these initial tests and implementation files right away before executing any tests.
        # At this point, we're just ensuring that we can actually track the progress that this agent
        # makes since it'll be really interesting to go back through and evaluate this later on.
        await workflow.execute_activity(
            commit_changes,
            CommitChangesArgs(
                aoc_problem=solve_aoc_problem_req,
                solutions_dir=solutions_dir,
                unit_tests=unit_tests,
                implementation=implementation,
                problem_input=problem_part.problem_input,
                commit_message="Initial Attempt",
            ),
            start_to_close_timeout=timedelta(seconds=60),
            retry_policy=RetryPolicy(maximum_attempts=5),
        )

        # Now, actually run the generated unit tests to see if we're gonna be able to move forward.
        unit_test_results = await workflow.execute_activity(
            run_generated_tests,
            solve_aoc_problem_req,
            start_to_close_timeout=timedelta(seconds=30),
            # Don't allow any retries for these unit tests.
        )

        if isinstance(unit_test_results.result, TestResults.Failure):
            raise Exception("Unit Tests Failed! Need to figure out how to correct them.")

        problem_solution_result = await workflow.execute_activity(
            run_generated_solution,
            solve_aoc_problem_req,
            start_to_close_timeout=timedelta(minutes=5),
            # Don't allow any retries for execution of the actual problem solution.
        )

        if isinstance(problem_solution_result.result, GeneratedSolutionRes.Failure):
            raise Exception(
                "Problem solution threw an exception! Need to figure out how to correct it."
            )

        return problem_solution_result.result.output
