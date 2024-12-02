import asyncio
from typing import cast
import asyncclick as click
import aiohttp
import os

from agent.adventofcode.problem_part import ProblemPart
from agent.adventofcode._HEADERS import _HEADERS


async def submit(
    year: int,
    day: int,
    part: ProblemPart,
    answer: str,
    base_dir: str,
) -> bool:
    """Submit solution to Advent of Code"""
    # Check existence of cached solution to check against first.
    cached_solution_path = os.path.join(base_dir, "solution.txt")
    if os.path.isfile(cached_solution_path):
        with open(cached_solution_path, "r") as f:
            cached_solution = f.read().strip()
            if cached_solution == answer.strip():
                click.echo("Correct answer! 🎉")
                return True
            else:
                click.echo("Wrong answer 😢")
                return False

    url = f"https://adventofcode.com/{year}/day/{day}/answer"

    data = {"level": str(part), "answer": answer}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=_HEADERS, data=data) as response:
            text = await response.text()
            if "That's the right answer" in text:
                click.echo("Correct answer! 🎉")
                # Write the solution to a file so that we can check against it next time.
                with open(cached_solution_path, "w") as f:
                    f.write(answer.strip())
                return True
            elif "That's not the right answer" in text:
                click.echo("Wrong answer 😢")
                return False
            else:
                raise ValueError(f"UNEXPECTED AoC ANSWER RESPONSE!\n{text}")


@click.command()
@click.option("--year", required=True)
@click.option("--day", required=True)
@click.option("--part", type=click.Choice(["1", "2"]), default="1")
@click.option("--answer", type=str, required=True, help="Answer to submit")
@click.option(
    "--base-dir",
    type=str,
    required=True,
    help="Path to the day's solution dir so that we can cache the solution to this part and transparently check solutions against local results. Just being friendly to the AoC maintainer. I don't need to be hitting their server more often than absolutely necessary.",  # noqa: E501
)
async def cmd(
    year: int,
    day: int,
    part: str,  # type: ignore - Need to redeclare with a cast after parsing into an int.
    answer: str,
    base_dir: str,
) -> bool:
    return await submit(
        year=year, day=day, part=cast(ProblemPart, int(part)), answer=answer, base_dir=base_dir
    )


if __name__ == "__main__":
    asyncio.run(cmd())
