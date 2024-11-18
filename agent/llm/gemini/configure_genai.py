from agent import settings

import google.generativeai as genai


def configure_genai() -> None:
    genai.configure(api_key=settings.GEMINI_API_KEY)
