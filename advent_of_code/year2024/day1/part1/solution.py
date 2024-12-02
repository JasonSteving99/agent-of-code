"""Solution for calculating total distance between two lists."""
from typing import List, Tuple


def get_lists_from_input(input_str: str) -> Tuple[List[int], List[int]]:
    """Parse input string into two lists of integers."""
    left_list = []
    right_list = []
    
    for line in input_str.strip().split('\n'):
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))
    
    return left_list, right_list


def calculate_total_distance(input_str: str) -> int:
    """
    Calculate the total distance between two lists of numbers.
    
    Distance is defined as the sum of absolute differences between corresponding elements
    when both lists are sorted.
    
    Args:
        input_str: String containing two lists of integers separated by spaces and newlines
        
    Returns:
        Total distance between the lists
    """
    # Parse input into two lists
    left_list, right_list = get_lists_from_input(input_str)
    
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    # Calculate total distance by summing absolute differences between corresponding elements
    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    
    return total_distance


def solution() -> int:
    """Read input from stdin and return the solution."""
    import sys
    input_data = sys.stdin.read()
    return calculate_total_distance(input_data)


if __name__ == "__main__":
    print(solution())