import asyncclick as click
import aiohttp
from openai import OpenAI

from agent import settings
from agent.llm.openai.models import DALL_E_Model

_OPENAI_CLIENT = OpenAI(api_key=settings.OPENAI_API_KEY)


async def generate_image_to_url(prompt: str) -> str:
    response = _OPENAI_CLIENT.images.generate(
        model=DALL_E_Model.DALL_E_3,
        prompt=prompt,
        n=1,
        size="1024x1024",
        quality="standard",
        response_format="url",
    )
    match response.data[0].url:
        case None:
            raise ValueError("No image data found")
        case url:
            return url


async def download_image(url: str, save_path: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()  # Let me know if there was some issue.

            data = await response.read()
            with open(save_path, "wb") as f:
                f.write(data)


@click.command()
@click.option("--prompt", required=True)
@click.option("--save-path", required=True)
async def main(prompt: str, save_path: str) -> None:
    url = await generate_image_to_url(prompt)
    await download_image(url, save_path)


if __name__ == "__main__":
    main()  # type: ignore
