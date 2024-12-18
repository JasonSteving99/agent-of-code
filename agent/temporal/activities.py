from pathlib import Path
import aiohttp
import os
from pydantic import BaseModel
from result import Err, Ok
from temporalio import activity

from agent.adventofcode import (
    AoCProblem,
    AoCProblemExtractedExamples,
    ExamplesContext,
    FileToCommit,
    contextualize_examples,
    execute_generated_solution,
    execute_tests,
    extract_examples_from_problem_html,
    generate_implementation,
    write_and_commit_changes,
)
from agent.adventofcode.debug.RefactoringPlan import RefactoringPlan
from agent.adventofcode.debug.debug_errors import theorize_solution, get_refactoring_plan
from agent.adventofcode.debug.DebuggingPrompt import DebuggingPrompt
from agent.adventofcode.debug.TheorizedSolution import TheorizedSolution
from agent.adventofcode.execute_generated_code import TestResults
from agent.adventofcode.generate_aoc_story_images import (
    ProblemStorySummary,
    extract_problem_story_summary,
    format_image_generation_prompt,
)
from agent.adventofcode.generate_code.generate_implementation import (
    GenerateImplementationOutput,
)
from agent.adventofcode.generate_code.generate_unit_tests import (
    GenerateUnitTestsOutput,
    generate_unit_tests,
)
from agent.adventofcode.generate_code.GeneratedImplementation import (
    GeneratedImplementation,
)
from agent.adventofcode.generate_code.GeneratedUnitTests import GeneratedUnitTests
from agent.adventofcode.scrape_problems import fetch_input, scrape_aoc
from agent.adventofcode.submit_solution import submit
from agent.llm.openai.generate_image import download_image, generate_image_to_url
from agent.llm.usage.LLMUsage import configure_llm_usage_logging


class ConfigureLLMUsageLoggingArgs(BaseModel):
    year: int
    day: int
    log_dir: str


@activity.defn
async def configure_llm_usage_logging_for_workflow(args: ConfigureLLMUsageLoggingArgs) -> None:
    configure_llm_usage_logging(
        execution_name=f"AgentOfCode-{args.year}-{args.day}", log_dir=Path(args.log_dir)
    )


class ExtractProblemPartArgs(BaseModel):
    aoc_problem: AoCProblem
    solutions_dir: str


class ExtractedProblemPart(BaseModel):
    problem_html: str
    problem_input: str


@activity.defn
async def extract_problem_part(args: ExtractProblemPartArgs) -> ExtractedProblemPart:
    # Make the solutions directory if it doesn't already exist.
    part_solutions_dir = os.path.join(args.solutions_dir, f"part{args.aoc_problem.part}")
    os.makedirs(part_solutions_dir, exist_ok=True)

    async with aiohttp.ClientSession() as session:
        return ExtractedProblemPart(
            problem_html=await scrape_aoc(
                session=session,
                year=args.aoc_problem.year,
                day=args.aoc_problem.day,
                part=args.aoc_problem.part,
                # Cache to `advent_of_code/year*/day*/part*/` dir, since this will NOT be shared
                # between part1 and part2.
                solutions_dir=part_solutions_dir,
            ),
            problem_input=await fetch_input(
                session=session,
                year=args.aoc_problem.year,
                day=args.aoc_problem.day,
                # Intentionally cache to top level `advent_of_code/year*/day*/` dir, since this will
                # be shared between part1 and part2.
                solutions_dir=args.solutions_dir,
            ),
        )


class ExtractExamplesArgs(BaseModel):
    extracted_problem_part: ExtractedProblemPart
    solve_part_2: bool


@activity.defn
async def extract_examples(args: ExtractExamplesArgs) -> AoCProblemExtractedExamples:
    return await extract_examples_from_problem_html(
        problem_html=args.extracted_problem_part.problem_html, solve_part_2=args.solve_part_2
    )


class GetExamplesContextArgs(BaseModel):
    extracted_problem_part: ExtractedProblemPart
    extracted_examples: AoCProblemExtractedExamples
    solve_part_2: bool


@activity.defn
async def get_examples_context(args: GetExamplesContextArgs) -> ExamplesContext:
    return await contextualize_examples(
        problem_html=args.extracted_problem_part.problem_html,
        examples=args.extracted_examples,
        solve_part_2=args.solve_part_2,
    )


class GetGeneratedUnitTestsArgs(BaseModel):
    examples: AoCProblemExtractedExamples
    examples_context: ExamplesContext
    debugging_prompt: DebuggingPrompt | None = None


@activity.defn
async def get_generated_unit_tests(args: GetGeneratedUnitTestsArgs) -> GenerateUnitTestsOutput:
    return await generate_unit_tests(
        examples=args.examples,
        examples_context=args.examples_context,
        debugging_prompt=args.debugging_prompt,
    )


