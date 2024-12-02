"""Solution for calculating total distance between two lists."""
from typing import List, Tuple


def parse_input(input_str: str) -> List[Tuple[int, int]]:
    """Parse input string into list of integer pairs."""
    pairs = []
    for line in input_str.strip().split('\n'):
        left, right = map(int, line.split())
        pairs.append((left, right))
    return pairs


def calculate_distance(pairs: List[Tuple[int, int]]) -> int:
    """Calculate total distance between sorted pairs."""
    # Sort both lists separately and calculate distance between corresponding elements
    left_nums = sorted(x[0] for x in pairs)
    right_nums = sorted(x[1] for x in pairs)
    
    total_distance = 0
    for left, right in zip(left_nums, right_nums):
        total_distance += abs(left - right)
    
    return total_distance


def calculate_total_distance(input_data: str) -> int:
    """
    Calculate the total distance between two lists of numbers.
    
    Args:
        input_data: String containing pairs of numbers, one pair per line
                   separated by whitespace.
    
    Returns:
        The sum of absolute differences between corresponding numbers
        when both lists are sorted.
    """
    # Parse input into pairs of numbers
    pairs = parse_input(input_data)
    
    # Calculate and return total distance
    return calculate_distance(pairs)