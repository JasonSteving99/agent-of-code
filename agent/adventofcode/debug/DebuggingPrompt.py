from pydantic import BaseModel

from agent.adventofcode.debug.TheorizedSolution import TheorizedSolution
from agent.llm.gemini.prompt import ModelMessage, UserMessage


class DebuggingPrompt(BaseModel):
    prior_msg_history: list[UserMessage | ModelMessage]
    theorized_solution: TheorizedSolution
