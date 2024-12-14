from typing import List, Tuple, Set
import sys

def parse_input(line: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """Parse a line containing position and velocity."""
    p_part, v_part = line.strip().split()
    px, py = map(int, p_part[2:].split(','))
    vx, vy = map(int, v_part[2:].split(','))
    return ((px, py), (vx, vy))

def get_positions_at_time(robots: List[Tuple[Tuple[int, int], Tuple[int, int]]], 
                         width: int, height: int, time: int) -> Set[Tuple[int, int]]:
    """Calculate positions of all robots at a given time."""
    positions = set()
    for pos, vel in robots:
        x = (pos[0] + vel[0] * time) % width
        y = (pos[1] + vel[1] * time) % height
        positions.add((x, y))
    return positions

def is_christmas_tree(positions: Set[Tuple[int, int]], width: int, height: int) -> bool:
    """Check if the robots form a Christmas tree pattern."""
    if not positions:
      return False

    grid = [[0] * width for _ in range(height)]
    for x, y in positions:
        grid[y][x] = 1

    min_y = min(y for _, y in positions)
    top_points = [(x, y) for x, y in positions if y == min_y]
    if len(top_points) != 1:  # Should have exactly one point at top
        return False
    top_x = top_points[0][0] 

    row_counts = [sum(1 for x, y in positions if y == row) for row in range(height)]

    star_y = min_y
    trunk_found = False
    max_width = 0
    max_width_y = -1
    
    for y in range(star_y + 1, height):
        count = row_counts[y]
        if count == 0:
            continue
        if count > max_width:
            max_width = count
            max_width_y = y
            
        # Found potential trunk
        if count <= 2 and y > max_width_y and max_width >= 3:
            trunk_points = [(x,y) for x,y in positions if y == y ]
            trunk_x_values = [x for x,y in trunk_points]
            if len(trunk_x_values) > 0 and all(abs(x - top_x) <= 1 for x in trunk_x_values):
                trunk_found = True
                break

    if (row_counts[min_y] == 1 and
        max_width >= 3 and
        trunk_found and
        max_width_y > star_y):
        return True
        
    return False

def find_christmas_tree_time(input_data: str) -> int:
    # Parse input
    lines = input_data.strip().split('\n')
    robots = [parse_input(line) for line in lines]
    
    # Set dimensions (101x103 for actual input)
    width = 101
    height = 103
    
    for time in range(1000):  # reasonable upper limit
        positions = get_positions_at_time(robots, width, height, time)
        if is_christmas_tree(positions, width, height):
            return time
            
    return -1  # If no pattern found

def solution() -> int:
    # Read input from stdin
    input_data = sys.stdin.read()
    return find_christmas_tree_time(input_data)

if __name__ == "__main__":
    print(solution())