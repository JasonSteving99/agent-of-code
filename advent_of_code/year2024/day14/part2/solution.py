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
    """Check if the robots form a more general tree-like shape."""
    if not positions:
        return False

    x_coords = [pos[0] for pos in positions]
    y_coords = [pos[1] for pos in positions]
    
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)
    
    bbox_width = max_x - min_x
    bbox_height = max_y - min_y

    # Check bounding box is somewhat elongated vertically
    if bbox_height < 10 or bbox_width > bbox_height: 
       return False
    
    # Count positions near the center for a tree-like distribution
    mid_x = width // 2
    mid_y = (min_y + max_y) // 2 #approx center for given y range

    center_points = 0
    for x, y in positions:
        if abs(x- mid_x) < bbox_width//3 and abs(y-mid_y) < bbox_height//2:
            center_points += 1
    
    # Ensure a reasonable cluster of points near center
    if center_points < 4: 
        return False

    # Check we have enough robots to form a tree
    total_robots = sum(positions.values())
    if total_robots < 8:
       return False
    
    return True


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
