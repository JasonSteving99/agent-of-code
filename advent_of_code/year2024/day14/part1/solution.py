"""Solution for calculating safety factor after robot movement simulation."""
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


def simulate_movement(robots: List[Tuple[Tuple[int, int], Tuple[int, int]]], 
                     width: int, height: int, seconds: int) -> Dict[Tuple[int, int], int]:
    """Simulate robot movement for given number of seconds."""
    positions = {}
    
    for pos, vel in robots:
        curr_pos = pos
        for _ in range(seconds):
            curr_pos = update_position(curr_pos, vel, width, height)
        positions[curr_pos] = positions.get(curr_pos, 0) + 1
        
    return positions


def count_quadrants(positions: Dict[Tuple[int, int], int], width: int, height: int) -> List[int]:
    """Count robots in each quadrant, excluding middle lines."""
    mid_x = width // 2
    mid_y = height // 2
    quadrants = [0, 0, 0, 0]  # TL, TR, BL, BR
    
    for (x, y), count in positions.items():
        # Skip robots on middle lines
        if x == mid_x or y == mid_y:
            continue
            
        quadrant_idx = (1 if x > mid_x else 0) + (2 if y > mid_y else 0)
        quadrants[quadrant_idx] += count
    
    return quadrants


def calculate_safety_factor(input_str: str) -> int:
    """Calculate safety factor based on robot positions after 100 seconds."""
    # Parse input
    robots = parse_input(input_str)
    
    # Define grid dimensions
    width, height = 101, 103
    
    # Simulate movement for 100 seconds
    final_positions = simulate_movement(robots, width, height, 100)
    
    # Count robots in each quadrant
    quadrant_counts = count_quadrants(final_positions, width, height)
    
    # Calculate safety factor (multiply all quadrant counts)
    safety_factor = 1
    for count in quadrant_counts:
        safety_factor *= count
    
    return safety_factor


def solution() -> int:
    """Read from stdin and return the solution."""
    input_data = sys.stdin.read()
    return calculate_safety_factor(input_data)


if __name__ == "__main__":
    print(solution())