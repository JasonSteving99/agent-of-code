"""Solution for calculating GPS coordinates sum after robot movements."""
from typing import List, Tuple, Set
import sys

def find_robot_and_boxes(grid: List[str]) -> Tuple[Tuple[int, int], Set[Tuple[int, int]]]:
    """Find starting positions of robot and boxes."""
    robot_pos = None
    boxes = set()
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '@':
                robot_pos = (i, j)
            elif cell == 'O':
                boxes.add((i, j))
    return robot_pos, boxes

def can_move(grid: List[str], 
             pos: Tuple[int, int], 
             boxes: Set[Tuple[int, int]], 
             new_pos: Tuple[int, int], 
             box_new_pos: Tuple[int, int] = None) -> bool:
    """Check if movement is possible."""
    if grid[new_pos[0]][new_pos[1]] == '#':
        return False
    if new_pos in boxes:
        if box_new_pos is None:
            return False
        if grid[box_new_pos[0]][box_new_pos[1]] == '#' or box_new_pos in boxes:
            return False
    return True

def move_robot(direction: str, 
               robot_pos: Tuple[int, int], 
               boxes: Set[Tuple[int, int]], 
               grid: List[str]) -> Tuple[Tuple[int, int], Set[Tuple[int, int]]]:
    """Move robot in given direction."""
    moves = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    dx, dy = moves[direction]
    new_pos = (robot_pos[0] + dx, robot_pos[1] + dy)
    
    if new_pos in boxes:
        box_new_pos = (new_pos[0] + dx, new_pos[1] + dy)
        if can_move(grid, robot_pos, boxes, new_pos, box_new_pos):
            boxes.remove(new_pos)
            boxes.add(box_new_pos)
            return new_pos, boxes
        return robot_pos, boxes
    
    if can_move(grid, robot_pos, boxes, new_pos):
        return new_pos, boxes
    return robot_pos, boxes

def calculate_gps_sum(boxes: Set[Tuple[int, int]]) -> int:
    """Calculate sum of GPS coordinates for all boxes."""
    return sum(100 * row + col for row, col in boxes)

def calculate_final_gps_sum(input_str: str) -> int:
    """Calculate the final sum of GPS coordinates after robot movements."""
    # Parse input
    parts = input_str.strip().split('\n\n')
    grid = [list(line) for line in parts[0].strip().split('\n')]
    moves = ''.join(parts[1].strip().split('\n'))
    
    # Find initial positions
    robot_pos, boxes = find_robot_and_boxes(grid)
    
    # Process movements
    for move in moves:
        robot_pos, boxes = move_robot(move, robot_pos, boxes, grid)
    
    return calculate_gps_sum(boxes)

def solution() -> int:
    """Read from stdin and return solution."""
    return calculate_final_gps_sum(sys.stdin.read())

if __name__ == "__main__":
    print(solution())