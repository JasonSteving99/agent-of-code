import asyncio
from typing import cast

import aiohttp
import asyncclick as click
from asyncclick import Choice
from bs4 import BeautifulSoup

from agent import settings
from agent.adventofcode.problem_part import ProblemPart

_HEADERS = {"Cookie": settings.AOC_COOKIE}


async def fetch_input(session: aiohttp.ClientSession, year: int, day: int) -> str:
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    async with session.get(url, headers=_HEADERS) as response:
        return await response.text()


async def fetch_problem(
    session: aiohttp.ClientSession, year: int, day: int, part: ProblemPart
) -> str:
    url = f"https://adventofcode.com/{year}/day/{day}"
    async with session.get(url, headers=_HEADERS) as response:
        return await response.text()


def parse_problem(html: str, part: ProblemPart):
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find_all("article", class_="day-desc")
    if article:
        # Let's just return the html as a string for now.
        return str(article[part - 1])
        # return article[part - 1].get_text(separator="\n", strip=False)
    return "Problem description not found."


async def scrape_aoc(session: aiohttp.ClientSession, year: int, day: int, part: ProblemPart) -> str:
    return parse_problem(
        await fetch_problem(session, year=year, day=day, part=part),
        part=part,
    )


@click.command()
@click.option("--year", required=True)
@click.option("--day", required=True)
@click.option("--part", type=Choice(["1", "2"]), default="1")
async def _cmd(
    year: int,
    day: int,
    part: str,  # type: ignore - Need to redeclare with a cast after parsing into an int.
) -> None:
    async with aiohttp.ClientSession() as session:
        print(
            await scrape_aoc(session=session, year=year, day=day, part=cast(ProblemPart, int(part)))
        )


if __name__ == "__main__":
    asyncio.run(_cmd())
