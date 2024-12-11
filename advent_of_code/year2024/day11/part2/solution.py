from typing import List
import sys

def blink(stones: List[int]) -> List[int]:
    """Transform a list of stone numbers according to the rules."""
    new_stones: List[int] = []

    for stone in stones:
        # Rule 1: If stone is 0, replace with 1
        if stone == 0:
            new_stones.append(1)
        # Rule 2: If number has even number of digits, split in half
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            half = len(s) // 2
            left = int(s[:half])
            right = int(s[half:])
            new_stones.extend([left, right])
        # Rule 3: Multiply by 2024
        else:
            new_stones.append(stone * 2024)

    return new_stones

def simulate_stone_evolution_part_2(initial_stones_str: str) -> int:
    """
    Simulates the evolution of stones for 75 blinks and returns the number of stones.

    Args:
        initial_stones_str: Space-separated string of initial stone numbers.

    Returns:
        Integer representing the final number of stones.
    """
    initial_stones = list(map(int, initial_stones_str.split()))

    stones = initial_stones
    for _ in range(75):
        stones = blink(stones)

    return len(stones)

def solution() -> int:
    """Read input from stdin and return the number of stones after 75 blinks."""
    initial_stones_str = sys.stdin.read().strip()
    return simulate_stone_evolution_part_2(initial_stones_str)

if __name__ == "__main__":
    print(solution())