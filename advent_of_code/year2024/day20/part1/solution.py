from collections import deque
from typing import List, Set, Tuple
import sys


def find_start_end(grid: List[str]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """Find start and end positions in the grid."""
    start = end = None
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (i, j)
            elif cell == 'E':
                end = (i, j)
    assert start is not None and end is not None
    return start, end


def shortest_path_without_cheats(input_map: str) -> int:
    """
    Find the shortest path from start to end without using any cheats.
    
    Args:
        input_map: String representing the racetrack map.
        
    Returns:
        The number of picoseconds needed to reach the end.
    """
    # Convert input string to grid
    grid = input_map.strip().split('\n')
    rows, cols = len(grid), len(grid[0])
    
    # Find start and end positions
    start, end = find_start_end(grid)
    
    # BFS for shortest path
    queue = deque([(start, 0)])  # (position, steps)
    visited: Set[Tuple[int, int]] = {start}
    
    # Possible moves: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        (row, col), steps = queue.popleft()
        
        if (row, col) == end:
            return steps
        
        # Try all possible moves
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Check bounds and if the new position is valid
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                grid[new_row][new_col] != '#' and 
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append(((new_row, new_col), steps + 1))
    
    return -1  # No path found


def solution() -> int:
    """Read from stdin and return the answer."""
    input_data = sys.stdin.read()
    return shortest_path_without_cheats(input_data)