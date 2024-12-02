from typing import List
import sys


def parse_input(input_str: str) -> tuple[List[int], List[int]]:
    """Parse the input string into two lists of integers."""
    left_list = []
    right_list = []
    
    for line in input_str.strip().splitlines():
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
        
    return left_list, right_list


def calculate_distance(list1: List[int], list2: List[int]) -> int:
    """Calculate the total distance between two sorted lists."""
    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length")
    
    # Sort both lists
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    
    # Calculate total distance
    total_distance = 0
    for n1, n2 in zip(sorted_list1, sorted_list2):
        total_distance += abs(n1 - n2)
        
    return total_distance


def calculate_total_distance(input_str: str) -> int:
    """
    Calculate the total distance between two lists of numbers from input string.
    
    Args:
        input_str: String containing pairs of numbers separated by spaces,
                  one pair per line
    
    Returns:
        Total distance between the sorted lists
    """
    # Parse input into two lists
    left_list, right_list = parse_input(input_str)
    
    # Calculate and return total distance
    return calculate_distance(left_list, right_list)


def solution() -> int:
    """Read from stdin and return the solution."""
    input_data = sys.stdin.read()
    return calculate_total_distance(input_data)


if __name__ == "__main__":
    print(solution())