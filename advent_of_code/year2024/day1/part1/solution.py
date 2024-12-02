"""Solution to the historian hysteria puzzle."""
from typing import List


def parse_input(data: str) -> tuple[List[int], List[int]]:
    """Parse input string into two lists of integers."""
    left_list: List[int] = []
    right_list: List[int] = []
    
    for line in data.strip().splitlines():
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))
        
    return left_list, right_list


def calculate_distance(left_list: List[int], right_list: List[int]) -> int:
    """Calculate total distance between sorted lists."""
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    total_distance = 0
    
    # Calculate distance between corresponding elements
    for left, right in zip(left_sorted, right_sorted):
        total_distance += abs(left - right)
        
    return total_distance


def calculate_total_distance(input_data: str) -> int:
    """
    Calculate the total distance between two lists of location IDs.
    
    Args:
        input_data: String containing pairs of numbers, one pair per line
        
    Returns:
        Total distance between the matched pairs after sorting
    """
    # Parse input into two lists
    left_list, right_list = parse_input(input_data)
    
    # Calculate and return total distance
    return calculate_distance(left_list, right_list)


def solution() -> int:
    """Read from stdin and solve the problem."""
    import sys
    return calculate_total_distance(sys.stdin.read())

if __name__ == "__main__":
    print(solution())