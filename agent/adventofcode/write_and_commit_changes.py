import os
import subprocess

from pydantic import BaseModel

from agent.adventofcode import AoCProblem


class FileToCommit(BaseModel):
    filename: str
    content: str


def write_and_commit_changes(
    basedir: str,
    files: list[FileToCommit],
    aoc_problem: AoCProblem,
    commit_message: str,
    dry_run: bool,
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
    if not dry_run:
        subprocess.run(["git", "add", basedir], check=True)
        subprocess.run(["git", "commit", "-m", agent_commit_message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
