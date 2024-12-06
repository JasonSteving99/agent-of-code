from typing import List, Set, Tuple
import sys

def get_guard_start_position(grid: List[str]) -> Tuple[int, int, str]:
    """Find the starting position and direction of the guard."""
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '^':
                return (i, j, 'N')
    raise ValueError("No guard starting position found")

def count_guard_visited_positions(grid_str: str) -> int:
    """
    Count the number of distinct positions visited by the guard before leaving the map area.
    
    Args:
        grid_str: String representation of the grid with newlines
    Returns:
        Integer count of distinct positions visited by the guard
    """
    # Parse grid into list of strings
    grid = grid_str.strip().split('\n')
    height, width = len(grid), len(grid[0])
    
    # Direction mapping for movement and turning right
    directions = {
        'N': (-1, 0),  # Up
        'E': (0, 1),   # Right
        'S': (1, 0),   # Down
        'W': (0, -1)   # Left
    }
    turn_right = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    
    # Get starting position and direction
    row, col, direction = get_guard_start_position(grid)
    
    # Keep track of visited positions
    visited: Set[Tuple[int, int]] = {(row, col)}
    
    while True:
        # Calculate next position
        dr, dc = directions[direction]
        next_row, next_col = row + dr, col + dc
        
        # Check if next move is out of bounds or hitting an obstacle
        if not (0 <= next_row < height and 0 <= next_col < width) or grid[next_row][next_col] == '#':
            direction = turn_right[direction]  # Turn right
        else:
            row, col = next_row, next_col
            visited.add((row, col))
            
        # Recalculate next position based on potentially new direction        
        dr, dc = directions[direction]
        next_row, next_col = row + dr, col + dc

        # Check if current position (after potential move or turn) is out of bounds. Break if so
        if not (0 <= next_row < height and 0 <= next_col < width):
            break
            
    return len(visited)

def solution() -> int:
    """Read the input from stdin and return the solution."""
    input_data = sys.stdin.read().strip()
    return count_guard_visited_positions(input_data)

if __name__ == "__main__":
    print(solution())