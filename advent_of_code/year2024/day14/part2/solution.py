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
    # Create a grid representation
    grid = defaultdict(int)
    for x, y in positions:
        grid[(x, y)] += 1
    
    # Define characteristics of a Christmas tree pattern:
    # 1. Should have a triangular shape
    # 2. Should have a trunk at the bottom
    # 3. Should be roughly symmetrical
    
    # Find the bounds of the pattern
    if not grid:
        return False
    
    positions_list = list(grid.keys())
    min_x = min(x for x, _ in positions_list)
    max_x = max(x for x, _ in positions_list)
    min_y = min(y for _, y in positions_list)
    max_y = max(y for _, y in positions_list)
    
    # Pattern should be roughly centered
    center_x = (min_x + max_x) // 2
    width_of_pattern = max_x - min_x
    height_of_pattern = max_y - min_y
    
    # Check for minimum size and rough proportions of a tree
    if width_of_pattern < 5 or height_of_pattern < 7:
        return False
    
    if width_of_pattern > height_of_pattern:
        return False
    
    # Check for trunk (should have 1-2 robots at bottom center)
    trunk_count = sum(1 for x, y in positions_list if abs(x - center_x) <= 1 and y >= max_y - 2)
    if trunk_count not in (1, 2):
        return False
    
    # Check for triangular shape (more robots at bottom than top)
    levels = defaultdict(int)
    for _, y in positions_list:
        levels[y] += 1
    
    sorted_levels = sorted(levels.items())
    if len(sorted_levels) < 4:
        return False
    
    # Top should have fewer robots than middle
    if levels[min_y] >= levels[(min_y + max_y) // 2]:
        return False
    
    return True


def find_earliest_christmas_tree(input_str: str) -> int:
    """Find the earliest time when robots form a Christmas tree pattern."""
    robots = parse_input(input_str)
    WIDTH = 101
    HEIGHT = 103
    
    # Search through time intervals
    for time in range(1, 1000):  # reasonable upper limit
        # Calculate positions at current time
        current_positions = []
        for pos, vel in robots:
            current_pos = calculate_position(pos, vel, time, WIDTH, HEIGHT)
            current_positions.append(current_pos)
        
        # Check if current positions form a Christmas tree
        if is_christmas_tree_pattern(current_positions, WIDTH, HEIGHT):
            return time
    
    return -1  # If no pattern found


def solution() -> int:
    """Read from stdin and return the result."""
    return find_earliest_christmas_tree(sys.stdin.read())

if __name__ == "__main__":
    print(solution())