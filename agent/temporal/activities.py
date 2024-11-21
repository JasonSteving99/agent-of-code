from pydantic import BaseModel
from temporalio import activity

from agent.adventofcode import (
    AoCProblemExtractedExamples,
    ExamplesContext,
    GeneratedUnitTests,
    ProblemPart,
    contextualize_examples,
    extract_examples_from_problem_html,
    generate_unit_tests,
)
from agent.adventofcode.scrape_problems import scrape_aoc


class AoCProblem(BaseModel):
    year: int
    day: int
    part: ProblemPart


class ExtractedProblemPart(BaseModel):
    problem_html: str


@activity.defn
async def extract_problem_part(aoc_problem: AoCProblem) -> ExtractedProblemPart:
    return ExtractedProblemPart(
        problem_html=await scrape_aoc(
            year=aoc_problem.year, day=aoc_problem.day, part=aoc_problem.part
        )
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
