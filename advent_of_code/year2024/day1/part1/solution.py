"""Solution for calculating total distance between two lists."""
from typing import List


def parse_input(input_str: str) -> tuple[List[int], List[int]]:
    """Parse the input string into two separate lists."""
    left_list = []
    right_list = []

    for line in input_str.strip().splitlines():
        left, right = map(int, line.split(maxsplit=1))
        left_list.append(left)
        right_list.append(right)

    return left_list, right_list


def calculate_total_distance(input_str: str) -> int:
    """Calculate the total distance between two lists of numbers.
    
    Args:
        input_str: A string containing pairs of numbers, one pair per line,
                  separated by whitespace.
    
    Returns:
        The sum of absolute differences between paired numbers after sorting
        each list independently.
    """
    # Parse the input into two separate lists
    left_list, right_list = parse_input(input_str)
    
    # Sort both lists independently
    left_list.sort()
    right_list.sort()
    
    # Calculate total distance by summing absolute differences of paired numbers
    total_distance = sum(abs(left - right) 
                        for left, right in zip(left_list, right_list))
    
    return total_distance


def solution() -> int:
    """Read from stdin and return the solution."""
    import sys
    input_data = sys.stdin.read()
    return calculate_total_distance(input_data)


if __name__ == "__main__":
    print(solution())