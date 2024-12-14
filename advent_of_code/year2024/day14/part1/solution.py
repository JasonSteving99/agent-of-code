"""Solution for calculating safety factor of robot positions."""
from typing import Tuple, List
import sys


class Robot:
    """Class representing a robot with position and velocity."""
    def __init__(self, pos: Tuple[int, int], vel: Tuple[int, int]):
        self.pos = pos
        self.vel = vel


def parse_input(input_str: str) -> List[Robot]:
    """Parse input string to create list of robots."""
    robots = []
    for line in input_str.strip().splitlines():
        pos_str, vel_str = line.split()
        px, py = map(int, pos_str[2:].split(','))
        vx, vy = map(int, vel_str[2:].split(','))
        robots.append(Robot((px, py), (vx, vy)))
    return robots


def update_position(pos: Tuple[int, int], vel: Tuple[int, int], width: int, height: int) -> Tuple[int, int]:
    """Update position of robot considering wrapping around edges."""
    new_x = (pos[0] + vel[0]) % width
    new_y = (pos[1] + vel[1]) % height
    return (new_x, new_y)


def get_quadrant(x: int, y: int, width: int, height: int) -> int:
    """Get the quadrant number (1-4) for a position, or 0 if on dividing lines."""
    mid_x = width // 2
    mid_y = height // 2
    
    if x == mid_x or y == mid_y:
        return 0
    
    if x < mid_x:
        if y < mid_y:
            return 1
        return 3
    else:
        if y < mid_y:
            return 2
        return 4


def calculate_safety_factor(input_data: str) -> int:
    """Calculate the safety factor after 100 seconds."""
    # Set dimensions
    width = 101
    height = 103
    time_steps = 100

    # Parse input and create robots
    robots = parse_input(input_data)
    
    # Simulate movement for specified time
    for _ in range(time_steps):
        for robot in robots:
            robot.pos = update_position(robot.pos, robot.vel, width, height)
    
    # Count robots in each quadrant
    quadrant_counts = [0] * 5  # Index 0 not used
    
    for robot in robots:
        quadrant = get_quadrant(robot.pos[0], robot.pos[1], width, height)
        if quadrant != 0:  # Don't count robots on dividing lines
            quadrant_counts[quadrant] += 1
    
    # Calculate safety factor (multiply non-zero quadrant counts)
    safety_factor = 1
    for count in quadrant_counts[1:]:  # Skip index 0
        safety_factor *= count
    
    return safety_factor


def solution() -> int:
    """Read from stdin and return the solution."""
    return calculate_safety_factor(sys.stdin.read().strip())

if __name__ == "__main__":
    print(solution())