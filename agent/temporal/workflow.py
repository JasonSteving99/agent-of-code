from datetime import timedelta

from temporalio import workflow
from temporalio.common import RetryPolicy

# Imports passed through Temporal's sandbox without overriding stdlib.
with workflow.unsafe.imports_passed_through():
    from agent.adventofcode.contextualize_examples import ExamplesContext
    from agent.temporal.activities import (
        AoCProblem,
        extract_examples,
        extract_problem_part,
        get_examples_context,
    )


@workflow.defn
class SolveAoCProblemWorkflow:
    @workflow.run
    async def run(self, solve_aoc_problem_req: AoCProblem) -> ExamplesContext:
        workflow.logger.info(
            f"Running SolveAoCProblemWorkflow with parameter {solve_aoc_problem_req}"
        )
        problem_part = await workflow.execute_activity(
            extract_problem_part,
            solve_aoc_problem_req,
            start_to_close_timeout=timedelta(seconds=15),
            retry_policy=RetryPolicy(
                maximum_attempts=5,
                # Try being a good citizen and don't spam retries to AoC's servers.
                initial_interval=timedelta(seconds=5),
                maximum_interval=timedelta(seconds=30),
            ),
        )

        extracted_examples = await workflow.execute_activity(
            extract_examples,
            problem_part,
            start_to_close_timeout=timedelta(seconds=20),
            retry_policy=RetryPolicy(maximum_attempts=5),
        )

        return await workflow.execute_activity(
            get_examples_context,
            args=[problem_part, extracted_examples],
            start_to_close_timeout=timedelta(seconds=20),
            retry_policy=RetryPolicy(maximum_attempts=5),
        )
