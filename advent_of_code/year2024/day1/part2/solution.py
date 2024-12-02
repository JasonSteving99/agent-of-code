"""
Solution for calculating distances between lists of numbers.
"""
from typing import List


def get_lists_from_input(data: str) -> tuple[List[int], List[int]]:
    """Parse input string into two lists of integers."""
    left, right = [], []
    for line in data.strip().splitlines():
        l, r = map(int, line.strip().split())
        left.append(l)
        right.append(r)
    return left, right


def calculate_total_distance(data: str) -> int:
    """
    Calculate the total distance between sorted left and right lists.
    
    Args:
        data: String input with pairs of numbers separated by whitespace
             Each line contains two integers.
             
    Returns:
        The sum of absolute differences between corresponding sorted numbers
    """
    # Parse input into two lists
    left, right = get_lists_from_input(data)
    
    # Sort both lists separately
    left = sorted(left)
    right = sorted(right)
    
    # Calculate sum of absolute differences between corresponding pairs
    total_distance = sum(abs(l - r) for l, r in zip(left, right))
    
    return total_distance


def solution() -> int:
    """Read from stdin and return the result."""
    import sys
    data = sys.stdin.read()
    return calculate_total_distance(data)