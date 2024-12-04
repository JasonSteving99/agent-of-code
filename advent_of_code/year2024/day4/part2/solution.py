"""Advent of Code Solution - X-MAS word search counter."""
from typing import List, Iterator
import sys

def check_xmas_patterns(grid: List[List[str]], row: int, col: int) -> bool:
    """Check if there's an X-MAS pattern centered at the given position."""
    if len(grid) < 3 or len(grid[0]) < 3:
        return False
    
    # Check bounds
    if row < 1 or col < 1 or row >= len(grid) - 1 or col >= len(grid[0]) - 1:
        return False
    
    # Check center position has 'A'
    if grid[row][col] != 'A':
        return False
        
    # Check the four possible X-MAS arrangements:
    patterns = [
        # MAS in top-right to bottom-left, MAS in top-left to bottom-right
        (lambda: grid[row-1][col+1] == 'M' and grid[row][col] == 'A' and grid[row+1][col-1] == 'S' and
         grid[row-1][col-1] == 'M' and grid[row][col] == 'A' and grid[row+1][col+1] == 'S'),
        
        # SAM in top-right to bottom-left, MAS in top-left to bottom-right
        (lambda: grid[row-1][col+1] == 'S' and grid[row][col] == 'A' and grid[row+1][col-1] == 'M' and
         grid[row-1][col-1] == 'M' and grid[row][col] == 'A' and grid[row+1][col+1] == 'S'),
        
        # MAS in top-right to bottom-left, SAM in top-left to bottom-right
        (lambda: grid[row-1][col+1] == 'M' and grid[row][col] == 'A' and grid[row+1][col-1] == 'S' and
         grid[row-1][col-1] == 'S' and grid[row][col] == 'A' and grid[row+1][col+1] == 'M'),
        
        # SAM in top-right to bottom-left, SAM in top-left to bottom-right
        (lambda: grid[row-1][col+1] == 'S' and grid[row][col] == 'A' and grid[row+1][col-1] == 'M' and
         grid[row-1][col-1] == 'S' and grid[row][col] == 'A' and grid[row+1][col+1] == 'M')
    ]
    
    return any(pattern() for pattern in patterns)

def count_xmas(grid_str: str) -> int:
    """Count the number of X-MAS patterns in the grid."""
    # Convert the input string to a 2D grid
    grid = [list(line) for line in grid_str.strip().split('\n')]
    
    count = 0
    # Check each position that could be the center of an X-MAS pattern
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if check_xmas_patterns(grid, row, col):
                count += 1
                
    return count

def solution() -> int:
    """Read from stdin and return the solution."""
    return count_xmas(sys.stdin.read().strip())

if __name__ == "__main__":
    print(solution())