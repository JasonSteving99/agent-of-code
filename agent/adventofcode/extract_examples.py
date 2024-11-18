import asyncio
from typing import cast
import asyncclick as click
from asyncclick import Choice
from pydantic import BaseModel

from agent.adventofcode.scrape_problems import scrape_aoc, ProblemPart
from agent.llm.gemini.configure_genai import configure_genai
from agent.llm.gemini.models import GeminiModel
from agent.llm.gemini.prompt import prompt


class AoCProblemExtractedExamples(BaseModel):
    class Example(BaseModel):
        description: str
        input: str
        output: str

    examples: list[Example]


async def extract_examples_from_problem_html(problem_html: str) -> AoCProblemExtractedExamples:
    system_prompt_text = """
You are a skilled technical reader tasked with extracting input/output examples from coding problems presented within HTML. Your goal is to provide these examples in a format suitable for unit testing.

Ignore all HTML tags and focus solely on the input/output data. Do not attempt to solve the problem; only extract the examples.

Remember to ignore all HTML tags and do not attempt to solve the problem. Extract ONLY the example inputs and outputs in the JSON format specified.
"""  # noqa: E501
    return await prompt(
        GeminiModel.GEMINI_1_5_PRO,
        system_prompt=system_prompt_text,
        prompt=problem_html,
        response_type=AoCProblemExtractedExamples,
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
    print(
        await extract_examples_from_problem_html(
            await scrape_aoc(year=year, day=day, part=cast(ProblemPart, int(part)))
        )
    )


if __name__ == "__main__":
    asyncio.run(_cmd())
