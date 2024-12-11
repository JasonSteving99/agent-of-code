"""
Solution for Plutonian Pebbles problem.
"""
from typing import List


def transform_stone(stone: str) -> List[str]:
    """Transform a single stone according to the rules."""
    num = int(stone)
    
    # Rule 1: If stone is 0, replace with 1
    if num == 0:
        return ["1"]
        
    # Rule 2: If number of digits is even, split in half
    if len(stone) % 2 == 0:
        mid = len(stone) // 2
        left = stone[:mid].lstrip('0')  # Remove leading zeros
        right = stone[mid:].lstrip('0')
        # Handle case where stripping zeros results in empty string
        return [left if left else "0", right if right else "0"]
        
    # Rule 3: Multiply by 2024
    return [str(num * 2024)]


def blink(stones_str: str) -> str:
    """Transform all stones in one blink."""
    # Split input into list of strings
    stones = stones_str.strip().split()
    
    # Transform each stone and collect results
    new_stones = []
    for stone in stones:
        new_stones.extend(transform_stone(stone))
        
    return " ".join(new_stones)


def solution() -> int:
    """
    Read initial stones from stdin and return the number of stones after 25 blinks.
    """
    # Read initial stones arrangement
    initial_stones = input().strip()
    
    # Perform 25 blinks
    current_stones = initial_stones
    for _ in range(25):
        current_stones = blink(current_stones)
        
    # Return number of stones in final arrangement
    return len(current_stones.split())