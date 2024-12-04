"""Solution for the word search problem."""
from typing import List, Generator


def solution() -> int:
    """Read the grid from stdin and count XMAS occurrences."""
    grid = []
    while True:
        try:
            line = input().strip()
            if line:
                grid.append(line)
        except EOFError:
            break
    return count_xmas_occurrences('\n'.join(grid))


def count_xmas_occurrences(grid_str: str) -> int:
    """Count the number of times XMAS appears in the grid in all directions.
    
    Args:
        grid_str: A string containing the grid data with rows separated by newlines
        
    Returns:
        The total count of XMAS occurrences in all directions
    """
    # Convert grid string to list of strings
    grid = [list(line) for line in grid_str.strip().split('\n')]
    rows, cols = len(grid), len(grid[0])
    target = "XMAS"
    count = 0
    
    def get_sequences(x: int, y: int) -> Generator[str, None, None]:
        """Generate all possible sequences of 4 characters from given position."""
        # Right
        if y <= cols - 4:
            yield ''.join(grid[x][y:y+4])
        
        # Down
        if x <= rows - 4:
            yield ''.join(grid[i][y] for i in range(x, x+4))
        
        # Diagonal down-right
        if x <= rows - 4 and y <= cols - 4:
            yield ''.join(grid[x+i][y+i] for i in range(4))
        
        # Diagonal down-left
        if x <= rows - 4 and y >= 3:
            yield ''.join(grid[x+i][y-i] for i in range(4))
        
        # Left
        if y >= 3:
            yield ''.join(reversed(grid[x][y-3:y+1]))
        
        # Up
        if x >= 3:
            yield ''.join(reversed([grid[i][y] for i in range(x-3, x+1)]))
        
        # Diagonal up-right
        if x >= 3 and y <= cols - 4:
            yield ''.join(reversed([grid[x-i][y+i] for i in range(4)]))
        
        # Diagonal up-left
        if x >= 3 and y >= 3:
            yield ''.join(reversed([grid[x-i][y-i] for i in range(4)]))

    # Check all positions in the grid
    for i in range(rows):
        for j in range(cols):
            for sequence in get_sequences(i, j):
                if sequence == target:
                    count += 1
                    
    return count