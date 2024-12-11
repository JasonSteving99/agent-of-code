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

def simulate_stone_evolution_part_2(initial_stones: str) -> str:
    """
    Simulates the evolution of stones for 75 blinks and returns the number of stones.
    
    Args:
        initial_stones: Space-separated string of initial stone numbers.
        
    Returns:
        String representation of the final number of stones.
    """
    stones = initial_stones
    
    # Apply 75 blinks (instead of 25 from Part 1)
    for _ in range(75):
        stones = blink(stones)
    
    # Return the number of stones as a string
    return str(len(stones.split()))

def solution() -> int:
    """Read input from stdin and return the number of stones after 75 blinks."""
    # Read initial stone arrangement from stdin
    initial_stones = sys.stdin.read().strip()
    
    # Apply 75 blinks and convert result to integer
    return int(simulate_stone_evolution_part_2(initial_stones))

if __name__ == "__main__":
    print(solution())