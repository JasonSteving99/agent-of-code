from agent.adventofcode.contextualize_examples import ExamplesContext
from agent.adventofcode.debug.TheorizedSolution import TheorizedSolution
from agent.adventofcode.generate_code.GeneratedImplementation import (
    GeneratedImplementation,
)
from agent.adventofcode.generate_code.GeneratedUnitTests import GeneratedUnitTests
from agent.llm.gemini.models import GeminiModel
from agent.llm.gemini.prompt import prompt


async def theorize_solution(
    problem_html: str,
    examples_context: ExamplesContext,
    unit_tests_src: GeneratedUnitTests,
    generated_impl_src: GeneratedImplementation,
    error_msg: str,
) -> TheorizedSolution:
    system_prompt_text = """
You are a skilled software engineer tasked with analyzing error messages raised from running Python 3.12 code and finding the problems/bugs in the code that caused the error.
You are also skilled at proposing CORRECT and ACTIONABLE theories on exactly how to solve problems and fix bugs in code.

In the spirit of "TDD" (test-driven-development) another engineer has run unit tests (tests.py) over their code implementation (solution.py), and you will help them to determine what's going wrong and how to fix it. 

Just for context, you will also be given the coding problem that they're trying to solve. Ignore all HTML tags in the problem statement and focus on how you will implement a valid solution to the problem.

You MUST respond with the specified JSON format.
"""  # noqa: E501
    return await prompt(
        GeminiModel.GEMINI_1_5_PRO,
        system_prompt=system_prompt_text,
        prompt=f"""
### Problem HTML:
{problem_html}

### Unit Tests (tests.py):
```python
{unit_tests_src.generated_unit_test_file_content}
```

## Unit Tests Context (this is what the unit tests SHOULD be doing):
{examples_context.model_dump_json(indent=2)}

### Tested Implementation (solution.py):
```python
{generated_impl_src.generated_implementation_file_content}
```

## Implementation rules:
IMPORTANT: Your implementation MUST include an implementation of the function for which unit tests have already been implemented.
IMPORTANT: The overall solution MUST be implemented as a function named `solution` that takes no args, reads the problem input from stdin, and returns the result (not printing anything to stdout).
IMPORTANT: The solution() function MUST RETURN THE RESULT VALUE. Do not just print the result to stdout.

### Unit Tests Error Message:
{error_msg}
""",
        response_type=TheorizedSolution,
    )
