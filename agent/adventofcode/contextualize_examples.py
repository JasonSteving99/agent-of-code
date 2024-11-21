import asyncio
from typing import cast

import asyncclick as click
from asyncclick import Choice
from pydantic import BaseModel

from agent.adventofcode.extract_examples import (
    AoCProblemExtractedExamples,
    extract_examples_from_problem_html,
)
from agent.adventofcode.scrape_problems import ProblemPart, scrape_aoc
from agent.llm.gemini.configure_genai import configure_genai
from agent.llm.gemini.models import GeminiModel
from agent.llm.gemini.prompt import prompt


class ExamplesContext(BaseModel):
    examples_context: str
    suggested_tested_function_name: str


async def contextualize_examples(
    problem_html: str, examples: AoCProblemExtractedExamples
) -> ExamplesContext:
    system_prompt_text = """
You are a skilled technical reader tasked with analyzing coding problems presented within HTML, and sample input/output examples for the coding problem.

Your goal is to provide succinct and helpful information on the examples that provides context on what exactly the examples demonstrate from the perspective of enabling someone to write unit tests of an implementation solving the coding problem.

In the spirit of "TDD" (test-driven-development) we're doing this so that we can write unit tests *before* writing the implementation, so, when you're contextualizing the examples, come up with a suggested name for a function that the implementation should follow.

Ignore all HTML tags and focus solely on the input/output data. Do not attempt to solve the problem; only contextualize the examples.

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
    problem_html = await scrape_aoc(year=year, day=day, part=cast(ProblemPart, int(part)))
    print(
        await contextualize_examples(
            problem_html=problem_html,
            examples=await extract_examples_from_problem_html(problem_html=problem_html),
        )
    )


if __name__ == "__main__":
    asyncio.run(_cmd())
