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
from agent.llm.anthropic.prompt import prompt as anthropic_prompt
from agent.llm.anthropic.models import AnthropicModel
from agent.llm.gemini.configure_genai import configure_genai
from agent.llm.gemini.models import GeminiModel
from agent.llm.gemini.prompt import (
    ModelMessage,
    PromptHistory,
    UserMessage,
    prompt as gemini_prompt,
)


class GenerateImplementationOutput(PromptHistory, BaseModel):
    generated_implementation: GeneratedImplementation


def _get_initial_attempt_system_prompt_text(
    solve_part_2: bool,
    part_1_generated_implementation: GenerateImplementationOutput | None,
) -> str:
    GENERATED_CODE_RULES = """
You MUST respond with a single complete Python 3.12 program with full type annotations. 
IMPORTANT: ONLY use imports from Python's stdlib. DO NOT use any third party libraries whatsoever in your implementation.
IMPORTANT: Your implementation MUST ONLY do I/O to read the problem input from stdin. You MUST NOT open any files.
IMPORTANT: Your implementation MUST include an implementation of the function for which unit tests have already been implemented.
IMPORTANT: The solution() function MUST take no args and read the input from stdin.
IMPORTANT: The solution() function MUST RETURN THE RESULT VALUE. Do not print anything to stdout.
"""

    INITIAL_ATTEMPT_SYSTEM_PROMPT_TEXT = f"""
You are a skilled software engineer, proficient at evaluating coding problems and writing simple and correct solutions using Python 3.12.

Ignore all HTML tags in the problem statement and focus on how you will implement a valid solution to the problem.

In the spirit of "TDD" (test-driven-development) unit tests have already been written before the implementation itself, so, make sure that your solution will pass the given sampled test cases.

Your goal is to provide a succinct and correct solution to the given coding problem that will handle the given examples and any other edge cases that tests are not explicitly given for.

Remember to ignore all HTML tags and carefully attempt to solve the problem.

{GENERATED_CODE_RULES}
{f"""
 !!!!MOST IMPORTANT!!!!: 
    - You are tasked with solving PART 2 of a multi-part problem that BUILDS ON TOP OF PART 1.
    - The problem parts 1 and 2 are denoted by the following HTML comments: "<!-- Part 1 -->", and "<!-- Part 2 -->".
    - You MUST FOCUS on part 2.
    - Keep in mind that part 2 is a modification/variation on part 1 so pay attention to how part 2 specifies modifications on part 1.
    - Part 2 specifies completely new example inputs and outputs - GENERATE A SOLUTION FOR PART 2 ONLY! 
{f"""
HERE IS A WORKING PYTHON PROGRAM THAT SOLVES PART 1 (you may make use of the logic within this program to solve part 2, but keep in mind that part 2 is a modification/variation on part 1 so pay attention to how part 2's solution will need to differ from the solution to part 1):
{part_1_generated_implementation.generated_implementation.generated_implementation_file_content}""" 
if part_1_generated_implementation else ""}
""" if solve_part_2 else ""}
"""  # noqa: E501
    return INITIAL_ATTEMPT_SYSTEM_PROMPT_TEXT


