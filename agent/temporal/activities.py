import aiohttp
from pydantic import BaseModel
from result import Err, Ok
from temporalio import activity

from agent.adventofcode import (
    AoCProblem,
    AoCProblemExtractedExamples,
    ExamplesContext,
    FileToCommit,
    GeneratedImplementation,
    GeneratedUnitTests,
    contextualize_examples,
    execute_generated_solution,
    execute_tests,
    extract_examples_from_problem_html,
    generate_implementation,
    generate_unit_tests,
    write_and_commit_changes,
)
from agent.adventofcode.execute_generated_code import TestResults
from agent.adventofcode.scrape_problems import fetch_input, scrape_aoc


class ExtractedProblemPart(BaseModel):
    problem_html: str
    problem_input: str


@activity.defn
async def extract_problem_part(aoc_problem: AoCProblem) -> ExtractedProblemPart:
    async with aiohttp.ClientSession() as session:
        return ExtractedProblemPart(
            problem_html=await scrape_aoc(
                session=session, year=aoc_problem.year, day=aoc_problem.day, part=aoc_problem.part
            ),
            problem_input=await fetch_input(
                session=session, year=aoc_problem.year, day=aoc_problem.day
            ),
        )


@activity.defn
async def extract_examples(
    extracted_problem_part: ExtractedProblemPart,
) -> AoCProblemExtractedExamples:
    return await extract_examples_from_problem_html(
        problem_html=extracted_problem_part.problem_html
    )


@activity.defn
async def get_examples_context(
    extracted_problem_part: ExtractedProblemPart,
    extracted_examples: AoCProblemExtractedExamples,
) -> ExamplesContext:
    return await contextualize_examples(
        problem_html=extracted_problem_part.problem_html, examples=extracted_examples
    )


@activity.defn
async def get_generated_unit_tests(
    examples: AoCProblemExtractedExamples,
    examples_context: ExamplesContext,
) -> GeneratedUnitTests:
    return await generate_unit_tests(examples=examples, examples_context=examples_context)


@activity.defn
async def get_generated_implementation(
    extracted_problem_part: ExtractedProblemPart,
    examples_context: ExamplesContext,
) -> GeneratedImplementation:
    return await generate_implementation(
        problem_html=extracted_problem_part.problem_html, examples_context=examples_context
    )


class CommitChangesArgs(BaseModel):
    aoc_problem: AoCProblem
    solutions_dir: str
    unit_tests: GeneratedUnitTests
    implementation: GeneratedImplementation
    problem_input: str
    commit_message: str


@activity.defn
async def commit_changes(
    args: CommitChangesArgs,
) -> None:
    return write_and_commit_changes(
        basedir=args.solutions_dir,
        files=[
            FileToCommit(
                filename="tests.py", content=args.unit_tests.generated_unit_test_file_content
            ),
            FileToCommit(
                filename="solution.py",
                content=args.implementation.generated_implementation_file_content,
            ),
            FileToCommit(
                filename="input.txt",
                content=args.problem_input,
            ),
        ],
        aoc_problem=args.aoc_problem,
        commit_message=args.commit_message,
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
