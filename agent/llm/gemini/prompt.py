import json
from dataclasses import dataclass
from typing import Any, Callable, Literal, Protocol

import google.generativeai as genai
from google.generativeai.types import ContentDict, HarmBlockThreshold, HarmCategory
from pydantic import BaseModel
from result import Err, Ok, Result

from agent.llm.gemini.models import GeminiModel, GEMINI_PROVIDER_NAME
from agent.llm.usage.LLMUsage import LLMError, log_llm_usage, Model, LLMUsage

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


@log_llm_usage(provider=GEMINI_PROVIDER_NAME, model=Model.DYNAMIC_MODEL_CHOICE)
async def prompt[ResponseType: BaseModel](
    *,  # Require all args to be passed as kwargs.
    model: GeminiModel,
    subtask_name: str,
    system_prompt: str,
    prompt: str | list[UserMessage | ModelMessage],
    response_type: type[ResponseType],
    extra_validation_fn: Callable[[ResponseType], Result[None, str]] | None = None,
) -> LLMUsage[ResponseType]:
    response = await _prompt(
        model=model,
        system_prompt=system_prompt,
        prompt=prompt,
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json",
            response_schema=response_type,
        ),
    )

    try:
        # Try to parse the response.
        response = response.map(response_type.model_validate_json)
        # Validate the response.
        if extra_validation_fn:
            match extra_validation_fn(response.response.unwrap()):
                case Err(err_msg):
                    response = LLMUsage(
                        input_tokens=response.input_tokens,
                        output_tokens=response.output_tokens,
                        response=Err(
                            LLMError(
                                err_type=LLMError.ErrType.LOGICAL_VALIDATION_FAILED,
                                msg=str(err_msg),
                            )
                        ),
                    )
        return response
    except Exception as e:
        return LLMUsage(
            input_tokens=response.input_tokens,
            output_tokens=response.output_tokens,
            response=Err(
                LLMError(err_type=LLMError.ErrType.RESPONSE_SCHEMA_VALIDATION_FAILED, msg=str(e))
            ),
        )


@log_llm_usage(provider=GEMINI_PROVIDER_NAME, model=Model.DYNAMIC_MODEL_CHOICE)
async def text_prompt(
    *,  # Require all args to be passed as kwargs.
    model: GeminiModel,
    subtask_name: str,
    system_prompt: str,
    prompt: str | list[UserMessage | TextModelMessage],
) -> LLMUsage[str]:
    return await _prompt(
        model=model, system_prompt=system_prompt, prompt=prompt, generation_config=None
    )


async def _prompt(
    model: GeminiModel,
    system_prompt: str,
    prompt: str | list[UserMessage | ModelMessage] | list[UserMessage | TextModelMessage],
    generation_config: genai.GenerationConfig | None,
) -> LLMUsage[str]:
    try:
        res = await genai.GenerativeModel(
            model, safety_settings=SAFETY_SETTINGS, system_instruction=system_prompt
        ).generate_content_async(
            prompt if isinstance(prompt, str) else [msg.to_content_dict() for msg in prompt],
            generation_config=generation_config,
        )
    except Exception as e:
        return LLMUsage(
            input_tokens=0,
            output_tokens=0,
            response=Err(LLMError(err_type=LLMError.ErrType.NO_RESPONSE, msg=str(e))),
        )

    output_tokens = res.usage_metadata.total_token_count - res.usage_metadata.prompt_token_count
    try:
        return LLMUsage(
            input_tokens=res.usage_metadata.prompt_token_count,
            output_tokens=output_tokens,
            response=Ok(res.text),  # res.text may raise ValueError.
        )
    except Exception as e:
        return LLMUsage(
            input_tokens=res.usage_metadata.prompt_token_count,
            output_tokens=output_tokens,
            response=Err(LLMError(err_type=LLMError.ErrType.UNEXPECTED_RESPONSE, msg=str(e))),
        )


class PromptHistory(BaseModel):
    prompt_history: list[UserMessage | ModelMessage]
