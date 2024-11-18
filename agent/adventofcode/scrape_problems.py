import asyncio
from typing import Literal, cast
import aiohttp
from bs4 import BeautifulSoup
import asyncclick as click
from asyncclick import Choice
from agent import settings


ProblemPart = Literal[1] | Literal[2]


async def fetch_problem(
    session: aiohttp.ClientSession, year: int, day: int, part: ProblemPart
) -> str:
    url = f"https://adventofcode.com/{year}/day/{day}"
    headers = {"Cookie": settings.AOC_COOKIE}
    async with session.get(url, headers=headers) as response:
        return await response.text()


def parse_problem(html: str, part: ProblemPart):
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find_all("article", class_="day-desc")
    if article:
        # Let's just return the html as a string for now.
        return str(article[part - 1])
        # return article[part - 1].get_text(separator="\n", strip=False)
    return "Problem description not found."


async def scrape_aoc(year: int, day: int, part: ProblemPart) -> str:
    async with aiohttp.ClientSession() as session:
        html = await fetch_problem(session, year=year, day=day, part=part)

    return parse_problem(html, part=part)


@click.command()
@click.option("--year", required=True)
@click.option("--day", required=True)
@click.option("--part", type=Choice(["1", "2"]), default="1")
async def _cmd(
    year: int,
    day: int,
    part: str,  # type: ignore - Need to redeclare with a cast after parsing into an int.
) -> None:
    print(await scrape_aoc(year=year, day=day, part=cast(ProblemPart, int(part))))


if __name__ == "__main__":
    asyncio.run(_cmd())
