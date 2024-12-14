"""Solution for Restroom Redoubt problem"""
from dataclasses import dataclass
from typing import List, Tuple
import sys


@dataclass
class Robot:
    """Class representing a robot's position and velocity"""
    pos_x: int
    pos_y: int
    vel_x: int
    vel_y: int


def parse_robot(line: str) -> Robot:
    """Parse a single line of input into a Robot object"""
    pos, vel = line.strip().split()
    px, py = map(int, pos[2:].split(','))
    vx, vy = map(int, vel[2:].split(','))
    return Robot(px, py, vx, vy)


def get_final_positions(robots: List[Robot], width: int, height: int, seconds: int) -> List[Tuple[int, int]]:
    """Calculate final positions of all robots after given seconds"""
    positions = []
    for robot in robots:
        # Calculate final position using modulo for wrapping
        final_x = (robot.pos_x + robot.vel_x * seconds) % width
        final_y = (robot.pos_y + robot.vel_y * seconds) % height
        positions.append((final_x, final_y))
    return positions


def count_robots_in_quadrants(positions: List[Tuple[int, int]], width: int, height: int) -> Tuple[int, int, int, int]:
    """Count robots in each quadrant, excluding center lines"""
    top_left = 0
    top_right = 0
    bottom_left = 0
    bottom_right = 0
    
    mid_x = width // 2
    mid_y = height // 2
    
    for x, y in positions:
      if x == mid_x and y == mid_y:
        continue

      if x <= mid_x and y <= mid_y:
          top_left += 1
      elif x > mid_x and y <= mid_y:
          top_right += 1
      elif x <= mid_x and y > mid_y:
          bottom_left += 1
      elif x > mid_x and y > mid_y:
          bottom_right += 1
    
    return (top_left, top_right, bottom_left, bottom_right)


def calculate_safety_factor(input_data: str) -> int:
    """
    Calculate the safety factor based on robot positions after 100 seconds
    
    Args:
        input_data: String containing robot positions and velocities
        
    Returns:
        Safety factor (product of robot counts in each quadrant)
    """
    # Parse input
    robots = [parse_robot(line) for line in input_data.strip().splitlines()]
    
    # Constants for the problem
    WIDTH = 101
    HEIGHT = 103
    SECONDS = 100
    
    # Get final positions
    final_positions = get_final_positions(robots, WIDTH, HEIGHT, SECONDS)
    
    # Count robots in quadrants
    q1, q2, q3, q4 = count_robots_in_quadrants(final_positions, WIDTH, HEIGHT)
    
    # Calculate safety factor
    return q1 * q2 * q3 * q4


def solution() -> int:
    """Read from stdin and return the result"""
    return calculate_safety_factor(sys.stdin.read())
