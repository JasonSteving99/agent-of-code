import asyncio
from typing import cast

import aiohttp
import asyncclick as click
from asyncclick import Choice
from pydantic import BaseModel

from agent.adventofcode.scrape_problems import ProblemPart, scrape_aoc
from agent.llm.gemini.configure_genai import configure_genai
from agent.llm.gemini.models import GeminiModel
from agent.llm.gemini.prompt import prompt


class AoCProblemExtractedExamples(BaseModel):
    class Example(BaseModel):
        input: str
        output: str

    examples: list[Example]


async def extract_examples_from_problem_html(
    problem_html: str, solve_part_2: bool
) -> AoCProblemExtractedExamples:
    system_prompt_text = f"""
You are a skilled technical reader tasked with extracting input/output examples from coding problems presented within HTML. Your goal is to provide these examples in a format suitable for unit testing.

Don't get confused by HTML tags and focus solely on the input/output data. Do not attempt to solve the problem; only extract the examples.

Extract ONLY the example inputs and outputs in the JSON format specified.

{"""
 !!!!MOST IMPORTANT!!!!: 
    - You are tasked with solving PART 2 of a multi-part problem that BUILDS ON TOP OF PART 1.
    - The problem parts 1 and 2 are denoted by the following HTML comments: "<!-- Part 1 -->", and "<!-- Part 2 -->".
    - You MUST FOCUS on part 2.
    - Keep in mind that part 2 is a modification/variation on part 1 so pay attention to how part 2 specifies modifications on part 1.
    - Part 2 MAY EITHER specify completely new example inputs and outputs OR build on top of examples given in part 1 - IN EITHER CASE EXTRACT EXAMPLES THAT APPLY TO PART 2! 

 """ if solve_part_2 else ""}
IMPORTANT! You MUST return examples with a SINGLE input mapping to its SINGLE corresponding output.
"""  # noqa: E501
    extracted_examples = await prompt(
        GeminiModel.GEMINI_1_5_PRO,
        system_prompt=system_prompt_text,
        prompt=problem_html,
        response_type=AoCProblemExtractedExamples,
    )

    if len(extracted_examples.examples) == 0:
        raise ValueError(f"No examples extracted: {extracted_examples}")

    return extracted_examples


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
        print(
            await extract_examples_from_problem_html(
                await scrape_aoc(
                    session=session, year=year, day=day, part=cast(ProblemPart, int(part))
                ),
                solve_part_2=part == "2",
            )
        )


if __name__ == "__main__":
    asyncio.run(_cmd())
