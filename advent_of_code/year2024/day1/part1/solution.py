"""Solution for calculating total distance between two sorted lists."""
from typing import List


def parse_input(input_str: str) -> tuple[List[int], List[int]]:
    """Parse input string into two lists of integers."""
    left_list = []
    right_list = []
    
    for line in input_str.strip().splitlines():
        # Split each line by whitespace and convert to integers
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
        
    return left_list, right_list


def calculate_total_distance(input_str: str) -> int:
    """
    Calculate the total distance between two lists of numbers.
    
    The function:
    1. Parses input into two lists
    2. Sorts both lists
    3. Calculates absolute difference between corresponding elements
    4. Returns sum of all differences
    
    Args:
        input_str: String containing pairs of numbers, one pair per line,
                  separated by whitespace
    
    Returns:
        Total distance (sum of absolute differences between paired elements)
    """
    # Parse input into two separate lists
    left_list, right_list = parse_input(input_str)
    
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate total distance by summing absolute differences
    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)
        
    return total_distance


def solution() -> int:
    """Read from stdin and return result."""
    import sys
    return calculate_total_distance(sys.stdin.read())