"""Solution for pipe maze maximum loop distance problem."""

from collections import deque
from typing import Dict, List, Set, Tuple


def max_loop_distance(grid_str: str) -> int:
    """Calculate maximum distance within pipe loop from start position.
    
    Args:
        grid_str: A string representing the grid layout with newlines
        
    Returns:
        Maximum distance within the loop from starting position
    """
    # Parse grid into 2D list
    grid = grid_str.strip().split('\n')
    rows, cols = len(grid), len(grid[0])

    # Find start position
    start_pos = None
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                start_pos = (i, j)
                break
        if start_pos:
            break

    # Handle case where no 'S' is found
    if start_pos is None:
        return 0 # Return 0 when no 'S' is found

    # Define valid connections for each pipe type
    connections = {
        '|': [(-1, 0), (1, 0)],   # North and South
        '-': [(0, -1), (0, 1)],   # West and East
        'L': [(-1, 0), (0, 1)],   # North and East
        'J': [(-1, 0), (0, -1)],  # North and West
        '7': [(1, 0), (0, -1)],   # South and West
        'F': [(1, 0), (0, 1)],    # South and East
        'S': [(-1, 0), (1, 0), (0, -1), (0, 1)]  # All directions initially
    }

    def is_valid(x: int, y: int) -> bool:
        """Check if position is within grid bounds."""
        return 0 <= x < rows and 0 <= y < cols

    def can_connect(from_pos: Tuple[int, int], to_pos: Tuple[int, int]) -> bool:
        """Check if two adjacent positions can form a valid pipe connection."""
        from_x, from_y = from_pos
        to_x, to_y = to_pos
        
        # Get the pipe types at both positions
        from_pipe = grid[from_x][from_y]
        to_pipe = grid[to_x][to_y]
        
        if from_pipe not in connections or to_pipe not in connections:
            return False
            
        # Get the direction vectors from both positions
        dx, dy = to_x - from_x, to_y - from_y
        reverse_dx, reverse_dy = -dx, -dy
        
        # Check if both pipes have compatible connections
        return (dx, dy) in connections[from_pipe] and (reverse_dx, reverse_dy) in connections[to_pipe]

    # BFS to find distances
    distances: Dict[Tuple[int, int], int] = {start_pos: 0}
    queue = deque([start_pos])
    visited: Set[Tuple[int, int]] = {start_pos}
    
    while queue:
        current = queue.popleft()
        curr_x, curr_y = current
        
        # Check all possible directions
        for dx, dy in connections[grid[curr_x][curr_y]]:
            next_x, next_y = curr_x + dx, curr_y + dy
            
            if (is_valid(next_x, next_y) and 
                (next_x, next_y) not in visited and 
                can_connect(current, (next_x, next_y))):
                
                distances[(next_x, next_y)] = distances[current] + 1
                visited.add((next_x, next_y))
                queue.append((next_x, next_y))

    # Return maximum distance in the loop
    return max(distances.values())


def solution() -> int:
    """Read input from stdin and return the solution."""
    import sys
    return max_loop_distance(sys.stdin.read())
