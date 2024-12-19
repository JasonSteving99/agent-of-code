"""Solution for finding minimum steps to exit in corrupted memory grid."""
from collections import deque
from typing import Deque, List, Set, Tuple


def min_steps_to_exit(input_str: str) -> int:
    """
    Calculate minimum steps needed to reach exit in memory grid.
    
    Args:
        input_str: String containing coordinates of falling bytes
        
    Returns:
        Minimum number of steps needed to reach exit
    """
    # Convert input to list of coordinates
    corrupted: List[Tuple[int, int]] = []
    for line in input_str.strip().splitlines():
        x, y = map(int, line.split(','))
        corrupted.append((x, y))
    
    # Set grid size to 71x71 (coordinates 0-70)
    SIZE = 71
    
    # Take only first 1024 bytes
    corrupted = corrupted[:1024]
    
    # Create set of corrupted coordinates for O(1) lookup
    blocked: Set[Tuple[int, int]] = set(corrupted)
    
    # BFS to find shortest path
    queue: Deque[Tuple[int, int, int]] = deque([(0, 0, 0)])  # (x, y, steps)
    visited: Set[Tuple[int, int]] = {(0, 0)}
    
    # Possible moves: right, down, left, up
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    while queue:
        x, y, steps = queue.popleft()
        
        # Check if reached exit
        if x == SIZE-1 and y == SIZE-1:
            return steps
        
        # Try all possible moves
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            # Check if move is valid:
            # - Within grid bounds
            # - Not visited
            # - Not corrupted
            if (0 <= new_x < SIZE and 
                0 <= new_y < SIZE and 
                (new_x, new_y) not in visited and 
                (new_x, new_y) not in blocked):
                
                queue.append((new_x, new_y, steps + 1))
                visited.add((new_x, new_y))
    
    # If no path found, return -1 (though problem guarantees solution exists)
    return -1


def solution() -> int:
    """Read input from stdin and return the solution."""
    import sys
    input_data = sys.stdin.read()
    return min_steps_to_exit(input_data)