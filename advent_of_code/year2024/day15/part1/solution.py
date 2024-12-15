"""Solution for the warehouse robot box-pushing puzzle."""
from typing import List, Set, Tuple, Optional


def parse_input(input_text: str) -> Tuple[List[List[str]], List[str]]:
    """Parse input into warehouse grid and moves list."""
    sections = input_text.strip().split('\n\n')
    
    # Parse warehouse grid
    grid = [list(line) for line in sections[0].strip().split('\n')]
    
    # Parse moves (ignore newlines in moves section)
    moves = list(''.join(sections[1].strip().split('\n')))
    
    return grid, moves


def get_robot_position(grid: List[List[str]]) -> Tuple[int, int]:
    """Find the robot's (@) position in the grid."""
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '@':
                return i, j
    raise ValueError("Robot not found in grid")


def try_move(grid: List[List[str]], robot_pos: Tuple[int, int], 
             direction: str) -> Optional[Tuple[int, int]]:
    """Try to move the robot in the given direction, pushing boxes if needed."""
    moves = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    dy, dx = moves[direction]
    r, c = robot_pos
    
    # Check next position
    new_r, new_c = r + dy, c + dx
    
    # If hitting a wall, can't move
    if grid[new_r][new_c] == '#':
        return None
    
    # If empty space, can move
    if grid[new_r][new_c] == '.':
        grid[new_r][new_c] = '@'
        grid[r][c] = '.'
        return (new_r, new_c)
    
    # If box, try to push it
    if grid[new_r][new_c] == 'O':
        box_new_r, box_new_c = new_r + dy, new_c + dx
        # Can't push if wall or another box
        if grid[box_new_r][box_new_c] == '#' or grid[box_new_r][box_new_c] == 'O':
            return None
        # Push box and move robot
        grid[box_new_r][box_new_c] = 'O'
        grid[new_r][new_c] = '@'
        if grid[r][c] != 'O':
           grid[r][c] = '.'
        return (new_r, new_c)
    
    return None


def calculate_box_gps_sum(grid: List[List[str]]) -> int:
    """Calculate sum of GPS coordinates for all boxes."""
    total = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'O':
                # GPS coordinate = 100 * row + column (0-based indexing)
                total += (100 * i) + j
    return total


def calculate_final_box_gps_sum(input_text: str) -> int:
    """Calculate the sum of GPS coordinates after robot finishes moving."""
    # Parse input
    grid, moves = parse_input(input_text)
    
    # Get initial robot position
    robot_pos = get_robot_position(grid)
    
    # Execute each move
    for move in moves:
        new_pos = try_move(grid, robot_pos, move)
        if new_pos is not None:
            robot_pos = new_pos
    
    # Calculate final GPS sum
    return calculate_box_gps_sum(grid)