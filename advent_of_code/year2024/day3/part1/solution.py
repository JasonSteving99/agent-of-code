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
    # Pattern for valid mul operations: mul followed by 1-3 digits, comma, 1-3 digits in parentheses
    # No spaces allowed within the pattern to match problem requirements
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    total = 0
    # Find all matches in the corrupted memory
    for match in re.finditer(pattern, corrupted_memory):
        # Extract numbers from the matched groups
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        # Add their product to the total
        total += num1 * num2
        
    return total


def solution() -> int:
    """
    Read input from stdin and solve the puzzle.
    
    Returns:
        int: The sum of all valid multiplication results
    """
    # Read the entire input as a single string
    corrupted_memory = stdin.read().strip()
    return sum_valid_mul_operations(corrupted_memory)


if __name__ == "__main__":
    print(solution())