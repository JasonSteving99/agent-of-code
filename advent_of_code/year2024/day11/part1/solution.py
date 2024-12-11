"""Solution for Plutonian Pebbles puzzle."""
from typing import List


def transform_number(num: int) -> List[int]:
    """Transform a single number according to the rules."""
    # Rule 1: If number is 0, return 1
    if num == 0:
        return [1]
    
    # Convert number to string to check digits
    num_str = str(num)
    
    # Rule 2: If number has even number of digits, split it
    if len(num_str) % 2 == 0:
        mid = len(num_str) // 2
        left = int(num_str[:mid])
        right = int(num_str[mid:])
        return [left, right]
    
    # Rule 3: Multiply by 2024
    return [num * 2024]


def blink(current_state: str) -> str:
    """Transform a space-separated string of integers according to blinking rules."""
    if not current_state:
        return ""
    
    # Split input into integers
    numbers = [int(x) for x in current_state.split()]
    
    # Transform each number and collect results
    new_numbers: List[int] = []
    for num in numbers:
        new_numbers.extend(transform_number(num))
    
    # Convert back to space-separated string
    return " ".join(str(x) for x in new_numbers)


def solution() -> int:
    """Read input and blink 25 times."""
    # Read initial state from stdin
    initial_state = input().strip()
    
    # Blink 25 times
    current_state = initial_state
    for _ in range(25):
        current_state = blink(current_state)
    
    # Return number of stones (number of space-separated values)
    return len(current_state.split())