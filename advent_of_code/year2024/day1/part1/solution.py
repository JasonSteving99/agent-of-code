"""Solution for calculating distance between lists."""
from typing import List

def parse_input(input_data: str) -> List[tuple[int, int]]:
    """Parse input string into list of integer pairs."""
    lines = input_data.strip().split('\n')
    pairs = []
    for line in lines:
        left, right = line.split()
        pairs.append((int(left), int(right)))
    return pairs

def calculate_total_distance(input_data: str) -> int:
    """
    Calculate total distance between two lists of location IDs.
    
    Args:
        input_data (str): String containing pairs of numbers, one pair per line
        
    Returns:
        int: Total distance between sorted lists
    """
    # Parse input into pairs
    pairs = parse_input(input_data)
    
    # Separate into left and right lists
    left_list = []
    right_list = []
    for left, right in pairs:
        left_list.append(left)
        right_list.append(right)
    
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate total distance
    total_distance = 0
    for i in range(len(left_list)):
        distance = abs(left_list[i] - right_list[i])
        total_distance += distance
        
    return total_distance

def solution() -> int:
    """Read input from stdin and solve the problem."""
    import sys
    input_data = sys.stdin.read()
    return calculate_total_distance(input_data)

if __name__ == "__main__":
    print(solution())