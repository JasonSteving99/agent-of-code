from pydantic import BaseModel
from temporalio import activity
from agent.adventofcode import ProblemPart
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
