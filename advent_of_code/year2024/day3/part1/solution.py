"""Solution for parsing corrupted memory and summing valid mul operations."""

import re
from typing import Match
from sys import stdin


def sum_valid_mul_operations(corrupted_memory: str) -> int:
    """
    Parse corrupted memory and sum results of all valid mul operations.
    
    Args:
        corrupted_memory (str): The corrupted memory string containing mul operations
        
    Returns:
        int: Sum of all valid multiplication results
    """
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    total = 0
    matches = re.findall(pattern, corrupted_memory)
    for match in matches:
        num1, num2 = map(int, match)  # Convert matched strings to integers
        total += num1 * num2
    return total


def solution() -> int:
    """
    Read input from stdin and solve the puzzle.
    
    Returns:
        int: The sum of all valid multiplication results
    """
    corrupted_memory = stdin.read().strip()
    return sum_valid_mul_operations(corrupted_memory)


if __name__ == "__main__":
    print(solution())
