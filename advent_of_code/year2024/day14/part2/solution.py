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
    """Check if the robots form a Christmas tree pattern based on row lengths."""
    if not positions:
        return False

    # Group robots by their y coordinates
    rows = {}
    for (x, y), count in positions.items():
        rows.setdefault(y, 0)
        rows[y] += count

    if len(rows) < 4:
        return False

    sorted_rows = sorted(rows.items())
    row_lengths = [length for _, length in sorted_rows]
    
    # Find the center row (longest one)
    max_row_length = max(row_lengths)
    center_index = row_lengths.index(max_row_length)
    
    if max_row_length < 3:
        return False
    
    # Check for decreasing lengths symmetrically from center
    for i in range(center_index):
        if row_lengths[i] > row_lengths[i + 1] + 2 or row_lengths[i] <= 0:
          return False
          
    for i in range(center_index, len(row_lengths) - 1):
      if row_lengths[i+1] > row_lengths[i] + 2 or row_lengths[i+1] <= 0:
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
