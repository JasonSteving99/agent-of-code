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
    if not positions:
        return False

    robot_grid = defaultdict(int)
    for x, y in positions:
        robot_grid[(x, y)] += 1

    min_x = min(x for x, _ in positions)
    max_x = max(x for x, _ in positions)
    min_y = min(y for _, y in positions)
    max_y = max(y for _, y in positions)

    if max_x - min_x < 4 or max_y - min_y < 4:
      return False

    center_x = (min_x + max_x) // 2
    center_y = (min_y + max_y) // 2
    
    # Check for a central trunk
    trunk_found = False
    for y_offset in range(2):
      check_x = center_x
      check_y = (max_y - y_offset) % height
      if robot_grid[(check_x, check_y)] > 0:
        trunk_found = True
        break
    if not trunk_found:
      return False
    
    # Check for wider branches, starting from the top (y=min_y) and going down
    levels = []
    for y_offset in range(max_y - min_y + 1):
        level_positions = []
        for x_offset in range(min_x, max_x + 1):
            check_x = x_offset % width
            check_y = (min_y + y_offset) % height
            if robot_grid[(check_x, check_y)] > 0:
                level_positions.append((check_x, check_y))
        if level_positions:
            levels.append(level_positions)
    
    # Basic triangular check: each row has more elements or same count as previous one
    if len(levels) < 3:
      return False

    for i in range(len(levels)-1):
        if len(levels[i]) > len(levels[i+1]):
            return False

    return True
    
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