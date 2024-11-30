from pydantic import BaseModel, Field


class RefactoringPlan(BaseModel):
    class Step(BaseModel):
        step: str = Field(description="Refactoring step in <=200 chars.")

    plan: list[Step] = Field(description="Your plan to fix the buggy program.")
