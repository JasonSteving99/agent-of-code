"""Solution for part 2 of the problem."""
from collections import Counter
from typing import List

def parse_input(input_str: str) -> List[List[int]]:
    """Parse input string into two lists of integers."""
    left, right = [], []
    for line in input_str.strip().splitlines():
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)
    return [left, right]

def calculate_similarity_score(input_data: str) -> int:
    """
    Calculate similarity score between two lists of integers.
    The similarity score is calculated by:
    1. Taking each number from the left list
    2. Multiplying it by the number of times it appears in the right list
    3. Summing all these products
    
    Args:
        input_data: String containing pairs of numbers separated by whitespace,
                   one pair per line
    
    Returns:
        The similarity score as defined above
    """
    # Parse input into two lists
    left_list, right_list = parse_input(input_data)
    
    # Count occurrences in right list
    right_counter = Counter(right_list)
    
    # Calculate similarity score
    total_score = 0
    for num in left_list:
        # Multiply each number by its frequency in right list
        total_score += num * right_counter[num]
        
    return total_score

def solution() -> int:
    """Read from stdin and return the solution."""
    import sys
    return calculate_similarity_score(sys.stdin.read())