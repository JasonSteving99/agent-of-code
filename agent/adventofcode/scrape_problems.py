import asyncio
from typing import cast

import aiohttp
import asyncclick as click
from asyncclick import Choice
from bs4 import BeautifulSoup

from agent.adventofcode._HEADERS import _HEADERS
from agent.adventofcode.problem_part import ProblemPart
import os


async def fetch_input(
    session: aiohttp.ClientSession, year: int, day: int, solutions_dir: str
) -> str:
    # Check if the input file already exists in the solutions directory.
    input_file_path = os.path.join(solutions_dir, "input.txt")
    if os.path.isfile(input_file_path):
        with open(input_file_path, "r") as f:
            return f.read()

    # Otherwise, fetch the input from the Advent of Code servers.
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    async with session.get(url, headers=_HEADERS) as response:
        input = await response.text()
        # Cache the input so we don't need to read it again later on.
        with open(input_file_path, "w") as f:
            f.write(input)
        return input


async def fetch_problem(
    session: aiohttp.ClientSession, year: int, day: int, solutions_dir: str | None
) -> str:
    if solutions_dir:
        # Check if the problem html file already exists in the solutions directory.
        problem_html_file_path = os.path.join(solutions_dir, "problem.html")
        if os.path.isfile(problem_html_file_path):
            with open(problem_html_file_path, "r") as f:
                return f.read()

    # Otherwise, fetch the input from the Advent of Code servers.
    url = f"https://adventofcode.com/{year}/day/{day}"
    async with session.get(url, headers=_HEADERS) as response:
        problem_html = await response.text()
        if solutions_dir:
            # Cache the input so we don't need to read it again later on.
            with open(problem_html_file_path, "w") as f:
                f.write(problem_html)
        return problem_html


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


async def scrape_aoc(
    session: aiohttp.ClientSession,
    year: int,
    day: int,
    part: ProblemPart,
    solutions_dir: str | None = None,
) -> str:
    return parse_problem(
        await fetch_problem(session, year=year, day=day, solutions_dir=solutions_dir), part=part
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
