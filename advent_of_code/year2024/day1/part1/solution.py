"""Solution to historian hysteria problem."""
from typing import List


def parse_input(input_data: str) -> tuple[List[int], List[int]]:
    """Parse the input string into two lists of integers."""
    left_nums = []
    right_nums = []

    for line in input_data.strip().split('\n'):
        parts = line.split()
        if len(parts) >= 2:
            try:
                left = int(parts[0])
                right = int(parts[-1])
                left_nums.append(left)
                right_nums.append(right)
            except ValueError:
                pass  # Handle potential errors if non-numeric values are present

    return left_nums, right_nums


def calculate_total_distance(input_data: str) -> int:
    """
    Calculate the total distance between sorted left and right lists.

    Args:
        input_data: String containing pairs of numbers, one pair per line.
                   Each line has a left number and right number separated by whitespace.

    Returns:
        The total distance between the sorted left and right lists.
    """
    left_nums, right_nums = parse_input(input_data)

    left_nums.sort()
    right_nums.sort()

    total_distance = sum(abs(left - right) for left, right in zip(left_nums, right_nums))

    return total_distance


def solution() -> int:
    """Read from stdin and return solution."""
    from sys import stdin
    return calculate_total_distance(stdin.read())