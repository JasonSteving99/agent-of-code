from typing import List

def calculate_similarity_score(input_data: str) -> int:
    # Parse the input data into left and right lists
    left_nums, right_nums = [], []
    for line in input_data.strip().split('\n'):
        left, right = map(int, line.split())
        left_nums.append(left)
        right_nums.append(right)

    # Calculate frequency of each number in right list 
    right_counts = {}
    for num in right_nums:
        right_counts[num] = right_counts.get(num, 0) + 1

    # Calculate similarity score
    similarity_score = 0
    for left_num in left_nums:
        # Get count of how many times left_num appears in right list (0 if never appears)
        count_in_right = right_counts.get(left_num, 0)
        # Add to similarity score: left_num * number of times it appears in right list
        similarity_score += left_num * count_in_right

    return similarity_score

def solution() -> int:
    # Read input from stdin
    import sys
    input_data = sys.stdin.read()
    return calculate_similarity_score(input_data)

if __name__ == "__main__":
    result = solution()
    print(result)