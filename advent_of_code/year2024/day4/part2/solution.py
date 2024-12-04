"""Module to solve part 2 of the word search problem."""
from typing import List, Iterator
import sys

def make_grid(input_str: str) -> List[List[str]]:
    """Convert input string into a 2D grid."""
    return [list(line.strip()) for line in input_str.splitlines() if line.strip()]

def in_bounds(grid: List[List[str]], x: int, y: int) -> bool:
    """Check if coordinates are within grid bounds."""
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def check_mas(grid: List[List[str]], x: int, y: int, dx: int, dy: int) -> bool:
    """Check if MAS sequence exists starting at x,y in direction dx,dy."""
    if not all(in_bounds(grid, x + i * dx, y + i * dy) for i in range(3)):
        return False
    chars = [grid[y + i * dy][x + i * dx] for i in range(3)]
    return chars == ['M', 'A', 'S']


def get_xmas_patterns(grid: List[List[str]], x: int, y: int) -> List[tuple[tuple[int, int, int, int], tuple[int, int, int, int]]]:
    """Get all possible X-MAS patterns centered at x,y."""
    # Directions for possible MAS sequences
    directions = [
        (-1, -1), (1, -1),  # Upper diagonal directions
        (-1, 1), (1, 1),    # Lower diagonal directions
    ]

    patterns = []
    for dx1, dy1 in directions[:2]:
        for dx2, dy2 in directions[2:]:
            if (check_mas(grid, x + dx1, y + dy1, dx1, dy1) and
                    check_mas(grid, x + dx2, y + dy2, dx2, dy2)):
                patterns.append(((dx1, dy1, dx1, dy1), (dx2, dy2, dx2, dy2)))

    return patterns

def count_xmas(input_str: str) -> int:
    """Count number of X-MAS patterns in the grid."""
    grid = make_grid(input_str)
    if not grid:
        return 0

    height, width = len(grid), len(grid[0])
    total = 0

    # For each possible center point
    for y in range(height):
        for x in range(width):
            # Get all valid X-MAS patterns centered at this point
            patterns = get_xmas_patterns(grid, x, y)
            total += len(patterns)

    return total

def solution() -> int:
    """Read from stdin and return the solution."""
    return count_xmas(sys.stdin.read())
