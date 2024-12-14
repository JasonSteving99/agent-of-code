"""Solution for finding when robots form a Christmas tree pattern."""
from typing import List, Tuple, Dict, Set
import sys
from collections import defaultdict


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
    x = x % width
    y = y % height
    return (x, y)


def is_christmas_tree_pattern(positions: Dict[Tuple[int, int], int], width: int, height: int) -> bool:
    """Check if the current robot positions form a Christmas tree pattern."""
    # Convert positions to a set of occupied coordinates for easier checking
    occupied = set()
    for pos, count in positions.items():
        for _ in range(count):
            occupied.add(pos)
    
    # Get bounds of the occupied positions
    if not occupied:
        return False
    
    min_x = min(x for x, _ in occupied)
    max_x = max(x for x, _ in occupied)
    min_y = min(y for _, y in occupied)
    max_y = max(y for _, y in occupied)
    
    # The tree should be roughly centered in the grid
    center_x = width // 2
    if abs(min_x + max_x - width) > width // 4:  # Tree not centered enough
        return False
    
    # Check for general tree shape:
    # 1. Single point at top (star)
    # 2. Triangular shape widening towards bottom
    # 3. Small rectangle at bottom (trunk)
    
    levels = defaultdict(set)
    for x, y in occupied:
        levels[y].add(x)
    
    # Sort levels from top to bottom
    sorted_levels = sorted(levels.items(), key=lambda x: x[0])
    
    if len(sorted_levels) < 5:  # Need minimum height for a tree
        return False
    
    # Check for single star at top
    if len(sorted_levels[0][1]) != 1:
        return False
    
    # Check for widening pattern in middle (tree shape)
    middle_section = sorted_levels[1:-1]
    prev_width = 0
    for _, level_points in middle_section:
        curr_width = max(level_points) - min(level_points)
        if curr_width <= prev_width:
            return False
        prev_width = curr_width
    
    # Check for narrow trunk at bottom
    trunk_points = sorted_levels[-1][1]
    trunk_width = max(trunk_points) - min(trunk_points)
    if trunk_width > 3:  # Trunk should be narrow
        return False
    
    return True


def simulate_until_tree(robots: List[Tuple[Tuple[int, int], Tuple[int, int]]], 
                       width: int, height: int, max_seconds: int = 1000) -> int:
    """Simulate robot movement until Christmas tree pattern is found."""
    for second in range(max_seconds):
        positions = {}
        
        # Update positions for all robots
        for pos, vel in robots:
            curr_pos = pos
            for _ in range(second):
                curr_pos = update_position(curr_pos, vel, width, height)
            positions[curr_pos] = positions.get(curr_pos, 0) + 1
        
        # Check if current positions form a Christmas tree
        if is_christmas_tree_pattern(positions, width, height):
            return second
    
    return -1  # Pattern not found within max_seconds


def find_christmas_tree(input_str: str) -> int:
    """Find how many seconds it takes for robots to form a Christmas tree pattern."""
    # Parse input
    robots = parse_input(input_str)
    
    # Define grid dimensions
    width, height = 101, 103
    
    # Simulate movement until tree pattern is found
    seconds = simulate_until_tree(robots, width, height)
    
    return seconds


def solution() -> int:
    """Read from stdin and return the solution."""
    input_data = sys.stdin.read()
    return find_christmas_tree(input_data)


if __name__ == "__main__":
    print(solution())