import asyncio
from typing import cast

import aiohttp
import asyncclick as click
from asyncclick import Choice
from pydantic import BaseModel, Field

from agent.adventofcode.extract_examples import (
    AoCProblemExtractedExamples,
    extract_examples_from_problem_html,
)
from agent.adventofcode.scrape_problems import ProblemPart, scrape_aoc
from agent.llm.gemini.configure_genai import configure_genai
from agent.llm.gemini.models import GeminiModel
from agent.llm.gemini.prompt import prompt


class ExamplesContext(BaseModel):
    class SuggestedTestedFunctionDetails(BaseModel):
        name: str = Field(
            description="Snake case suggested name for the function that these examples would serve as tests for."  # noqa: E501
        )
        input_type_annotations: list[str] = Field(
            description="A list of valid Python 3.12 type annotations representing the arguments to the tested function."  # noqa: E501
        )
        output_type_annotation: str = Field(
            description="A valid Python 3.12 type annotation representing the output of the tested function."  # noqa: E501
        )

    examples_context: str
    tested_function_details: SuggestedTestedFunctionDetails


async def contextualize_examples(
    problem_html: str, examples: AoCProblemExtractedExamples, solve_part_2: bool
) -> ExamplesContext:
    system_prompt_text = f"""
You are a skilled technical reader tasked with analyzing coding problems presented within HTML, and sample input/output examples for the coding problem.

Your goal is to provide succinct and helpful information on the examples that provides context on what exactly the examples demonstrate from the perspective of enabling someone to write unit tests of an implementation solving the coding problem.

In the spirit of "TDD" (test-driven-development) we're doing this so that we can write unit tests *before* writing the implementation, so, when you're contextualizing the examples, come up with a suggested name for a function that the implementation should follow.

Ignore all HTML tags and focus solely on the input/output data. Do not attempt to solve the problem; only contextualize the examples.

{"""
 !!!!MOST IMPORTANT!!!!: 
    - You are tasked with solving PART 2 of a multi-part problem that BUILDS ON TOP OF PART 1.
    - The problem parts 1 and 2 are denoted by the following HTML comments: "<!-- Part 1 -->", and "<!-- Part 2 -->".
    - You MUST FOCUS on part 2.
    - Keep in mind that part 2 is a modification/variation on part 1 so pay attention to how part 2 specifies modifications on part 1.
    - Part 2 specifies completely new example inputs and outputs - FOCUS ON EXAMPLES FOR PART 2 ONLY! 

 """ if solve_part_2 else ""}
You MUST respond with the specified JSON format.
"""  # noqa: E501
    return await prompt(
        GeminiModel.GEMINI_1_5_PRO,
        system_prompt=system_prompt_text,
        prompt=f"""
### Problem HTML:
{problem_html}

### Input/Output Examples:
{examples.model_dump_json(indent=2)}
""",
        response_type=ExamplesContext,
    )


@click.command()
@click.option("--year", required=True)
@click.option("--day", required=True)
@click.option("--part", type=Choice(["1", "2"]), default="1")
async def _cmd(
    year: int,
    day: int,
    part: str,  # type: ignore - Need to redeclare with a cast after parsing into an int.
) -> None:
    configure_genai()
    async with aiohttp.ClientSession() as session:
        problem_html = await scrape_aoc(
            session=session, year=year, day=day, part=cast(ProblemPart, int(part))
        )
    print(
        await contextualize_examples(
            problem_html=problem_html,
            examples=await extract_examples_from_problem_html(
                problem_html=problem_html, solve_part_2=part == "2"
            ),
            solve_part_2=part == "2",
        )
    )


if __name__ == "__main__":
    asyncio.run(_cmd())
