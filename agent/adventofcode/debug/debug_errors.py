from agent.adventofcode.contextualize_examples import ExamplesContext
from agent.adventofcode.debug.RefactoringPlan import RefactoringPlan
from agent.adventofcode.debug.TheorizedSolution import TheorizedSolution
from agent.adventofcode.extract_examples import AoCProblemExtractedExamples
from agent.adventofcode.generate_code.GeneratedImplementation import (
    GeneratedImplementation,
)
from agent.adventofcode.generate_code.GeneratedUnitTests import GeneratedUnitTests
from agent.llm.gemini.models import GeminiModel
from agent.llm.gemini.prompt import prompt

THEORIZING_SYSTEM_PROMPT_TEXT = """
You are a skilled software engineer tasked with analyzing error messages raised from running Python 3.12 code and finding the problems/bugs in the code that caused the error.
You are also skilled at proposing CORRECT and ACTIONABLE theories on exactly how to solve problems and fix bugs in code.

In the spirit of "TDD" (test-driven-development) another engineer has run unit tests (tests.py) over their code implementation (solution.py), and you will help them to determine what's going wrong and how to fix it. 

Just for context, you will also be given the coding problem that they're trying to solve. Ignore all HTML tags in the problem statement and focus on how you will implement a valid solution to the problem.

IMPORTANT!! Focus on a SINGLE concrete suggestion in your response. If there are multiple problems, don't try to solve everything all at once.

Carefully consider whether there are logical errors in the unit test (tests.py) or the implementation (solution.py), or potentially both.
You MUST respond with the specified JSON format.
"""  # noqa: E501


async def theorize_solution(
    problem_html: str,
    examples_context: ExamplesContext,
    unit_tests_src: GeneratedUnitTests,
    generated_impl_src: GeneratedImplementation,
    error_msg: str,
) -> TheorizedSolution:
    theorize_solution_prompt = f"""
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
"""

    # Ensure that the theorized solution generates at least one actionable code change.
    attempts = 0
    MAX_RETRIES = 3
    while True:
        attempts += 1
        theorized_solution = await prompt(
            GeminiModel.GEMINI_1_5_PRO,
            system_prompt=THEORIZING_SYSTEM_PROMPT_TEXT,
            prompt=theorize_solution_prompt,
            response_type=TheorizedSolution,
        )

        if (
            theorized_solution.optional_theorized_unit_test_fix
            or theorized_solution.optional_theorized_implementation_fix
        ):
            break
        elif attempts > MAX_RETRIES:
            raise ValueError(
                f"Invalid TheorizedSolution should come up with at least one actionable code change.\n{theorized_solution}"  # noqa: E501
            )

    return theorized_solution


PLANNING_SYSTEM_PROMPT_TEXT = """
You are an expert software engineer, proficient at evaluating coding puzzles and debugging Python 3.12 code that's attempting to solve it.

You will be presented with a puzzle summary, input/output examples, the buggy program, and a theorized bug fix.

Your goal is to come up with a straightforward plan to fix the buggy program so that it correctly solve the coding problem.

Format your plan as a list of numbered steps that would be easy to follow for any junior developer. Something like: 
```
1. <step 1 in <=200 chars>
...
N. <step N in <=200 chars>
```

Your plan must clearly express the necessary refactoring steps to fix the program.

IMPORTANT!!!! EACH STEP MUST BE INCREDIBLY EXPLICIT AND DETAILED SO THAT A JUNIOR DEVELOPER COULD BLINDLY TYPE IN THE SPECIFIED CHANGES TO THE CODE AND FIX THE PROGRAM.
"""  # noqa: E501


async def get_refactoring_plan(
    examples: AoCProblemExtractedExamples,
    examples_context: ExamplesContext,
    generated_impl_src: GeneratedImplementation,
    theorized_implementation_fix: str,
) -> RefactoringPlan:
    refactoring_plan = await prompt(
        GeminiModel.GEMINI_1_5_PRO,
        system_prompt=THEORIZING_SYSTEM_PROMPT_TEXT,
        prompt=f"""
### Coding Puzzle Summary:
{examples_context.examples_context}

### Input/Output Examples:
```json
{examples.model_dump_json(indent=2)}
```

## Unit Tests Context (this is the function implementation that the unit tests expect to be present in the solution):
{examples_context.tested_function_details.model_dump_json(indent=2)}

### Tested Implementation (solution.py):
```python
{generated_impl_src.generated_implementation_file_content}
```

### Theorized Bug Fix:
{theorized_implementation_fix}
""",  # noqa: E501
        response_type=RefactoringPlan,
    )

    # Ensure that the refactoring plan generates at least one actionable code change.
    if not refactoring_plan.plan:
        raise ValueError(
            "Invalid RefactoringPlan should come up with at least one actionable code change."
        )

    return refactoring_plan
