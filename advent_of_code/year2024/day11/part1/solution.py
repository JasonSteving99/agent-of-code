from typing import List
import sys

def blink(stones_str: str) -> str:
    """Transform a space-separated string of stone numbers according to the rules."""
    stones = list(map(str, stones_str.split()))
    new_stones: List[str] = []
    
    for stone in stones:
        # Rule 1: If stone is 0, replace with 1
        if stone == '0':
            new_stones.append('1')
        # Rule 2: If number has even number of digits, split in half
        elif len(stone) % 2 == 0:
            half = len(stone) // 2
            left = stone[:half].lstrip('0') or '0'  # Handle leading zeros but keep single '0'
            right = stone[half:].lstrip('0') or '0'
            new_stones.extend([left, right])
        # Rule 3: Multiply by 2024
        else:
            new_stones.append(str(int(stone) * 2024))
    
    return ' '.join(new_stones)

def solution() -> int:
    """Read input from stdin and return the number of stones after 25 blinks."""
    # Read initial stone arrangement from stdin
    initial_stones = sys.stdin.read().strip()
    
    # Apply 25 blinks
    stones = initial_stones
    for _ in range(25):
        stones = blink(stones)
    
    # Count the number of stones (number of space-separated values)
    return len(stones.split())

if __name__ == "__main__":
    print(solution())