"""Solution for finding when robots form a Christmas tree pattern."""
from typing import List, Tuple, Dict, Set
import sys


def parse_input(input_str: str) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """Parse input string into list of position and velocity tuples."""
    robots = []
    for line in input_str.strip().split('\n'):
        pos, vel = line.split()
        px, py = map(int, pos.replace('p=', '').split(','))
        vx, vy = map(int, vel.replace('v=', '').split(','))
        robots.append(((px, py), (vx, vy)))
    return robots


def update_position(pos: Tuple[int, int], vel: Tuple[int, int], width: int, height: int) -> Tuple[int, int]:
    """Update position considering teleportation at boundaries."""
    x, y = pos[0] + vel[0], pos[1] + vel[1]
    x = x % width  # Wrap around horizontally
    y = y % height  # Wrap around vertically
    return (x, y)


def get_positions_at_time(robots: List[Tuple[Tuple[int, int], Tuple[int, int]]], 
                         width: int, height: int, seconds: int) -> Set[Tuple[int, int]]:
    """Get set of positions where robots are at a given time."""
    positions = set()
    
    for pos, vel in robots:
        curr_pos = pos
        for _ in range(seconds):
            curr_pos = update_position(curr_pos, vel, width, height)
        positions.add(curr_pos)
        
    return positions


def looks_like_tree(positions: Set[Tuple[int, int]], width: int, height: int) -> bool:
    """Check if the robot positions form a Christmas tree pattern."""
    # Convert positions to a grid for pattern analysis
    grid = [[0] * width for _ in range(height)]
    for x, y in positions:
        grid[y][x] = 1
    
    # Find the bounding box of the pattern
    min_x, max_x, min_y, max_y = width, 0, height, 0
    for y in range(height):
        for x in range(width):
            if grid[y][x]:
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)
    
    if max_y - min_y < 5 or max_x - min_x < 3:
        return False  # Too small to be a tree
    
    # Calculate pattern density in triangular shape
    tree_height = max_y - min_y + 1
    tree_base = max_x - min_x + 1
    
    # Check if the overall shape is triangular
    points_in_triangle = 0
    total_points = len(positions)
    
    for y in range(min_y, max_y + 1):
        y_ratio = (y - min_y) / tree_height
        # Expected width at this height
        expected_width = tree_base * (1 - y_ratio)
        points_in_row = sum(1 for x in range(min_x, max_x + 1) if (x, y) in positions)
        
        if points_in_row > expected_width * 1.5:
            return False
        
        if points_in_row > 0:
            points_in_triangle += points_in_row
    
    # Check if most points form a triangular shape
    return points_in_triangle >= total_points * 0.8


def find_christmas_tree_time(input_str: str) -> int:
    """Find the earliest time when robots form a Christmas tree pattern."""
    robots = parse_input(input_str)
    width, height = 101, 103
    
    # Search for the pattern in reasonable time window
    for seconds in range(200):  # Increased the range to 200
        positions = get_positions_at_time(robots, width, height, seconds)
        if looks_like_tree(positions, width, height):
            return seconds
    
    return -1  # Pattern not found


def solution() -> int:
    """Read from stdin and return the solution."""
    input_data = sys.stdin.read()
    return find_christmas_tree_time(input_data)


if __name__ == "__main__":
    print(solution())
