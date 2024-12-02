"""
Solution to calculate total manhattan distance between pairs of sorted location IDs.
"""
from typing import List


def parse_input(input_str: str) -> tuple[List[int], List[int]]:
    """Parse input string into two lists of integers."""
    left_list = []
    right_list = []
    
    for line in input_str.strip().splitlines():
        # Split each line into two numbers
        left, right = line.strip().split()
        left_list.append(int(left))
        right_list.append(int(right))
        
    return left_list, right_list


def calculate_total_distance(input_str: str) -> int:
    """
    Calculate the total distance between two lists of location IDs.
    
    Args:
        input_str (str): Input string containing pairs of location IDs
        
    Returns:
        int: Total distance between the paired location IDs
    """
    # Parse input into two lists
    left_list, right_list = parse_input(input_str)
    
    # Sort both lists independently
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    # Calculate total distance by summing absolute differences
    total_distance = 0
    for left, right in zip(left_sorted, right_sorted):
        distance = abs(left - right)
        total_distance += distance
        
    return total_distance


def solution() -> int:
    """Read from stdin and return solution."""
    import sys
    input_data = sys.stdin.read()
    return calculate_total_distance(input_data)

if __name__ == "__main__":
    print(solution())