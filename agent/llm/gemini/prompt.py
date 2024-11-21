import google.generativeai as genai
from google.generativeai.types import HarmBlockThreshold, HarmCategory
from pydantic import BaseModel

from agent.llm.gemini.models import GeminiModel

# Avoid being so dang conservative. Answer the questions!
SAFETY_SETTINGS = {
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
}


async def prompt[ResponseType: BaseModel](
    model: GeminiModel, system_prompt: str, prompt: str, response_type: type[ResponseType]
) -> ResponseType:
    res = (
        await genai.GenerativeModel(
            model, safety_settings=SAFETY_SETTINGS, system_instruction=system_prompt
        ).generate_content_async(
            prompt,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
                response_schema=response_type,
            ),
        )
    ).text
    return response_type.model_validate_json(res)


async def text_prompt(model: GeminiModel, system_prompt: str, prompt: str) -> str:
    return (
        await genai.GenerativeModel(
            model, safety_settings=SAFETY_SETTINGS, system_instruction=system_prompt
        ).generate_content_async(prompt)
    ).text
