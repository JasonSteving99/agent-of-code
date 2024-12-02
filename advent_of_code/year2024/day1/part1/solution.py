"""Solution for calculating total distance between two lists."""
from typing import List, Tuple


def parse_input(input_str: str) -> List[Tuple[int, int]]:
    """Parse input string into list of integer pairs."""
    pairs = []
    if not input_str.strip():
        return pairs
    for line in input_str.strip().split('\n'):
        nums = line.split()
        if len(nums) != 2:
            raise ValueError("Each line must contain exactly two numbers.")
        left, right = map(int, nums)
        pairs.append((left, right))
    return pairs


def calculate_distance(pairs: List[Tuple[int, int]]) -> int:
    """Calculate total distance between pairs."""
    total_distance = 0
    for left, right in pairs:  # Iterate directly through the pairs
        total_distance += abs(left - right)
    return total_distance


def calculate_total_distance(input_data: str) -> int:
    """
    Calculate the total distance between two lists of numbers.
    Args:
        input_data: String containing pairs of numbers, one pair per line, separated by whitespace.
    Returns:
        The sum of absolute differences between corresponding numbers.
    Raises:
        ValueError: if input lines do not have exactly two numbers
    """
    pairs = parse_input(input_data)
    return calculate_distance(pairs)
