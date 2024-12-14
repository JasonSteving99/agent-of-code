from typing import List, Tuple
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

def count_robots_in_quadrants(positions: List[Tuple[int, int]], 
                            width: int, height: int) -> List[int]:
    """Count robots in each quadrant, excluding those on dividing lines."""
    mid_x = width // 2
    mid_y = height // 2
    quadrants = [0] * 4
    
    for x, y in positions:
        # Skip robots on dividing lines
        if x == mid_x or y == mid_y:
            continue
            
        # Determine quadrant (0: top-left, 1: top-right, 2: bottom-left, 3: bottom-right)
        quadrant = (2 if y > mid_y else 0) + (1 if x > mid_x else 0)
        quadrants[quadrant] += 1
        
    return quadrants

def calculate_safety_factor(input_data: str) -> int:
    # Parse input
    lines = input_data.strip().split('\n')
    robots = [parse_input(line) for line in lines]
    
    # Set dimensions (101x103 for actual input)
    width = 101
    height = 103
    time = 100  # seconds
    
    # Calculate final positions
    final_positions = [
        get_position_after_time(pos, vel, width, height, time)
        for pos, vel in robots
    ]
    
    # Count robots in quadrants
    quadrant_counts = count_robots_in_quadrants(final_positions, width, height)
    
    # Calculate safety factor (multiply all quadrant counts)
    safety_factor = 1
    for count in quadrant_counts:
        safety_factor *= count
        
    return safety_factor

def solution() -> int:
    # Read input from stdin
    input_data = sys.stdin.read()
    return calculate_safety_factor(input_data)

if __name__ == "__main__":
    print(solution())