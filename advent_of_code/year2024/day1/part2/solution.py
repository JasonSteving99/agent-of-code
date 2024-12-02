"""Solution for calculating total distance between two lists."""
from typing import List


def parse_input(input_str: str) -> tuple[List[int], List[int]]:
    """Parse the input string into two lists of integers."""
    left_list = []
    right_list = []
    
    # Split input into lines and parse each line
    for line in input_str.strip().split('\n'):
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    
    return left_list, right_list


def calculate_total_distance(input_str: str) -> int:
    """
    Calculate the total distance between two lists after sorting.
    
    Args:
        input_str: String containing pairs of numbers separated by whitespace,
                  one pair per line.
    
    Returns:
        Total distance (sum of absolute differences) between the sorted lists.
    """
    # Parse input into two lists
    left_list, right_list = parse_input(input_str)
    
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate total distance by summing absolute differences
    total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))
    
    return total_distance


def solution() -> int:
    """Read from stdin and return the solution."""
    import sys
    return calculate_total_distance(sys.stdin.read())