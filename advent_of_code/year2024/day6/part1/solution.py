from typing import List, Set, Tuple
import sys


def count_visited_positions(initial_map: str) -> int:
    """
    Count the number of distinct positions visited by the guard before leaving the mapped area.
    
    Args:
        initial_map: String representation of the map with guard position and obstacles
        
    Returns:
        Number of distinct positions visited
    """
    # Convert the map to a 2D grid
    grid = [list(line) for line in initial_map.strip().split('\n')]
    rows, cols = len(grid), len(grid[0])
    
    # Find guard's starting position and direction
    start_pos = None
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '^':
                start_pos = (i, j)
                break
        if start_pos:
            break
            
    # Define direction vectors (up, right, down, left)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_chars = ['^', '>', 'v', '<']
    current_dir = 0  # Start facing up
    
    visited: Set[Tuple[int, int]] = {start_pos}
    current_pos = start_pos
    
    while True:
        row, col = current_pos
        
        # Check if we're still in bounds
        if row < 0 or row >= rows or col < 0 or col >= cols:
            break
        
        # Get the next position in current direction
        next_row = row + directions[current_dir][0]
        next_col = col + directions[current_dir][1]
        
        # Check if there's an obstacle or out of bounds ahead
        if (next_row < 0 or next_row >= rows or 
            next_col < 0 or next_col >= cols or 
            grid[next_row][next_col] == '#'):
            # Turn right
            current_dir = (current_dir + 1) % 4
        else:
            # Move forward
            current_pos = (next_row, next_col)
            visited.add(current_pos)
    
    return len(visited)


def solution() -> int:
    """Read input from stdin and solve the problem."""
    # Read input lines until EOF
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line.rstrip())
    
    # Join lines with newlines to create the map string
    initial_map = '\n'.join(input_lines)
    
    return count_visited_positions(initial_map)