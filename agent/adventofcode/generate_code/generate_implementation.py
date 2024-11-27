import asyncio
from typing import cast

import aiohttp
import asyncclick as click
from pydantic import BaseModel

from agent.adventofcode.contextualize_examples import (
    ExamplesContext,
    contextualize_examples,
)
from agent.adventofcode.debug.DebuggingPrompt import DebuggingPrompt
from agent.adventofcode.extract_examples import extract_examples_from_problem_html
from agent.adventofcode.generate_code.GeneratedImplementation import (
    GeneratedImplementation,
)
from agent.adventofcode.problem_part import ProblemPart
from agent.adventofcode.scrape_problems import scrape_aoc
from agent.llm.gemini.configure_genai import configure_genai
from agent.llm.gemini.models import GeminiModel
from agent.llm.gemini.prompt import ModelMessage, PromptHistory, UserMessage, prompt


class GenerateImplementationOutput(PromptHistory, BaseModel):
    generated_implementation: GeneratedImplementation


async def generate_implementation(
    problem_html: str,
    examples_context: ExamplesContext,
    debugging_prompt: DebuggingPrompt | None = None,
) -> GenerateImplementationOutput:
    system_prompt_text = """
You are a skilled software engineer, proficient at evaluating coding problems and writing simple and correct solutions using Python 3.12.

Ignore all HTML tags in the problem statement and focus on how you will implement a valid solution to the problem.

In the spirit of "TDD" (test-driven-development) unit tests have already been written before the implementation itself, so, make sure that your solution will pass the given sampled test cases.

Your goal is to provide a succinct and correct solution to the given coding problem that will handle the given examples and any other edge cases that tests are not explicitly given for.

Remember to ignore all HTML tags and carefully attempt to solve the problem.

You MUST respond with a single complete Python 3.12 program with full type annotations. 
IMPORTANT: ONLY use imports from Python's stdlib. DO NOT use any third party libraries whatsoever in your implementation.
IMPORTANT: Your implementation MUST ONLY do I/O to read the problem input from stdin.
IMPORTANT: Your implementation MUST include an implementation of the function for which unit tests have already been implemented.
IMPORTANT: The overall solution MUST be implemented as a function named `solution` that takes no args, reads the problem input from stdin, and returns the result (not printing anything to stdout).
IMPORTANT: The solution() function MUST RETURN THE RESULT VALUE. Do not just print the result to stdout.
"""  # noqa: E501
    generate_implementation_prompt = _get_generate_implementation_prompt(
        problem_html=problem_html,
        examples_context=examples_context,
        debugging_prompt=debugging_prompt,
    )
    generated_implementation = await prompt(
        GeminiModel.GEMINI_1_5_PRO,
        system_prompt=system_prompt_text,
        prompt=generate_implementation_prompt,
        response_type=GeneratedImplementation,
    )
    return GenerateImplementationOutput(
        prompt_history=[
            *generate_implementation_prompt,
            ModelMessage(msg=generated_implementation.model_dump()),
        ],
        generated_implementation=generated_implementation,
    )


def _get_generate_implementation_prompt(
    problem_html: str,
    examples_context: ExamplesContext,
    debugging_prompt: DebuggingPrompt | None = None,
) -> list[UserMessage | ModelMessage]:
    prompt: list[UserMessage | ModelMessage]

    if debugging_prompt:
        prompt = [
            *debugging_prompt.prior_msg_history,
            UserMessage(
                msg=f"""
The solution you previously generated was not completely correct, an issue was encountered when trying to run it.
Follow the error message below to correct any issues in the generated solution.

IMPORTANT: Change as little code as possible to address the recommended fix.

### Problem Explanation:
{debugging_prompt.theorized_solution.problem_explanation}

### Suggested Fix:
{debugging_prompt.theorized_solution.optional_theorized_implementation_fix}
"""  # noqa: E501
            ),
        ]
    else:
        prompt = [
            UserMessage(
                msg=f"""
### Problem Statement HTML:
{problem_html}

### Existing Unit Tests:
{examples_context.model_dump_json(indent=2)}
""",
            )
        ]

    return prompt


@click.command()
@click.option("--year", required=True)
@click.option("--day", required=True)
@click.option("--part", type=click.Choice(["1", "2"]), default="1")
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
    examples_context = await contextualize_examples(
        problem_html=problem_html,
        examples=await extract_examples_from_problem_html(problem_html=problem_html),
    )
    implementation = await generate_implementation(
        problem_html=problem_html, examples_context=examples_context
    )
    print(implementation)


if __name__ == "__main__":
    asyncio.run(_cmd())
