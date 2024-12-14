"""Solution for calculating robot safety factor after 100 seconds."""
from typing import List, Tuple
import sys


def parse_input(input_str: str) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """Parse input string into list of position and velocity tuples."""
    robots = []
    for line in input_str.strip().splitlines():
        pos, vel = line.split()
        px, py = map(int, pos[2:].split(','))
        vx, vy = map(int, vel[2:].split(','))
        robots.append(((px, py), (vx, vy)))
    return robots


def calculate_position(
    initial_pos: Tuple[int, int],
    velocity: Tuple[int, int],
    time: int,
    width: int,
    height: int
) -> Tuple[int, int]:
    """Calculate final position after given time with wrapping."""
    x, y = initial_pos
    vx, vy = velocity
    
    # Calculate total movement
    total_x = (x + vx * time) % width
    total_y = (y + vy * time) % height
    
    return (total_x, total_y)


def count_robots_in_quadrants(
    positions: List[Tuple[int, int]], 
    width: int, 
    height: int
) -> Tuple[int, int, int, int]:
    """Count robots in each quadrant, ignoring middle lines."""
    mid_x = width // 2
    mid_y = height // 2
    q1, q2, q3, q4 = 0, 0, 0, 0
    
    for x, y in positions:
        if x == mid_x or y == mid_y:
            continue
        
        if x < mid_x and y < mid_y:
            q1 += 1
        elif x > mid_x and y < mid_y:
            q2 += 1
        elif x < mid_x and y > mid_y:
            q3 += 1
        elif x > mid_x and y > mid_y:
            q4 += 1
    
    return (q1, q2, q3, q4)


def calculate_safety_factor(input_str: str) -> int:
    """Calculate the safety factor after 100 seconds."""
    robots = parse_input(input_str)
    WIDTH = 101
    HEIGHT = 103
    TIME = 100
    
    # Calculate final positions
    final_positions = []
    for pos, vel in robots:
        final_pos = calculate_position(pos, vel, TIME, WIDTH, HEIGHT)
        final_positions.append(final_pos)
    
    # Count robots in quadrants and calculate safety factor
    q1, q2, q3, q4 = count_robots_in_quadrants(final_positions, WIDTH, HEIGHT)
    return q1 * q2 * q3 * q4


def solution() -> int:
    """Read from stdin and return the result."""
    return calculate_safety_factor(sys.stdin.read())

if __name__ == "__main__":
    print(solution())