class GetGeneratedImplementationArgs(BaseModel):
    extracted_problem_part: ExtractedProblemPart
    examples_context: ExamplesContext
    solve_part_2: bool
    part_1_generated_implementation: GenerateImplementationOutput | None = None
    debugging_prompt: DebuggingPrompt | None = None


@activity.defn
async def get_generated_implementation(
    args: GetGeneratedImplementationArgs,
) -> GenerateImplementationOutput:
    return await generate_implementation(
        problem_html=args.extracted_problem_part.problem_html,
        examples_context=args.examples_context,
        solve_part_2=args.solve_part_2,
        part_1_generated_implementation=args.part_1_generated_implementation,
        debugging_prompt=args.debugging_prompt,
    )


class CommitChangesArgs(BaseModel):
    aoc_problem: AoCProblem
    files: list[FileToCommit]
    solutions_dir: str
    commit_message: str
    dry_run: bool


@activity.defn
async def commit_changes(
    args: CommitChangesArgs,
) -> None:
    return write_and_commit_changes(
        basedir=args.solutions_dir,
        files=args.files,
        aoc_problem=args.aoc_problem,
        commit_message=args.commit_message,
        dry_run=args.dry_run,
    )


@activity.defn
async def run_generated_tests(aoc_problem: AoCProblem) -> TestResults:
    return execute_tests(year=aoc_problem.year, day=aoc_problem.day, part=aoc_problem.part)


class GeneratedSolutionRes(BaseModel):
    class Success(BaseModel):
        output: str

    class Failure(BaseModel):
        exit_code: int
        std_err: str

    result: Success | Failure


@activity.defn
async def run_generated_solution(
    aoc_problem: AoCProblem,
) -> GeneratedSolutionRes:
    match execute_generated_solution(
        year=aoc_problem.year, day=aoc_problem.day, part=aoc_problem.part
    ):
        case Ok(output):
            return GeneratedSolutionRes(result=GeneratedSolutionRes.Success(output=output))
        case Err(err):
            return GeneratedSolutionRes(
                result=GeneratedSolutionRes.Failure(exit_code=err.returncode, std_err=err.stderr)
            )
        case _:
            raise ValueError("Unexpected execute generated solution result")


class DebugUnitTestFailuresArgs(BaseModel):
    problem_html: str
    examples_context: ExamplesContext
    unit_tests_src: GeneratedUnitTests
    generated_impl_src: GeneratedImplementation
    error_msg: str


@activity.defn
async def debug_unit_test_failures(args: DebugUnitTestFailuresArgs) -> TheorizedSolution:
    return await theorize_solution(
        problem_html=args.problem_html,
        examples_context=args.examples_context,
        unit_tests_src=args.unit_tests_src,
        generated_impl_src=args.generated_impl_src,
        error_msg=args.error_msg,
    )


class PlanImplRefactoringArgs(BaseModel):
    examples: AoCProblemExtractedExamples
    examples_context: ExamplesContext
    generated_impl_src: GeneratedImplementation
    theorized_solution: TheorizedSolution


@activity.defn
async def plan_impl_refactoring(args: PlanImplRefactoringArgs) -> RefactoringPlan:
    assert (
        args.theorized_solution.optional_theorized_implementation_fix
    ), "Expected a theorized impl fix to be set."

    return await get_refactoring_plan(
        examples=args.examples,
        examples_context=args.examples_context,
        generated_impl_src=args.generated_impl_src,
        theorized_implementation_fix=args.theorized_solution.optional_theorized_implementation_fix,
    )


class SubmitSolutionArgs(BaseModel):
    aoc_problem: AoCProblem
    solution: str
    base_dir: str


@activity.defn
async def submit_solution(args: SubmitSolutionArgs) -> bool:
    return await submit(
        year=args.aoc_problem.year,
        day=args.aoc_problem.day,
        part=args.aoc_problem.part,
        answer=args.solution,
        base_dir=args.base_dir,
    )


@activity.defn
async def extract_story_summary(problem_html: str) -> ProblemStorySummary:
    return await extract_problem_story_summary(problem_html)


@activity.defn
async def meta_get_image_generation_prompt(problem_story_summary: ProblemStorySummary) -> str:
    return await format_image_generation_prompt(problem_story_summary)


class GenerateCelebratoryImageArgs(BaseModel):
    image_generation_prompt: str
    solutions_dir: str


@activity.defn
async def generate_celebratory_image(args: GenerateCelebratoryImageArgs) -> None:
    await download_image(
        await generate_image_to_url(args.image_generation_prompt),
        os.path.join(args.solutions_dir, "generated_aoc_story_image.png"),
    )
