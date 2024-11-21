import asyncio
from typing import cast

import asyncclick as click
from asyncclick import Choice
from pydantic import BaseModel, Field

from agent.adventofcode.contextualize_examples import (
    ExamplesContext,
    contextualize_examples,
)
from agent.adventofcode.extract_examples import (
    AoCProblemExtractedExamples,
    extract_examples_from_problem_html,
)
from agent.adventofcode.scrape_problems import ProblemPart, scrape_aoc
from agent.llm.gemini.configure_genai import configure_genai
from agent.llm.gemini.models import GeminiModel
from agent.llm.gemini.prompt import prompt


class GeneratedUnitTests(BaseModel):
    generated_unit_test_file_content: str = Field(
        description="The full text contents of a valid Python 3.12 file called `generated_tests.py`."  # noqa: E501
    )


async def generate_unit_tests(
    examples: AoCProblemExtractedExamples, examples_context: ExamplesContext
) -> GeneratedUnitTests:
    system_prompt_text = """
You are a skilled software test engineer skilled at writing Python 3.12, Pytest based unit tests based on sample input/output examples for a tested function described by its signature given as JSON.

Your goal is to provide succinct and correct unit tests that test the function over the given examples.

In the spirit of "TDD" (test-driven-development) you write unit tests BEFORE the function implementation itself, so, at the top of the test file you generate, include a description of what part of the problem the tests cover, so that the following implementation can follow.

Do not attempt to solve the problem; only generate unit tests for the given examples.

You MUST respond with a single complete Python 3.12 Pytest test suite. 
IMPORTANT: Import the tested function using `from solution import <tested function name here>`.
IMPORTANT: For each example, generate a distinct test function named with the `test_` prefix.
IMPORTANT: Make sure that any assertions provide EXPLICIT context on the input(s) to the tested function and the expected vs actual output.
"""  # noqa: E501
    return await prompt(
        GeminiModel.GEMINI_1_5_PRO,
        system_prompt=system_prompt_text,
        prompt=f"""
### Input/Output Examples:
{examples.model_dump_json(indent=2)}

### Examples Context:
{examples_context.model_dump_json(indent=2)}
""",
        response_type=GeneratedUnitTests,
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
    examples = await extract_examples_from_problem_html(problem_html=problem_html)
    examples_context = await contextualize_examples(
        problem_html=problem_html,
        examples=examples,
    )
    unit_tests = await generate_unit_tests(examples=examples, examples_context=examples_context)
    print(unit_tests)


if __name__ == "__main__":
    asyncio.run(_cmd())
