import asyncio
from typing import cast

import aiohttp
import asyncclick as click
from asyncclick import Choice
from bs4 import BeautifulSoup

from agent.adventofcode._HEADERS import _HEADERS
from agent.adventofcode.problem_part import ProblemPart


async def fetch_input(session: aiohttp.ClientSession, year: int, day: int) -> str:
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    async with session.get(url, headers=_HEADERS) as response:
        return await response.text()


async def fetch_problem(session: aiohttp.ClientSession, year: int, day: int) -> str:
    url = f"https://adventofcode.com/{year}/day/{day}"
    async with session.get(url, headers=_HEADERS) as response:
        return await response.text()


def parse_problem(html: str, part: ProblemPart) -> str:
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find_all("article", class_="day-desc")
    if article:
        # Let's just return the html as a string for now.
        part_1_html = str(article[0])
        match part:
            case 1:
                return part_1_html
            case 2:
                # Cheat a bit and embed a note directly within the page html telling the LLM that
                # we've already solved part 1 and only want it to focus on a solution to part 2.
                return f"""<main>
<!-- Part 1 -->
{part_1_html}
<p>Part 1 solved - great job! Now try to solve part 2!</p>
<!-- Part 2 -->
{str(article[1])}
</main>"""
        # return article[part - 1].get_text(separator="\n", strip=False)
    raise ValueError("Problem description not found.")


async def scrape_aoc(session: aiohttp.ClientSession, year: int, day: int, part: ProblemPart) -> str:
    return parse_problem(await fetch_problem(session, year=year, day=day), part=part)


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
