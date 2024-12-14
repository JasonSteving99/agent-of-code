"""Solution for finding earliest Christmas tree pattern in robot movement."""
from typing import List, Tuple, Dict
import sys
from collections import defaultdict


def parse_input(input_str: str) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """Parse input string into list of position and velocity tuples."""
    robots = []
    for line in input_str.strip().splitlines():
        pos, vel = line.split()
        px, py = map(int, pos[2:].split(','))
        vx, vy = map(int, vel[2:].split(','))
        robots.append(((px, py), (vx, vy)))
    return robots


def calculate_position(
    initial_pos: Tuple[int, int],
    velocity: Tuple[int, int],
    time: int,
    width: int,
    height: int
) -> Tuple[int, int]:
    """Calculate final position after given time with wrapping."""
    x, y = initial_pos
    vx, vy = velocity

    # Calculate new positions and apply modulo
    final_x = (x + vx * time) % width
    final_y = (y + vy * time) % height

    return (final_x, final_y)


def is_christmas_tree_pattern(positions: List[Tuple[int, int]], width: int, height: int) -> bool:
    """Check if robots form a Christmas tree pattern."""
    if not positions:
        return False

    levels = defaultdict(list)
    for x, y in positions:
        levels[y].append(x)

    # Find center level (smallest x-range)
    min_range = float('inf')
    center_level = -1
    for y, x_coords in levels.items():
        if x_coords:
            current_range = max(x_coords) - min(x_coords)
            if current_range < min_range:
                min_range = current_range
                center_level = y

    if center_level == -1:
        return False

    # Check for general increase in range as we move away from center
    for y, x_coords in levels.items():
        if x_coords:
            if abs(y-center_level) > 2 and max(x_coords) - min(x_coords) < min_range + 3: # Tolerance added
                return False
    return True

def find_earliest_christmas_tree(input_str: str) -> int:
    """Find the earliest time when robots form a Christmas tree pattern."""
    robots = parse_input(input_str)
    WIDTH = 101
    HEIGHT = 103

    for time in range(1, 1000):
        current_positions = []
        for pos, vel in robots:
            current_pos = calculate_position(pos, vel, time, WIDTH, HEIGHT)
            current_positions.append(current_pos)

        if is_christmas_tree_pattern(current_positions, WIDTH, HEIGHT):
            return time

    return -1


def solution() -> int:
    """Read from stdin and return the result."""
    return find_earliest_christmas_tree(sys.stdin.read())

if __name__ == "__main__":
    print(solution())
