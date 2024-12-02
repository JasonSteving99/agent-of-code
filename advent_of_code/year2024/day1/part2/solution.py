from typing import List, Tuple
import sys


def parse_input(data: str) -> Tuple[List[int], List[int]]:
    """Parse input string into two lists of integers."""
    left, right = [], []
    for line in data.strip().splitlines():
        if not line:
            continue
        # Split line into two numbers, handling any amount of whitespace
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)
    return left, right


def calculate_distance(left: List[int], right: List[int]) -> int:
    """Calculate total distance between sorted lists."""
    # Sort both lists
    left_sorted = sorted(left)
    right_sorted = sorted(right)
    
    # Calculate sum of absolute differences
    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    return total_distance


def calculate_similarity_score(left: List[int], right: List[int]) -> int:
    """Calculate similarity score between lists."""
    # Count occurrences in right list
    right_counts = {}
    for num in right:
        right_counts[num] = right_counts.get(num, 0) + 1
    
    # Calculate total score
    total_score = sum(num * right_counts.get(num, 0) for num in left)
    return total_score


def calculate_total_distance(data: str) -> int:
    """Calculate total distance between two lists from input data."""
    # Part 1 implementation
    left, right = parse_input(data)
    return calculate_distance(left, right)


def solution() -> int:
    """Read from stdin and return the result."""
    input_data = sys.stdin.read()
    return calculate_total_distance(input_data)


if __name__ == "__main__":
    print(solution())