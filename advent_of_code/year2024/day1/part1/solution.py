"""Solution for calculating total distance between lists of location IDs."""
from io import StringIO


def calculate_total_distance(input_str: str) -> int:
    # Parse input and split into left and right lists
    left_list = []
    right_list = []
    
    # Using StringIO to simulate file input reading
    with StringIO(input_str) as f:
        for line in f:
            # Skip empty lines
            if not line.strip():
                continue
            # Split line and convert to integers
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)
    
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate total distance
    total_distance = 0
    for left, right in zip(left_list, right_list):
        distance = abs(left - right)
        total_distance += distance
    
    return total_distance


def solution() -> int:
    """Read from stdin and return the solution.
    
    Returns:
        int: Total distance between the two lists of location IDs.
    """
    import sys
    input_data = sys.stdin.read()
    return calculate_total_distance(input_data)

if __name__ == "__main__":
    result = solution()
    print(result)  # only for testing