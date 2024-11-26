import io
import json
import subprocess
import sys
from importlib import import_module
from typing import Literal, cast

import asyncclick as click
import pytest
from pydantic import BaseModel
from pytest_jsonreport.plugin import JSONReport
from result import Err, Ok, Result

from agent.adventofcode.problem_part import ProblemPart


@click.group()
def cli_group():
    pass


def execute_generated_solution(
    year: int, day: int, part: ProblemPart
) -> Result[str, subprocess.CalledProcessError]:
    """Execute the solution in a subprocess so that this process can make programmatic edits to the
    tests/implementations according to the agent's fixes and have the changes reflected in
    subsequent test runs."""
    result = subprocess.run(
        [
            "python",
            "-m",
            "agent.adventofcode.execute_generated_code",
            "execute-problem-solution",
            f"--year={year}",
            f"--day={day}",
            f"--part={part}",
        ],
        capture_output=True,
        text=True,
    )
    try:
        return Ok(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        return Err(e)


@cli_group.command()
@click.option("--year", required=True)
@click.option("--day", required=True)
@click.option("--part", type=click.Choice(["1", "2"]), default="1")
def execute_problem_solution(
    year: int,
    day: int,
    part: str,  # type: ignore - Need to redeclare with a cast after parsing into an int.
) -> None:
    part: ProblemPart = cast(ProblemPart, part)

    with open(f"advent_of_code/year{year}/day{day}/part{part}/input.txt") as f:
        # Patch stdin to return the contents of the input file without needing to actually have the
        # file contents piped into the program from the cli.
        sys.stdin = io.StringIO(f.read())

    solution_module = import_module(f"advent_of_code.year{year}.day{day}.part{part}.solution")

    # Execute the actual implementation!
    print(str(solution_module.solution()))


class TestResults(BaseModel):
    class Success(BaseModel):
        passed: Literal[True] = True

    class Failure(BaseModel):
        err_msg: str

    result: Success | Failure


def execute_tests(year: int, day: int, part: ProblemPart) -> TestResults:
    """Execute the tests in a subprocess so that this process can make programmatic edits to the
    tests/implementations according to the agent's fixes and have the changes reflected in
    subsequent test runs."""
    result = subprocess.run(
        [
            "python",
            "-m",
            "agent.adventofcode.execute_generated_code",
            "get-test-report",
            f"--year={year}",
            f"--day={day}",
            f"--part={part}",
        ],
        capture_output=True,
        text=True,
    )
    report_json = json.loads(result.stdout)

    if report_json["exitcode"] == 0:
        return TestResults(result=TestResults.Success())
    else:
        test_file = f"advent_of_code/year{year}/day{day}/part{part}/tests.py"
        return TestResults(
            result=TestResults.Failure(
                err_msg=next(
                    x["longrepr"] for x in report_json["collectors"] if x["nodeid"] == test_file
                )
            )
        )


@cli_group.command()
@click.option("--year", required=True)
@click.option("--day", required=True)
@click.option("--part", type=click.Choice(["1", "2"]), default="1")
def get_test_report(
    year: int,
    day: int,
    part: str,  # type: ignore - Need to redeclare with a cast after parsing into an int.
) -> None:
    part: ProblemPart = cast(ProblemPart, part)

    # I need to prevent Pytest from writing useless logs to stdout, I literally just want the JSON
    # report from the plugin.
    orig_stdout = sys.stdout
    sys.stdout = io.StringIO()  # Throw away any output.

    plugin = JSONReport()
    pytest.main(
        [
            "--quiet",
            "--json-report-file=none",
            f"advent_of_code/year{year}/day{day}/part{part}/tests.py",
        ],
        plugins=[plugin],
    )

    sys.stdout = orig_stdout  # Return to writing to stdout.
    print(json.dumps(plugin.report, indent=4))


if __name__ == "__main__":
    cli_group()
