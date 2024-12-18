from enum import StrEnum

GEMINI_PROVIDER_NAME = "Google"


class GeminiModel(StrEnum):
    GEMINI_2_0_FLASH_EXP = "gemini-2.0-flash-exp"
    GEMINI_1_5_PRO = "gemini-1.5-pro-002"
    GEMINI_1_5_FLASH_8B = "gemini-1.5-flash-8b"
    GEMINI_1_5_FLASH = "gemini-1.5-flash"
    GEMINI_EXP_1206 = "gemini-exp-1206"
