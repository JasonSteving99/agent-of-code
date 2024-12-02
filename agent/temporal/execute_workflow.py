import os

import asyncclick as click

from agent import settings
from agent.temporal.client import get_temporal_client
from agent.temporal.workflow import SolveAoCProblemWorkflow, SolveAoCProblemWorkflowArgs


@click.command()
@click.option("--year", required=True)
@click.option("--day", required=True)
async def main(
    year: int,
    day: int,
) -> None:
    # Need to get the path to the dir where solutions should be written. Implementing this to work
    # on various machines.
    aoc_solutions_dir = os.path.realpath(
        os.path.join(
            os.path.dirname(__file__),
            "../../advent_of_code",
            f"year{year}",
            f"day{day}",
        )
    )

    # Create a client.
    client = await get_temporal_client()

    # Start the workflow.
    result = await client.execute_workflow(
        SolveAoCProblemWorkflow.run,
        SolveAoCProblemWorkflowArgs(year=year, day=day, solutions_dir=aoc_solutions_dir),
        id=f"solve-aoc-problem-{year}-{day}",
        task_queue=settings.TEMPORAL_TASK_QUEUE_NAME,
    )

    click.echo(f"Final problem result: {result}")


if __name__ == "__main__":
    main()
