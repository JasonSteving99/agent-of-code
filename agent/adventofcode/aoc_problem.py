from pydantic import BaseModel

from agent.adventofcode.problem_part import ProblemPart


class AoCProblem(BaseModel):
    year: int
    day: int
    part: ProblemPart
