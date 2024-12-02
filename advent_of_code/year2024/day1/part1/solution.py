"""Calculates the total distance between two lists of numbers."""
from typing import List


def parse_input(input_str: str) -> tuple[List[int], List[int]]:
    """Parse the input string into two lists of numbers."""
    left_nums = []
    right_nums = []
    
    # Split input into lines and process each line
    for line in input_str.strip().splitlines():
        # Split each line into two numbers
        left, right = line.split()
        left_nums.append(int(left))
        right_nums.append(int(right))
    
    return left_nums, right_nums


def calculate_total_distance(input_str: str) -> int:
    """
    Calculate total distance between left and right lists of numbers.
    
    Args:
        input_str: String containing pairs of numbers, one pair per line
                  separated by whitespace.
    
    Returns:
        Total distance calculated by summing absolute differences between
        sorted pairs of numbers.
    """
    # Parse input into two lists
    left_nums, right_nums = parse_input(input_str)
    
    # Sort both lists independently
    left_nums.sort()
    right_nums.sort()
    
    # Calculate total distance by summing absolute differences of paired numbers
    total_distance = 0
    for left, right in zip(left_nums, right_nums):
        total_distance += abs(left - right)
    
    return total_distance


def solution() -> int:
    """Read from stdin and return solution."""
    import sys
    return calculate_total_distance(sys.stdin.read())