async def generate_implementation(
    problem_html: str,
    examples_context: ExamplesContext,
    solve_part_2: bool,
    part_1_generated_implementation: GenerateImplementationOutput | None = None,
    debugging_prompt: DebuggingPrompt | None = None,
) -> GenerateImplementationOutput:
    generate_implementation_prompt = _get_generate_implementation_prompt(
        problem_html=problem_html,
        examples_context=examples_context,
        debugging_prompt=debugging_prompt,
    )
    # The initial prompt will use the more capable Clause Sonnet 3.5 model, but subsequent debugging
    # requests will use Gemini 1.5 Pro.
    INITIAL_ATTEMPT_SYSTEM_PROMPT_TEXT = _get_initial_attempt_system_prompt_text(
        solve_part_2=solve_part_2,
        part_1_generated_implementation=part_1_generated_implementation,
    )

    attempts = 0
    MAX_RETRIES = 3
    while True:
        attempts += 1
        if debugging_prompt:
            generated_implementation = (
                await gemini_prompt(
                    # GeminiModel.GEMINI_1_5_PRO,
                    model=GeminiModel.GEMINI_2_0_FLASH_EXP,
                    subtask_name="generate-implementation",
                    # GeminiModel.GEMINI_EXP_1206,
                    system_prompt=INITIAL_ATTEMPT_SYSTEM_PROMPT_TEXT,
                    prompt=generate_implementation_prompt,
                    response_type=GeneratedImplementation,
                )
            ).unwrap()
        else:
            assert isinstance(generate_implementation_prompt[0], UserMessage), "Lazy coding"
            generated_implementation = await anthropic_prompt(
                model=AnthropicModel.CLAUDE_SONNET_3_5_OCT_2024,
                system_prompt=INITIAL_ATTEMPT_SYSTEM_PROMPT_TEXT,
                prompt=generate_implementation_prompt[0].msg,
                response_type=GeneratedImplementation,
            )

        if _implementation_is_updated(generated_implementation, debugging_prompt):
            break
        elif attempts > MAX_RETRIES:
            # TODO(steving) DROP THIS... but for now, allow a duplicated generation
            # raise ValueError(
            #     f"Failed to get LLM to generate a NEW implementation after {MAX_RETRIES} retries."
            # )
            break

    return GenerateImplementationOutput(
        prompt_history=[
            *generate_implementation_prompt,
            ModelMessage(msg=generated_implementation.model_dump()),
        ],
        generated_implementation=generated_implementation,
    )


def _implementation_is_updated(
    generated_impl: GeneratedImplementation, debugging_prompt: DebuggingPrompt | None
) -> bool:
    # Check if the generated implementation is updated by comparing it with the previous
    # implementation in the debugging prompt. This is essential to ensure that we actually
    # have something to commit to GitHub and then rerun tests on.
    if debugging_prompt is None:
        return True

    prev_impl = GeneratedImplementation.model_validate(
        # The last ModelMessage in the prompt history is the previous implementation.
        next(
            part
            for part in reversed(debugging_prompt.prior_msg_history)
            if isinstance(part, ModelMessage)
        ).msg
    )
    return (
        generated_impl.generated_implementation_file_content
        != prev_impl.generated_implementation_file_content
    )


def _get_generate_implementation_prompt(
    problem_html: str,
    examples_context: ExamplesContext,
    debugging_prompt: DebuggingPrompt | None = None,
) -> list[UserMessage | ModelMessage]:
    prompt: list[UserMessage | ModelMessage]

    if debugging_prompt:
        assert (
            debugging_prompt.impl_refactoring_plan is not None
        ), "Refactoring plan is required for debugging prompt"
        prompt = [
            *debugging_prompt.prior_msg_history,
            UserMessage(
                msg=f"""
The solution you previously generated was not completely correct, an issue was encountered when trying to run it.
Follow the error message below to correct any issues in the generated solution.

IMPORTANT: Follow the given refactoring plan EXACTLY to fix the problem.

### Error Message:
{debugging_prompt.error_msg}

### Problem Explanation:
{debugging_prompt.theorized_solution.problem_explanation}

### Refactoring Plan:
{"\n".join(f"Step {n}: {step}" for n, step in enumerate(debugging_prompt.impl_refactoring_plan.plan))}
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
"""
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
    solve_part_2 = part == "2"
    examples_context = await contextualize_examples(
        problem_html=problem_html,
        examples=await extract_examples_from_problem_html(
            problem_html=problem_html, solve_part_2=solve_part_2
        ),
        solve_part_2=solve_part_2,
    )
    implementation = await generate_implementation(
        problem_html=problem_html, examples_context=examples_context, solve_part_2=solve_part_2
    )
    print(implementation)


if __name__ == "__main__":
    asyncio.run(_cmd())
