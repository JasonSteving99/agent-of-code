"""Solution for calculating total distance between two lists."""
from typing import List


def parse_input(input_str: str) -> tuple[List[int], List[int]]:
    """Parse the input string into two lists of integers."""
    left_list = []
    right_list = []
    
    # Split input into lines and process each line
    for line in input_str.strip().split('\n'):
        # Split line into two numbers
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    
    return left_list, right_list


def calculate_total_distance(input_str: str) -> int:
    """
    Calculate the total distance between two lists of numbers.
    
    The distance is calculated by:
    1. Sorting both lists
    2. Pairing numbers from the same positions
    3. Calculating absolute difference between pairs
    4. Summing up all differences
    
    Args:
        input_str: String containing pairs of numbers, one pair per line
                  separated by whitespace
    
    Returns:
        Total distance between the two lists
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
    input_data = sys.stdin.read()
    return calculate_total_distance(input_data)


if __name__ == "__main__":
    print(solution())