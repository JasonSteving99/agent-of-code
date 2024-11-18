from pydantic import BaseModel
from temporalio import activity
from agent.adventofcode import ProblemPart
from agent.adventofcode.extract_examples import (
    AoCProblemExtractedExamples,
    extract_examples_from_problem_html,
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
