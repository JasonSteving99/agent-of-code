"""
Module containing solution for part 2 of the problem.
Calculate similarity score between two lists based on occurrence counts.
"""
from typing import List


def parse_input(input_str: str) -> tuple[List[int], List[int]]:
    """Parse input string into two lists of integers."""
    left_list = []
    right_list = []
    
    for line in input_str.strip().splitlines():
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
        
    return left_list, right_list


def count_occurrences(numbers: List[int]) -> dict[int, int]:
    """Count occurrences of each number in the list."""
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    return counts


def calculate_similarity_score(input_str: str) -> int:
    """
    Calculate similarity score between two lists.
    
    The similarity score is calculated by taking each number in the left list
    and multiplying it by the number of times it appears in the right list,
    then summing all these products.
    
    Args:
        input_str: String containing pairs of numbers representing the left and right lists.
                  Each pair is space-separated, and pairs are newline-separated.
    
    Returns:
        The total similarity score.
    """
    # Parse input into two lists
    left_list, right_list = parse_input(input_str)
    
    # Count occurrences of numbers in the right list
    right_counts = count_occurrences(right_list)
    
    # Calculate similarity score
    similarity_score = 0
    for num in left_list:
        # Multiply each number by its occurrence count in the right list (0 if not present)
        similarity_score += num * right_counts.get(num, 0)
    
    return similarity_score