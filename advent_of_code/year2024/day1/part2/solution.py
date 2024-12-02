from typing import List
import sys

def parse_input(raw_input: str) -> tuple[List[int], List[int]]:
    """Parse the input into two lists of integers."""
    left_nums = []
    right_nums = []
    
    # Split input into lines and process each line
    for line in raw_input.strip().split('\n'):
        # Split line by whitespace and convert to integers
        left, right = map(int, line.split())
        left_nums.append(left)
        right_nums.append(right)
        
    return left_nums, right_nums

def calculate_similarity_score(raw_input: str) -> int:
    """
    Calculate the similarity score between two lists of numbers.
    
    For each number in the left list, multiply it by the number of times it appears
    in the right list and add to the total score.
    
    Args:
        raw_input: String containing pairs of numbers separated by whitespace,
                  one pair per line
    
    Returns:
        The total similarity score
    """
    # Parse input into two lists
    left_nums, right_nums = parse_input(raw_input)
    
    # Count occurrences of each number in right list
    right_counts = {}
    for num in right_nums:
        right_counts[num] = right_counts.get(num, 0) + 1
    
    # Calculate similarity score
    total_score = 0
    for left_num in left_nums:
        # Multiply each left number by how many times it appears in right list
        appearances = right_counts.get(left_num, 0)
        total_score += left_num * appearances
            
    return total_score

def solution() -> int:
    """Read from stdin and return solution."""
    return calculate_similarity_score(sys.stdin.read())

if __name__ == "__main__":
    print(solution())