import google.generativeai as genai
from pydantic import BaseModel

from agent.llm.gemini.models import GeminiModel
from google.generativeai.types import HarmCategory, HarmBlockThreshold


async def prompt[ResponseType: BaseModel](
    model: GeminiModel, system_prompt: str, prompt: str, response_type: type[ResponseType]
) -> ResponseType:
    res = (
        await genai.GenerativeModel(
            model,
            # Prevent this chatbot from being so dang conservative. Answer the questions!
            safety_settings={
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            },
            system_instruction=system_prompt,
        ).generate_content_async(
            prompt,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json", response_schema=response_type
            ),
        )
    ).text
    return response_type.model_validate_json(res)
