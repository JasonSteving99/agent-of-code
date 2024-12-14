from typing import List, Tuple, Set
import sys

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

def is_christmas_tree_pattern(positions: List[Tuple[int, int]], width: int, height: int) -> bool:
    """Check if the current positions form a Christmas tree pattern."""
    if not positions:
        return False

    min_x = min(x for x, _ in positions)
    max_x = max(x for x, _ in positions)
    min_y = min(y for _, y in positions)
    max_y = max(y for _, y in positions)

    if max_x - min_x > width // 2 or max_y - min_y > height // 2:
        return False
    
    points_by_row = {}
    for x, y in positions:
        if y not in points_by_row:
            points_by_row[y] = 0
        points_by_row[y] += 1
    
    sorted_rows = sorted(points_by_row.keys())

    if not sorted_rows:
        return False
    
    for i in range(len(sorted_rows) - 1):
      if points_by_row[sorted_rows[i]] < points_by_row[sorted_rows[i+1]]:
        return False
    
    if len(sorted_rows) < 3: # minimal tree needs a base and some levels
        return False

    return True

def find_christmas_tree(input_data: str) -> int:
    # Parse input
    lines = input_data.strip().split('\n')
    robots = [parse_input(line) for line in lines]
    
    width = 101
    height = 103
    
    # Check each second up to a reasonable maximum
    max_time = 1000  # Reasonable upper limit
    
    for time in range(max_time):
        positions = [
            get_position_after_time(pos, vel, width, height, time)
            for pos, vel in robots
        ]
        
        if is_christmas_tree_pattern(positions, width, height):
            return time
    
    # If no pattern is found, return -1 or raise an exception
    return -1

def solution() -> int:
    input_data = sys.stdin.read()
    return find_christmas_tree(input_data)

if __name__ == "__main__":
    print(solution())