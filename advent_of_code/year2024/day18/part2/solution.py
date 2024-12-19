"""Solution for finding first byte that blocks path to exit in corrupted memory grid."""
from collections import deque
from typing import Deque, List, Set, Tuple


def has_path_to_exit(blocked: Set[Tuple[int, int]], grid_size: int) -> bool:
    """
    Check if there is a path from start to exit given current blocked positions.
    
    Args:
        blocked: Set of blocked coordinates
        grid_size: Size of the grid
        
    Returns:
        True if path exists to exit, False otherwise
    """
    queue: Deque[Tuple[int, int]] = deque([(0, 0)])
    visited: Set[Tuple[int, int]] = {(0, 0)}
    
    # Possible moves: right, down, left, up
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    while queue:
        x, y = queue.popleft()
        
        if x == grid_size-1 and y == grid_size-1:
            return True
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            if (0 <= new_x < grid_size and 
                0 <= new_y < grid_size and 
                (new_x, new_y) not in visited and 
                (new_x, new_y) not in blocked):
                
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
    
    return False


def find_first_blocking_byte(input_str: str) -> str:
    """
    Find coordinates of first byte that blocks path to exit.
    
    Args:
        input_str: String containing coordinates of falling bytes
        
    Returns:
        String with coordinates of blocking byte in format "x,y"
    """
    # Convert input to list of coordinates
    corrupted: List[Tuple[int, int]] = []
    for line in input_str.strip().splitlines():
        x, y = map(int, line.split(','))
        corrupted.append((x, y))
    
    grid_size = 7  # Grid is 7x7 (0 to 6 inclusive) - changed from 71 to 7 for example
    blocked: Set[Tuple[int, int]] = set()
    
    # Check each byte in sequence
    for x, y in corrupted:
        # Add new byte
        blocked.add((x, y))
        
        # If path is blocked, this is the byte we're looking for
        if not has_path_to_exit(blocked, grid_size):
            return f"{x},{y}"
    
    # Should never reach here as problem guarantees a solution
    raise ValueError("No blocking byte found")


def solution() -> str:
    """Read input from stdin and return the solution."""
    import sys
    input_data = sys.stdin.read()
    return find_first_blocking_byte(input_data)