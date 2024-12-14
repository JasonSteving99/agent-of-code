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
    # Convert positions to a set for faster lookup
    pos_set = set(positions)
    
    # Find the bounding box of all positions
    if not positions:
        return False
    
    min_x = min(x for x, _ in positions)
    max_x = max(x for x, _ in positions)
    min_y = min(y for _, y in positions)
    max_y = max(y for _, y in positions)
    
    # The pattern should be relatively compact
    if max_x - min_x > width // 3 or max_y - min_y > height // 3:
        return False
        
    # Center point of the pattern
    center_x = (min_x + max_x) // 2
    
    # Count points in triangular shape
    tree_points = 0
    trunk_points = 0
    
    for x, y in pos_set:
        # Normalize coordinates relative to center
        rel_x = x - center_x
        rel_y = y - min_y
        
        # Check tree portion (triangular shape)
        if rel_y < (max_y - min_y) * 2 // 3:
            if abs(rel_x) <= rel_y // 2:  # Triangular shape check
                tree_points += 1
        # Check trunk portion
        else:
            if abs(rel_x) <= 1:  # Narrow trunk
                trunk_points += 1
    
    # Verify we have enough points in both tree and trunk sections
    total_points = len(positions)
    return (tree_points >= total_points * 2 // 3 and 
            trunk_points >= 2 and 
            trunk_points <= total_points // 4)

def find_christmas_tree(input_data: str) -> int:
    # Parse input
    lines = input_data.strip().split('\n')
    robots = [parse_input(line) for line in lines]
    
    width = 101
    height = 103
    
    # Check each second up to a reasonable maximum
    # Since we're looking for a pattern, it's likely to occur within
    # a relatively small number of steps
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