from pydantic import BaseModel, Field


class GeneratedImplementation(BaseModel):
    generated_implementation_file_content: str = Field(
        description="The full text contents of a valid Python 3.12 file called `solution.py`."  # noqa: E501
    )
