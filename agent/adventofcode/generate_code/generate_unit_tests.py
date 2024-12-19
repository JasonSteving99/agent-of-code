import asyncio
from typing import cast

import aiohttp
import asyncclick as click
from asyncclick import Choice
from pydantic import BaseModel

from agent.adventofcode.contextualize_examples import (
    ExamplesContext,
    contextualize_examples,
)
from agent.adventofcode.debug.DebuggingPrompt import DebuggingPrompt
from agent.adventofcode.extract_examples import (
    AoCProblemExtractedExamples,
    extract_examples_from_problem_html,
)
from agent.adventofcode.generate_code.GeneratedUnitTests import GeneratedUnitTests
from agent.adventofcode.scrape_problems import ProblemPart, scrape_aoc
from agent.llm.anthropic.models import AnthropicModel
from agent.llm.anthropic.prompt import prompt as anthropic_prompt
from agent.llm.gemini.configure_genai import configure_genai
from agent.llm.gemini.models import GeminiModel
from agent.llm.gemini.prompt import (
    ModelMessage,
    PromptHistory,
    UserMessage,
    prompt as gemini_prompt,
)


class GenerateUnitTestsOutput(PromptHistory, BaseModel):
    generated_unit_tests: GeneratedUnitTests


async def generate_unit_tests(
    examples: AoCProblemExtractedExamples,
    examples_context: ExamplesContext,
    debugging_prompt: DebuggingPrompt | None = None,
) -> GenerateUnitTestsOutput:
    system_prompt_text = """
You are a skilled software test engineer skilled at writing Python 3.12, Pytest based unit tests based on sample input/output examples for a tested function described by its signature given as JSON.

Your goal is to provide succinct and correct unit tests that test the function over the given examples.

In the spirit of "TDD" (test-driven-development) you write unit tests BEFORE the function implementation itself, so, at the top of the test file you generate, include a description of what part of the problem the tests cover, so that the following implementation can follow.

Do not attempt to solve the problem; ONLY generate unit tests for the given examples.

You MUST respond with a single complete Python 3.12 Pytest test suite. 
IMPORTANT: Import the tested function using `from solution import <tested function name here>`.
IMPORTANT: For each example, generate a distinct test function named with the `test_` prefix.
IMPORTANT: Make sure that any assertions provide EXPLICIT context on the input(s) to the tested function and the expected vs actual output.
IMPORTANT: Only generate unit tests for the given POSITIVE examples of valid input & output. Do not generate unit tests that validate that the program throws exceptions for invalid input.
"""  # noqa: E501

    generate_unit_tests_prompt = _get_generate_unit_tests_prompt(
        examples=examples,
        examples_context=examples_context,
        debugging_prompt=debugging_prompt,
    )
    # The initial prompt will use the more capable Clause Sonnet 3.5 model, but subsequent debugging
    # requests will use Gemini 1.5 Pro.
    if debugging_prompt:
        generated_unit_tests = (
            await gemini_prompt(
                model=GeminiModel.GEMINI_1_5_PRO,
                subtask_name="generate-unit-tests",
                system_prompt=system_prompt_text,
                prompt=generate_unit_tests_prompt,
                response_type=GeneratedUnitTests,
            )
        ).unwrap()
    else:
        assert isinstance(generate_unit_tests_prompt[0], UserMessage), "Lazy coding"
        generated_unit_tests = (
            await anthropic_prompt(
                model=AnthropicModel.CLAUDE_SONNET_3_5_OCT_2024,
                subtask_name="generate-unit-tests",
                system_prompt=system_prompt_text,
                prompt=generate_unit_tests_prompt[0].msg,
                response_type=GeneratedUnitTests,
            )
        ).unwrap()

    return GenerateUnitTestsOutput(
        prompt_history=[
            *generate_unit_tests_prompt,
            ModelMessage(msg=generated_unit_tests.model_dump()),
        ],
        generated_unit_tests=generated_unit_tests,
    )


def _get_generate_unit_tests_prompt(
    examples: AoCProblemExtractedExamples,
    examples_context: ExamplesContext,
    debugging_prompt: DebuggingPrompt | None,
) -> list[UserMessage | ModelMessage]:
    prompt: list[UserMessage | ModelMessage]

    if debugging_prompt:
        prompt = [
            *debugging_prompt.prior_msg_history,
            UserMessage(
                msg=f"""
The unit tests you previously generated were not completely correct, an issue was encountered when trying to run them.
Follow the error message below to correct any issues in the generated unit tests.

IMPORTANT: Change as little code as possible to address the recommended fix.

### Error Message:
{debugging_prompt.error_msg}

### Problem Explanation:
{debugging_prompt.theorized_solution.problem_explanation}

### Suggested Fix:
{debugging_prompt.theorized_solution.optional_theorized_unit_test_fix}
"""  # noqa: E501
            ),
        ]
    else:
        prompt = [
            UserMessage(
                msg=f"""
### Input/Output Examples:
{examples.model_dump_json(indent=2)}

### Examples Context:
{examples_context.model_dump_json(indent=2)}
"""
            )
        ]

    return prompt


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
    solve_part_2 = part == "2"
    examples = await extract_examples_from_problem_html(
        problem_html=problem_html, solve_part_2=solve_part_2
    )
    examples_context = await contextualize_examples(
        problem_html=problem_html, examples=examples, solve_part_2=solve_part_2
    )
    unit_tests = await generate_unit_tests(examples=examples, examples_context=examples_context)
    print(unit_tests)


if __name__ == "__main__":
    asyncio.run(_cmd())
