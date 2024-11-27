import json
from dataclasses import dataclass
from typing import Any, Literal, Protocol

import google.generativeai as genai
from google.generativeai.types import ContentDict, HarmBlockThreshold, HarmCategory
from pydantic import BaseModel

from agent.llm.gemini.models import GeminiModel

# Avoid being so dang conservative. Answer the questions!
SAFETY_SETTINGS = {
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
}


class ToContentDict(Protocol):
    def to_content_dict(self) -> ContentDict: ...


class UserMessage(BaseModel):
    msg: str
    role: Literal["user"] = "user"

    def to_content_dict(self) -> ContentDict:
        return _get_content_dict(msg=self.msg, role=self.role)


class ModelMessage(BaseModel):
    msg: dict[str, Any]
    role: Literal["model"] = "model"

    def to_content_dict(self) -> ContentDict:
        return _get_content_dict(msg=json.dumps(self.msg, indent=2), role=self.role)


@dataclass
class TextModelMessage:
    msg: str
    role: Literal["model"] = "model"

    def to_content_dict(self) -> ContentDict:
        return _get_content_dict(msg=self.msg, role=self.role)


def _get_content_dict(msg: str, role: Literal["user", "model"]) -> ContentDict:
    return {
        "parts": [msg],
        "role": role,
    }


async def prompt[ResponseType: BaseModel](
    model: GeminiModel,
    system_prompt: str,
    prompt: str | list[UserMessage | ModelMessage],
    response_type: type[ResponseType],
) -> ResponseType:
    return response_type.model_validate_json(
        await _prompt(
            model=model,
            system_prompt=system_prompt,
            prompt=prompt,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
                response_schema=response_type,
            ),
        )
    )


async def text_prompt(
    model: GeminiModel,
    system_prompt: str,
    prompt: str | list[UserMessage | TextModelMessage],
) -> str:
    return await _prompt(
        model=model, system_prompt=system_prompt, prompt=prompt, generation_config=None
    )


async def _prompt(
    model: GeminiModel,
    system_prompt: str,
    prompt: str | list[UserMessage | ModelMessage] | list[UserMessage | TextModelMessage],
    generation_config: genai.GenerationConfig | None,
) -> str:
    return (
        await genai.GenerativeModel(
            model, safety_settings=SAFETY_SETTINGS, system_instruction=system_prompt
        ).generate_content_async(
            prompt if isinstance(prompt, str) else [msg.to_content_dict() for msg in prompt],
            generation_config=generation_config,
        )
    ).text


class PromptHistory(BaseModel):
    prompt_history: list[UserMessage | ModelMessage]