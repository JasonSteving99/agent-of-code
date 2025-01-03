import logging

import asyncclick as click
from temporalio.worker import Worker

from agent import settings
from agent.llm.gemini.configure_genai import configure_genai
from agent.temporal import activities
from agent.temporal.client import get_temporal_client
from agent.temporal.workflow import GenerateCelebratoryImageWorkflow, SolveAoCProblemWorkflow


@click.command()
async def main() -> None:
    # Just for the sake of this demo worker, let's see info logs.
    logging.basicConfig(level=logging.INFO)

    # Configuring this here ensures all activities in this worker are automatically configured.
    configure_genai()

    # Create a worker for the workflow
    worker = Worker(
        await get_temporal_client(),
        # TODO(steving) Generalize this to enable running locally or against prod Temporal Cloud.
        task_queue=settings.TEMPORAL_TASK_QUEUE_NAME,
        workflows=[SolveAoCProblemWorkflow, GenerateCelebratoryImageWorkflow],
        activities=[
            activities.configure_llm_usage_logging_for_workflow,
            activities.extract_problem_part,
            activities.extract_examples,
            activities.get_examples_context,
            activities.get_generated_unit_tests,
            activities.get_generated_implementation,
            activities.commit_changes,
            activities.run_generated_tests,
            activities.run_generated_solution,
            activities.debug_unit_test_failures,
            activities.plan_impl_refactoring,
            activities.submit_solution,
            activities.extract_story_summary,
            activities.meta_get_image_generation_prompt,
            activities.generate_celebratory_image,
        ],
    )

    # Run the worker indefinitely, so that it polls for tasks.
    await worker.run()


if __name__ == "__main__":
    main()
