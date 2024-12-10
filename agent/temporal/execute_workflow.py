import os

import asyncclick as click

from agent import settings
from agent.temporal.client import get_temporal_client
from agent.temporal.workflow import (
    GenerateCelebratoryImageWorkflow,
    GenerateCelebratoryImageWorkflowArgs,
    SolveAoCProblemWorkflow,
    SolveAoCProblemWorkflowArgs,
)


@click.command()
@click.option("--year", required=True)
@click.option("--day", required=True)
@click.option("--dry-run", default=False, is_flag=True)
async def main(
    year: int,
    day: int,
    dry_run: bool,
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
        SolveAoCProblemWorkflowArgs(
            year=year, day=day, solutions_dir=aoc_solutions_dir, dry_run=dry_run
        ),
        id=f"solve-aoc-problem-{year}-{day}",
        task_queue=settings.TEMPORAL_TASK_QUEUE_NAME,
    )

    # Generate a celebratory image to remember the problem by!
    if result.celebratory_image_generation_context:
        await client.execute_workflow(
            GenerateCelebratoryImageWorkflow.generate_problem_story_image,
            GenerateCelebratoryImageWorkflowArgs(
                problem_req=result.celebratory_image_generation_context.problem_req,
                problem_part=result.celebratory_image_generation_context.problem_part,
                solutions_dir=aoc_solutions_dir,
                dry_run=dry_run,
            ),
            id=f"generate-celebratory-image-{year}-{day}",
            task_queue=settings.TEMPORAL_TASK_QUEUE_NAME,
        )

    click.echo(f"Final problem result: {result}")


if __name__ == "__main__":
    main()
