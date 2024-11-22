import os

from pydantic import BaseModel

from agent.adventofcode import AoCProblem


class FileToCommit(BaseModel):
    filename: str
    content: str


def write_and_commit_changes(
    basedir: str, files: list[FileToCommit], aoc_problem: AoCProblem, commit_message: str
) -> None:
    # Make the dir if it doesn't already exist.
    os.makedirs(basedir, exist_ok=True)
    for to_commit in files:
        with open(os.path.join(basedir, to_commit.filename), "w") as f:
            f.write(to_commit.content)

    # TODO(steving) Commit and push the changes to git.
    agent_commit_message = (
        f"Coding-Agent ({aoc_problem.year}.{aoc_problem.day}.{aoc_problem.part}): {commit_message}"
    )
    print(agent_commit_message)
