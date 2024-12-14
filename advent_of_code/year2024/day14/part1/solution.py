from typing import List, Tuple
import sys


def parse_input(input_str: str) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """Parse input string to get list of robot positions and velocities."""
    robots = []
    for line in input_str.strip().split('\n'):
        # Split position and velocity parts
        pos_part, vel_part = line.split()
        # Extract position coordinates
        px, py = map(int, pos_part[2:].split(','))
        # Extract velocity components
        vx, vy = map(int, vel_part[2:].split(','))
        robots.append(((px, py), (vx, vy)))
    return robots


def update_position(pos: Tuple[int, int], vel: Tuple[int, int], width: int, height: int) -> Tuple[int, int]:
    """Update position based on velocity and teleport to the other side if it hits an edge."""
    x, y = pos
    vx, vy = vel
    new_x = x + vx
    new_y = y + vy

    if new_x < 0:
        new_x = width - 1
    elif new_x >= width:
        new_x = 0
    
    if new_y < 0:
        new_y = height - 1
    elif new_y >= height:
        new_y = 0

    return (new_x, new_y)


def count_quadrants(robot_positions: List[Tuple[int, int]], width: int, height: int) -> Tuple[int, int, int, int]:
    """Count robots in each quadrant, excluding those on middle lines."""
    mid_x = width // 2
    mid_y = height // 2
    q1, q2, q3, q4 = 0, 0, 0, 0

    for x, y in robot_positions:
        # Skip if robot is on middle lines
        if x == mid_x or y == mid_y:
            continue
        
        # Count robots in each quadrant
        if x < mid_x and y < mid_y:  # Top-left
            q1 += 1
        elif x > mid_x and y < mid_y:  # Top-right
            q2 += 1
        elif x < mid_x and y > mid_y:  # Bottom-left
            q3 += 1
        elif x > mid_x and y > mid_y:  # Bottom-right
            q4 += 1

    return (q1, q2, q3, q4)


def calculate_safety_factor(input_str: str) -> int:
    """
    Calculate the safety factor after simulating robot movement for 100 seconds.
    """
    # Constants
    WIDTH = 101
    HEIGHT = 103
    SECONDS = 100

    # Parse input
    robots = parse_input(input_str)
    
    # Simulate movement for 100 seconds
    positions = [pos for pos, _ in robots]
    velocities = [vel for _, vel in robots]
    
    for _ in range(SECONDS):
        # Update positions
        positions = [
            update_position(pos, vel, WIDTH, HEIGHT)
            for pos, vel in zip(positions, velocities)
        ]
    
    # Count robots in quadrants
    q1, q2, q3, q4 = count_quadrants(positions, WIDTH, HEIGHT)
    
    # Calculate safety factor
    return q1 * q2 * q3 * q4


def solution() -> int:
    """Read from stdin and return result."""
    return calculate_safety_factor(sys.stdin.read().strip())


if __name__ == "__main__":
    print(solution())