"""Solution for parsing corrupted memory and summing valid mul operations."""

import re
from typing import Match
from sys import stdin


def sum_valid_mul_operations(corrupted_memory: str) -> int:
    """
    Parses corrupted memory and sums the result of valid "mul" operations.

    Args:
        corrupted_memory: The input string containing potentially corrupted memory.

    Returns:
        The sum of the results of valid "mul" operations.
    """
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    total = 0

    for match in re.finditer(pattern, corrupted_memory):
        num1, num2 = map(int, match.groups())
        total += num1 * num2

    return total


def solution() -> int:
    """Reads input from stdin and solves the puzzle."""
    corrupted_memory = stdin.read().strip()
    return sum_valid_mul_operations(corrupted_memory)


if __name__ == "__main__":
    print(solution())
