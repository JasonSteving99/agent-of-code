from pydantic import BaseModel

from agent.adventofcode.debug.RefactoringPlan import RefactoringPlan
from agent.adventofcode.debug.TheorizedSolution import TheorizedSolution
from agent.llm.gemini.prompt import ModelMessage, UserMessage


class DebuggingPrompt(BaseModel):
    prior_msg_history: list[UserMessage | ModelMessage]
    error_msg: str
    theorized_solution: TheorizedSolution
    impl_refactoring_plan: RefactoringPlan | None
