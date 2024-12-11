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
            left = stone[:half].lstrip('0') or '0'
            right = stone[half:].lstrip('0') or '0'
            new_stones.extend([left, right])
        # Rule 3: Multiply by 2024
        else:
            new_stones.append(str(int(stone) * 2024))
    
    return ' '.join(new_stones)

def simulate_pebbles(initial_stones: str, num_blinks: int) -> str:
    """
    Simulate the evolution of stones for the given number of blinks and return 
    the number of stones as a string.
    """
    stones = initial_stones.strip()
    
    for _ in range(num_blinks):
        stones = blink(stones)
    
    return str(len(stones.split()))

def solution() -> int:
    """Read input from stdin and return the number of stones after 75 blinks."""
    initial_stones = sys.stdin.read().strip()
    
    result = simulate_pebbles(initial_stones, 75)
    return int(result)

if __name__ == "__main__":
    print(solution())