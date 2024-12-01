from typing import List, Tuple, Set
import sys
from itertools import combinations

def find_empty_rows_and_columns(grid: List[str]) -> Tuple[Set[int], Set[int]]:
    """Find rows and columns that have no galaxies."""
    empty_rows = {i for i in range(len(grid)) if '#' not in grid[i]}
    empty_cols = {j for j in range(len(grid[0])) if all(grid[i][j] == '.' for i in range(len(grid)))}
    return empty_rows, empty_cols

def get_galaxy_positions(grid: List[str]) -> List[Tuple[int, int]]:
    """Get all galaxy positions in the grid."""
    positions = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                positions.append((i, j))
    return positions

def calculate_manhattan_distance(pos1: Tuple[int, int], pos2: Tuple[int, int], 
                              empty_rows: Set[int], empty_cols: Set[int]) -> int:
    """Calculate Manhattan distance accounting for expanded universe."""
    row1, col1 = pos1
    row2, col2 = pos2
    
    # Get regular manhattan distance
    base_distance = abs(row1 - row2) + abs(col1 - col2)
    
    # Add extra distance for empty rows between points
    min_row, max_row = min(row1, row2), max(row1, row2)
    extra_rows = sum(1 for r in empty_rows if min_row < r < max_row)
    
    # Add extra distance for empty columns between points
    min_col, max_col = min(col1, col2), max(col1, col2)
    extra_cols = sum(1 for c in empty_cols if min_col < c < max_col)
    
    return base_distance + extra_rows + extra_cols

def calculate_sum_of_shortest_paths(input_str: str) -> int:
    """
    Calculate the sum of shortest paths between all pairs of galaxies in an expanded universe.
    
    Args:
        input_str: A string representing the universe map with '.' for empty space and '#' for galaxies
    
    Returns:
        The sum of the shortest paths between all pairs of galaxies
    """
    # Convert input string to grid
    grid = input_str.strip().split('\n')
    
    # Find empty rows and columns
    empty_rows, empty_cols = find_empty_rows_and_columns(grid)
    
    # Get all galaxy positions
    galaxy_positions = get_galaxy_positions(grid)
    
    # Calculate sum of shortest paths for all pairs
    total_distance = 0
    for pos1, pos2 in combinations(galaxy_positions, 2):
        distance = calculate_manhattan_distance(pos1, pos2, empty_rows, empty_cols)
        total_distance += distance
        
    return total_distance

def solution() -> int:
    """Read input from stdin and solve the problem."""
    input_str = sys.stdin.read()
    return calculate_sum_of_shortest_paths(input_str)

if __name__ == "__main__":
    print(solution())