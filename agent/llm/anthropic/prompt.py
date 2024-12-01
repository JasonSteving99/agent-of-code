import anthropic
from pydantic import BaseModel

from agent import settings
from agent.llm.anthropic.models import AnthropicModel


_CLIENT = anthropic.AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)


async def prompt[ResponseType: BaseModel](
    model: AnthropicModel,
    system_prompt: str,
    prompt: str | list[anthropic.types.MessageParam],
    response_type: type[ResponseType],
) -> ResponseType:
    JSON_RESPONSE_TYPE_TOOL_NAME = "json_response_type_tool"
    response = (
        await _CLIENT.messages.create(
            model=model.value,
            max_tokens=2000,
            system=system_prompt,
            tools=[
                anthropic.types.ToolParam(
                    name=JSON_RESPONSE_TYPE_TOOL_NAME,
                    description=response_type.model_json_schema().get(
                        "description", "The json response format that your response MUST follow."
                    ),
                    input_schema=response_type.model_json_schema(),
                )
            ],
            tool_choice={"type": "tool", "name": JSON_RESPONSE_TYPE_TOOL_NAME},
            messages=[
                anthropic.types.MessageParam(
                    role="user", content=[anthropic.types.TextBlockParam(type="text", text=prompt)]
                )
            ]
            if isinstance(prompt, str)
            else prompt,
        )
    ).content[0]
    if isinstance(response, anthropic.types.ToolUseBlock):
        return response_type.model_validate(response.input)
    else:
        raise ValueError(f"Unexpected response: {response}")


async def text_prompt(
    model: AnthropicModel,
    system_prompt: str,
    prompt: str | list[anthropic.types.MessageParam],
) -> str:
    response = (
        await _CLIENT.messages.create(
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
    ).content[0]
    if isinstance(response, anthropic.types.TextBlock):
        return response.text
    else:
        raise ValueError(f"Unexpected response: {response}")
