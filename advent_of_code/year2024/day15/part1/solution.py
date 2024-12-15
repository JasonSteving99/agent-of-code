"""Implementation for solving the warehouse robot movement puzzle"""
from typing import List, Set, Tuple
import re
from html import unescape

def parse_input(input_str: str) -> Tuple[List[List[str]], str]:
    """Parse the input string into warehouse layout and movement instructions"""
    parts = input_str.strip().split('\n\n')
    layout = [list(line) for line in parts[0].splitlines()]
    movements = ''.join(unescape(parts[1]).split())
    return layout, movements

def find_robot(layout: List[List[str]]) -> Tuple[int, int]:
    """Find the initial position of the robot"""
    for i, row in enumerate(layout):
        for j, cell in enumerate(row):
            if cell == '@':
                return i, j
    raise ValueError("Robot not found in layout")

def move_possible(layout: List[List[str]], from_pos: Tuple[int, int], 
                 to_pos: Tuple[int, int], box_pos: Tuple[int, int] = None) -> bool:
    """Check if a move is possible"""
    rows, cols = len(layout), len(layout[0])
    
    # Check if destination is within bounds
    if not (0 <= to_pos[0] < rows and 0 <= to_pos[1] < cols):
        return False
    
    # Check if destination is a wall
    if layout[to_pos[0]][to_pos[1]] == '#':
        return False
        
    # If moving a box, check if destination is clear
    if box_pos and (layout[to_pos[0]][to_pos[1]] in ['O', '#']):
        return False
        
    return True

def get_box_coordinates(layout: List[List[str]]) -> Set[Tuple[int, int]]:
    """Get coordinates of all boxes"""
    boxes = set()
    for i, row in enumerate(layout):
        for j, cell in enumerate(row):
            if cell == 'O':
                boxes.add((i, j))
    return boxes

def calculate_gps_sum(boxes: Set[Tuple[int, int]]) -> int:
    """Calculate the sum of GPS coordinates for all boxes"""
    return sum(100 * row + col for row, col in boxes)

def calculate_final_gps_sum(input_str: str) -> int:
    """
    Calculate the sum of GPS coordinates of all boxes after robot movement
    
    Args:
        input_str: String containing warehouse layout and movement instructions
    
    Returns:
        int: Sum of GPS coordinates of all boxes after movement
    """
    # Parse input
    layout, movements = parse_input(input_str)
    
    # Get initial robot position and box positions
    robot_pos = find_robot(layout)
    
    # Direction vectors for movement
    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }
    
    # Process each movement
    curr_pos = robot_pos
    layout[curr_pos[0]][curr_pos[1]] = '.'  # Clear initial robot position
    
    for move in movements:
        dx, dy = directions[move]
        new_pos = (curr_pos[0] + dx, curr_pos[1] + dy)
        
        # Check if movement is possible
        if not move_possible(layout, curr_pos, new_pos):
            continue
            
        # If there's a box in the way
        if layout[new_pos[0]][new_pos[1]] == 'O':
            box_new_pos = (new_pos[0] + dx, new_pos[1] + dy)
            
            # Check if box can be pushed
            if not move_possible(layout, new_pos, box_new_pos, box_new_pos):
                continue
                
            # Move box
            layout[new_pos[0]][new_pos[1]] = '.'
            layout[box_new_pos[0]][box_new_pos[1]] = 'O'
        
        # Move robot
        curr_pos = new_pos
    
    # Get final box positions and calculate GPS sum
    boxes = get_box_coordinates(layout)
    return calculate_gps_sum(boxes)