import anthropic
from pydantic import BaseModel
from result import Err, Ok, Result

from agent import settings
from agent.llm.anthropic.models import ANTHROPIC_PROVIDER_NAME, AnthropicModel
from agent.llm.usage.LLMUsage import LLMError, LLMUsage, Model, log_llm_usage


_CLIENT = anthropic.AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)


@log_llm_usage(provider=ANTHROPIC_PROVIDER_NAME, model=Model.DYNAMIC_MODEL_CHOICE)
async def prompt[ResponseType: BaseModel](
    *,
    model: AnthropicModel,
    subtask_name: str,
    system_prompt: str,
    prompt: str | list[anthropic.types.MessageParam],
    response_type: type[ResponseType],
) -> LLMUsage[ResponseType]:
    JSON_RESPONSE_TYPE_TOOL_NAME = "json_response_type_tool"
    try:
        raw_response = await _CLIENT.messages.create(
            model=model.value,
            max_tokens=2000,
            system=system_prompt,
            tools=[
                anthropic.types.ToolParam(
                    name=JSON_RESPONSE_TYPE_TOOL_NAME,
                    description=response_type.model_json_schema().get(
                        "description",
                        "The json response format that your response MUST follow.",
                    ),
                    input_schema=response_type.model_json_schema(),
                )
            ],
            tool_choice={"type": "tool", "name": JSON_RESPONSE_TYPE_TOOL_NAME},
            messages=[
                anthropic.types.MessageParam(
                    role="user",
                    content=[anthropic.types.TextBlockParam(type="text", text=prompt)],
                )
            ]
            if isinstance(prompt, str)
            else prompt,
        )
    except Exception as e:
        return LLMUsage(
            input_tokens=0,
            output_tokens=0,
            response=Err(LLMError(err_type=LLMError.ErrType.NO_RESPONSE, msg=str(e))),
        )

    response: Result[ResponseType, LLMError]
    input_tokens = raw_response.usage.input_tokens
    output_tokens = raw_response.usage.output_tokens
    if isinstance(raw_response.content[0], anthropic.types.ToolUseBlock):
        try:
            response = Ok(response_type.model_validate(raw_response.content[0].input))
        except Exception as e:
            response = Err(
                LLMError(err_type=LLMError.ErrType.RESPONSE_SCHEMA_VALIDATION_FAILED, msg=str(e))
            )
    else:
        response = Err(
            LLMError(
                err_type=LLMError.ErrType.UNEXPECTED_RESPONSE,
                msg=f"Unexpected response: {raw_response}",
            )
        )

    return LLMUsage(input_tokens=input_tokens, output_tokens=output_tokens, response=response)


@log_llm_usage(provider=ANTHROPIC_PROVIDER_NAME, model=Model.DYNAMIC_MODEL_CHOICE)
async def text_prompt(
    *,
    model: AnthropicModel,
    subtask_name: str,
    system_prompt: str,
    prompt: str | list[anthropic.types.MessageParam],
) -> LLMUsage[str]:
    try:
        raw_response = await _CLIENT.messages.create(
            model=model.value,
            max_tokens=2000,
            system=system_prompt,
            messages=[
                anthropic.types.MessageParam(
                    role="user", content=[anthropic.types.TextBlockParam(type="text", text=prompt)]
                )
            ]
            if isinstance(prompt, str)
            else prompt,
        )
    except Exception as e:
        return LLMUsage(
            input_tokens=0,
            output_tokens=0,
            response=Err(LLMError(err_type=LLMError.ErrType.NO_RESPONSE, msg=str(e))),
        )

    response: Result[str, LLMError]
    input_tokens = raw_response.usage.input_tokens
    output_tokens = raw_response.usage.output_tokens
    if isinstance(raw_response.content[0], anthropic.types.TextBlock):
        response = Ok(raw_response.content[0].text)
    else:
        response = Err(
            LLMError(
                err_type=LLMError.ErrType.UNEXPECTED_RESPONSE,
                msg=f"Unexpected response: {raw_response}",
            )
        )

    return LLMUsage(input_tokens=input_tokens, output_tokens=output_tokens, response=response)
