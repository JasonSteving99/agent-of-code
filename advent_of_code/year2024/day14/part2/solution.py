"""Solution for finding time when robots form Christmas tree pattern."""
from typing import List, Tuple, Dict
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


def simulate_step(robots: List[Tuple[Tuple[int, int], Tuple[int, int]]], 
                 width: int, height: int) -> Dict[Tuple[int, int], int]:
    """Simulate one step of robot movement."""
    positions = {}
    for pos, vel in robots:
        new_pos = update_position(pos, vel, width, height)
        positions[new_pos] = positions.get(new_pos, 0) + 1
    return positions


def is_christmas_tree_pattern(positions: Dict[Tuple[int, int], int], width: int, height: int) -> bool:
    """Check if the robots form a Christmas tree pattern."""
    mid_x = width // 2
    center_line_count = sum(1 for (x, y), count in positions.items() if x == mid_x)
    
    # Check if we have a vertical line in the center
    if center_line_count < 3:
        return False
    
    # Count robots in triangular pattern around center
    left_side = 0
    right_side = 0
    
    for (x, y), count in positions.items():
        dist_from_center = abs(x - mid_x)
        if dist_from_center < 10:  # reasonable distance for tree width
            if x < mid_x:
                left_side += count
            elif x > mid_x:
                right_side += count
    
    # Check if sides are roughly symmetrical
    if abs(left_side - right_side) > 2:
        return False
    
    # Check if we have enough robots to form a tree
    total_robots = sum(positions.values())
    return total_robots >= 10  # reasonable minimum for a tree pattern


def find_christmas_tree_time(input_str: str) -> int:
    """Find the earliest time when robots form a Christmas tree pattern."""
    robots = parse_input(input_str)
    width, height = 101, 103
    
    # Keep track of each robot's current position and velocity
    current_robots = robots.copy()
    
    # Simulate for a reasonable time period
    for t in range(1000):  # Set a reasonable upper limit
        # Update positions for all robots
        new_positions = {}
        new_robots = []
        
        for (pos, vel) in current_robots:
            new_pos = update_position(pos, vel, width, height)
            new_positions[new_pos] = new_positions.get(new_pos, 0) + 1
            new_robots.append((new_pos, vel))
        
        # Check if current positions form a Christmas tree
        if is_christmas_tree_pattern(new_positions, width, height):
            return t
        
        current_robots = new_robots
    
    return -1  # Return -1 if no pattern is found within limit


def solution() -> int:
    """Read from stdin and return the solution."""
    input_data = sys.stdin.read()
    return find_christmas_tree_time(input_data)


if __name__ == "__main__":
    print(solution())