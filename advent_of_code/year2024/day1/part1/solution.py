"""Solution for calculating manhattan distance between two lists."""
from typing import List


def parse_input(input_str: str) -> tuple[List[int], List[int]]:
    """Parse input string into two separate lists of integers."""
    lines = input_str.strip().split('\n')
    left_list = []
    right_list = []
    
    for i, line in enumerate(lines):
        nums = [int(x) for x in line.strip().split()]
        if nums:
            if i % 2 == 0:
                left_list.append(nums[0])
            else:
                right_list.append(nums[0])
    
    return left_list, right_list


def calculate_manhattan_distance(input_str: str) -> int:
    """
    Calculate the total manhattan distance between two sorted lists.
    
    Args:
        input_str: String containing alternating numbers for left and right list
    
    Returns:
        The total manhattan distance between the paired numbers
    """
    # Parse input into two lists
    left_list, right_list = parse_input(input_str)
    
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate total distance
    total_distance = 0
    for left_num, right_num in zip(left_list, right_list):
        distance = abs(left_num - right_num)
        total_distance += distance
    
    return total_distance


def solution() -> int:
    """Read from stdin and return the solution."""
    import sys
    input_data = sys.stdin.read()
    return calculate_manhattan_distance(input_data)


if __name__ == "__main__":
    print(solution())