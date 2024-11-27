from pydantic import BaseModel, Field


class GeneratedUnitTests(BaseModel):
    generated_unit_test_file_content: str = Field(
        description="The full text contents of a valid Python 3.12 file called `generated_tests.py`."  # noqa: E501
    )
