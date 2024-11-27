from pydantic import BaseModel, Field


def pop_default(s):
    s.pop("default")


class TheorizedSolution(BaseModel):
    problem_explanation: str = Field(
        description="A detailed description of the problem with the given program. This should NOT include a solution to the problem, just an explanation of the problem itself."  # noqa: E501
    )
    optional_theorized_unit_test_fix: str | None = Field(
        description="SET THIS FIELD IF THERE'S A PROBLEM IN THE UNIT TEST CODE (tests.py) ITSELF. A detailed theory on how to FIX the problem in the given UNIT TESTS. This may include code snippets, but should be primarily expressed in clear and concise English.",  # noqa: E501
        default=None,
        json_schema_extra=pop_default,
    )
    optional_theorized_implementation_fix: str | None = Field(
        description="SET THIS FIELD IF THERE'S A PROBLEM IN THE CODE OF THE IMPLEMENTATION (solution.py) ITSELF. A detailed theory on how to FIX the problem in the given IMPLEMENTATION. This may include code snippets, but should be primarily expressed in clear and concise English.",  # noqa: E501
        default=None,
        json_schema_extra=pop_default,
    )
