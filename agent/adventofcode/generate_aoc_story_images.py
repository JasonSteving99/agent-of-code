import aiohttp
from typing import cast
import asyncclick as click
from pydantic import BaseModel, Field

from agent.adventofcode.problem_part import ProblemPart
from agent.adventofcode.scrape_problems import scrape_aoc
from agent.llm.gemini.configure_genai import configure_genai
from agent.llm.gemini.models import GeminiModel
from agent.llm.gemini.prompt import prompt, text_prompt
from agent.llm.openai.generate_image import download_image, generate_image_to_url


class ProblemStorySummary(BaseModel):
    summarized_story: str = Field(
        description="A short summary of the narrative story described in this problem - focus on the narrative and ignore any coding related specifics."  # noqa: E501
    )
    cast: list[str] = Field(description="A list of characters in the story.")
    setting: str = Field(
        description="A description of the setting of the story with enough detail that an artist could animate it."  # noqa: E501
    )


EXTRACT_PROBLEM_STORY_SUMMARY_PROMPT = """
You will be given an HTML specification of a coding puzzle framed as a NARRATIVE story about elves and maybe other festive characters.

Extract the following information from the given problem description:

- A short retelling of the ENTIRE narrative story framing the given puzzle - focus on the narrative and ignore any coding related specifics.
- A list of characters in the story.
- A description of the setting of the story with enough detail that an artist could animate it.

Return the information in the specified JSON format.
"""  # noqa: E501


async def extract_problem_story_summary(problem_html: str) -> ProblemStorySummary:
    return (
        await prompt(
            model=GeminiModel.GEMINI_1_5_PRO,
            subtask_name="extract-problem-story-summary",
            system_prompt=EXTRACT_PROBLEM_STORY_SUMMARY_PROMPT,
            prompt=problem_html,
            response_type=ProblemStorySummary,
        )
    ).unwrap()


IMAGE_GENERATION_PROMPT_CREATION_META_PROMPT = """You are an experienced prompt engineer, that knows how to create effective prompts to guide an image generation model.

You will be given a detailed summary of a narrative story, along with a list of characters, and a description of the setting.

Create a single prompt that will guide an image generation model to create an image that captures the essence of the story.

The prompt should be detailed, enough that the full story and setting are described, but not so long that it will distract an image generation model.

Ensure that the prompt directs the 2d-artist to create an image that is suitable for a Christmas-time, elf-themed graphic novel.

Also make sure that the resulting image ends up being cute and fun, and not too dark or serious. 

The resulting prompt should also include a SHORT prohibition on large amounts of text.

Return the prompt as a string with 5 sentences or less.
"""  # noqa: E501


async def format_image_generation_prompt(story_summary: ProblemStorySummary) -> str:
    image_generation_meta_prompt = f"""
You are a world-class 2d-artist.

Create a single image that captures the essence of the following story:

{story_summary.summarized_story}

The image should be set in the following setting:

{story_summary.setting}

The image should include the following characters:

    - {"\n\t- ".join(story_summary.cast)}

The image should be detailed, high-quality, and visually appealing.

The image should be suitable for a Christmas-time, elf-themed graphic novel.
"""  # noqa: E501

    _META_IMAGE_GEN_PROMPT_CREATION_SUBTASK_NAME = "meta-image-generation-prompt-creation"
    formatted_image_generation_prompt = (
        await text_prompt(
            model=GeminiModel.GEMINI_1_5_PRO,
            subtask_name=_META_IMAGE_GEN_PROMPT_CREATION_SUBTASK_NAME,
            system_prompt=IMAGE_GENERATION_PROMPT_CREATION_META_PROMPT,
            prompt=image_generation_meta_prompt,
        )
    ).unwrap()

    # OpenAI's image generation model has an input limit of 1000 characters.
    MAX_ATTEMPTS = 3
    i = 0
    while i < MAX_ATTEMPTS and len(formatted_image_generation_prompt) >= 1000:
        formatted_image_generation_prompt = (
            await text_prompt(
                model=GeminiModel.GEMINI_1_5_PRO,
                subtask_name=_META_IMAGE_GEN_PROMPT_CREATION_SUBTASK_NAME,
                system_prompt="You are an expert writer that's able to edit a text while maintaining its original meaning and descriptive power. You will be given text that was a bit too wordy, and you should rewrite it to be a bit shorter.",  # noqa: E501
                prompt=image_generation_meta_prompt,
            )
        ).unwrap()

    if len(formatted_image_generation_prompt) >= 1000:
        raise ValueError("Failed to generate a prompt that is less than 1000 characters.")

    return formatted_image_generation_prompt


@click.command()
@click.option("--year", required=True)
@click.option("--day", required=True)
@click.option("--part", type=click.Choice(["1", "2"]), default="1")
@click.option("--save-path", required=True)
async def main(
    year: int,
    day: int,
    part: str,  # type: ignore - Need to redeclare with a cast after parsing into an int.
    save_path: str,
) -> None:
    part: ProblemPart = cast(ProblemPart, int(part))

    async with aiohttp.ClientSession() as session:
        problem_html = await scrape_aoc(session=session, year=year, day=day, part=part)

    configure_genai()
    problem_story_summary = await extract_problem_story_summary(problem_html)
    print(problem_story_summary.model_dump_json(indent=4))

    image_generation_prompt = await format_image_generation_prompt(problem_story_summary)
    print(image_generation_prompt)

    url = await generate_image_to_url(image_generation_prompt)
    await download_image(url, save_path)


if __name__ == "__main__":
    main()  # type: ignore
