"""Solution to historian hysteria problem."""
from typing import List


def parse_input(input_data: str) -> tuple[List[int], List[int]]:
    """Parse the input string into two lists of integers."""
    left_nums = []
    right_nums = []
    
    for line in input_data.strip().split('\n'):
        left, right = [int(x) for x in line.strip().split()]
        left_nums.append(left)
        right_nums.append(right)
        
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
    # Parse input into two lists
    left_nums, right_nums = parse_input(input_data)
    
    # Sort both lists independently
    left_nums.sort()
    right_nums.sort()
    
    # Calculate distance between corresponding elements after sorting
    total_distance = sum(abs(left - right) for left, right in zip(left_nums, right_nums))
    
    return total_distance


def solution() -> int:
    """Read from stdin and return solution."""
    from sys import stdin
    return calculate_total_distance(stdin.read())