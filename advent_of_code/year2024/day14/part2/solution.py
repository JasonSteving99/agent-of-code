from typing import List, Tuple, Dict
import sys
from collections import defaultdict

def parse_input(line: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """Parse a line containing position and velocity."""
    p_part, v_part = line.strip().split()
    px, py = map(int, p_part[2:].split(','))
    vx, vy = map(int, v_part[2:].split(','))
    return ((px, py), (vx, vy))

def get_position_after_time(pos: Tuple[int, int], vel: Tuple[int, int], 
                          width: int, height: int, time: int) -> Tuple[int, int]:
    """Calculate position after given time with wraparound."""
    x = (pos[0] + vel[0] * time) % width
    y = (pos[1] + vel[1] * time) % height
    return (x, y)

def looks_like_christmas_tree(positions: List[Tuple[int, int]], width: int, height: int) -> bool:
    """Check if the robots form a Christmas tree pattern."""
    # Convert positions to a grid-like structure
    robot_grid = defaultdict(int)
    for x, y in positions:
        robot_grid[(x, y)] += 1

    # Expected relative positions for a basic Christmas tree shape
    # Assuming the tree should have:
    # - A star/top point
    # - 2-3 levels of increasing width
    # - A trunk
    tree_pattern = {
        # Star/top
        (0, -2),
        # Top level
        (-1, -1), (0, -1), (1, -1),
        # Middle level
        (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0),
        # Bottom level
        (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1), (3, 1),
        # Trunk
        (0, 2), (0, 3)
    }

    required_matches = len(tree_pattern) * 0.8  # Allow for some imperfection
    
    # Iterate through all possible center points
    for cx in range(width):
        for cy in range(height):
            matches = 0
            for rel_x, rel_y in tree_pattern:
                check_x = (cx + rel_x) % width
                check_y = (cy + rel_y) % height
                if robot_grid[(check_x, check_y)] > 0:
                    matches += 1
            if matches >= required_matches:
                return True
    return False

def find_christmas_tree_time(input_data: str) -> int:
    # Parse input
    lines = input_data.strip().split('\n')
    robots = [parse_input(line) for line in lines]
    
    # Set dimensions (101x103 for actual input)
    width = 101
    height = 103
    
    # Check positions every second up to a reasonable limit
    MAX_TIME = 1000  # Reasonable upper limit
    
    for time in range(MAX_TIME):
        # Calculate positions at current time
        current_positions = [
            get_position_after_time(pos, vel, width, height, time)
            for pos, vel in robots
        ]
        
        # Check if current positions form a Christmas tree
        if looks_like_christmas_tree(current_positions, width, height):
            return time
    
    # If no pattern found within limit
    return -1

def solution() -> int:
    input_data = sys.stdin.read()
    return find_christmas_tree_time(input_data)

if __name__ == "__main__":
    print(solution())