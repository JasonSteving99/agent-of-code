import os
from typing import cast

import asyncclick as click

from agent import settings
from agent.adventofcode.scrape_problems import ProblemPart
from agent.temporal.activities import AoCProblem
from agent.temporal.client import get_temporal_client
from agent.temporal.workflow import SolveAoCProblemWorkflow


@click.command()
@click.option("--year", required=True)
@click.option("--day", required=True)
@click.option("--part", type=click.Choice(["1", "2"]), default="1")
async def main(
    year: int,
    day: int,
    part: str,  # type: ignore - Need to redeclare with a cast after parsing into an int.
) -> None:
    # Need to get the path to the dir where solutions should be written. Implementing this to work
    # on various machines.
    aoc_solutions_dir = os.path.realpath(
        os.path.join(
            os.path.dirname(__file__),
            "../../advent_of_code",
            f"year{year}",
            f"day{day}",
            f"part{part}",
        )
    )

    # Create a client.
    client = await get_temporal_client()

    # Start the workflow.
    result = await client.execute_workflow(
        SolveAoCProblemWorkflow.run,
        args=[AoCProblem(year=year, day=day, part=cast(ProblemPart, int(part))), aoc_solutions_dir],
        id=f"solve-aoc-problem-{year}-{day}-{part}",
        task_queue=settings.TEMPORAL_TASK_QUEUE_NAME,
    )

    click.echo(f"Final problem result: {result}")


if __name__ == "__main__":
    main()
