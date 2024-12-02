"""Solution to calculate total distance between two sorted lists of integers."""
from typing import List


def parse_input(input_str: str) -> tuple[List[int], List[int]]:
    """Parse input string into two lists of integers."""
    left_list = []
    right_list = []
    
    # Split input into lines and parse each line
    for line in input_str.strip().split('\n'):
        left, right = map(int, line.strip().split())
        left_list.append(left)
        right_list.append(right)
    
    return left_list, right_list


def calculate_total_distance(input_str: str) -> int:
    """
    Calculate the total distance between sorted left and right lists.
    
    Args:
        input_str: A string containing pairs of integers separated by spaces,
                  one pair per line.
    
    Returns:
        The sum of absolute differences between paired numbers after sorting.
    """
    # Parse input into two lists
    left_list, right_list = parse_input(input_str)
    
    # Sort both lists independently
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    # Calculate total distance by summing absolute differences
    total_distance = 0
    for left, right in zip(left_sorted, right_sorted):
        total_distance += abs(left - right)
    
    return total_distance


def solution() -> int:
    """Read from stdin and return the solution."""
    import sys
    input_data = sys.stdin.read()
    return calculate_total_distance(input_data)

if __name__ == "__main__":
    print(solution())