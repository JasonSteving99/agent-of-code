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
    if not positions:
        return False

    min_x, max_x, min_y, max_y = width, 0, height, 0
    for x, y in positions:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    tree_height = max_y - min_y + 1
    tree_base = max_x - min_x + 1

    if tree_height < 5 or tree_base < 3:
        return False

    if tree_height > tree_base * 2: # ensure not too tall
        return False

    total_points = len(positions)
    expected_points = (tree_base * tree_height) / 2

    if not (expected_points * 0.2 < total_points):
        return False
    
    # Check for decreasing count in the rows
    previous_count = 10000
    for y in range(min_y, max_y + 1):
        current_row_count = sum(1 for x in range(min_x, max_x + 1) if (x, y) in positions)

        if y == min_y and current_row_count > tree_base * 0.6:
            return False # top is too wide
            
        if current_row_count > previous_count * 1.3 : # check decreasing number of robots
            return False
        if current_row_count > previous_count * 1.1 +2 : # allow for some fluctuation
            return False
            
        previous_count = current_row_count

    return True


def find_christmas_tree_time(input_str: str) -> int:
    """Find the earliest time when robots form a Christmas tree pattern."""
    robots = parse_input(input_str)
    width, height = 101, 103

    for seconds in range(600):
        positions = get_positions_at_time(robots, width, height, seconds)
        if looks_like_tree(positions, width, height):
            return seconds

    return -1


def solution() -> int:
    """Read from stdin and return the solution."""
    input_data = sys.stdin.read()
    return find_christmas_tree_time(input_data)


if __name__ == "__main__":
    print(solution())
