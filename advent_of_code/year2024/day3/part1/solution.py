"""
Solution for finding valid multiplication instructions and summing results.
"""
import re
from sys import stdin
from typing import List, Tuple


def extract_valid_mul_operations(line: str) -> List[Tuple[int, int]]:
    """Extract all valid mul(x,y) operations from a corrupted line."""
    # Match mul(X,Y) where X and Y are 1-3 digit numbers, ensuring isolation
    pattern = r'(?<![a-zA-Z\(])mul\((\d{1,3}),(\d{1,3})\)(?![a-zA-Z0-9])'
    matches = re.finditer(pattern, line)

    operations = []
    for match in matches:
        x, y = int(match.group(1)), int(match.group(2))
        operations.append((x, y))

    return operations


def sum_valid_mul_operations(line: str) -> int:
    """
    Calculate the sum of all valid multiplication operations in the line.

    Args:
        line: String containing corrupted memory with mul instructions

    Returns:
        Sum of the results of all valid multiplication operations
    """
    operations = extract_valid_mul_operations(line)
    return sum(x * y for x, y in operations)


def solution() -> int:
    """
    Read input from stdin and return the sum of all valid multiplication operations.

    Returns:
        Total sum of all valid multiplication results
    """
    content = ''.join(line for line in stdin)
    return sum_valid_mul_operations(content)