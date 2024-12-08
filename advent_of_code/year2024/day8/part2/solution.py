"""Calculate antinodes according to harmonic rules."""
from typing import Set, Tuple, List
import sys

def is_collinear(p1: Tuple[int, int], p2: Tuple[int, int], p3: Tuple[int, int]) -> bool:
    """Checks if three points are collinear."""
    # Calculate vectors
    v1 = (p1[0] - p3[0], p1[1] - p3[1])
    v2 = (p2[0] - p3[0], p2[1] - p3[1])
    
    # Cross product should be 0 for collinearity
    cross_prod = v1[0] * v2[1] - v1[1] * v2[0]
    return cross_prod == 0

def get_positions_of_frequency(grid: List[str], freq: str) -> List[Tuple[int, int]]:
    """Returns list of (row, col) coordinates where given frequency appears."""
    positions = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == freq:
                positions.append((i, j))
    return positions

def get_all_frequencies(grid: List[str]) -> Set[str]:
    """Returns set of all frequencies in the grid."""
    frequencies = set()
    for row in grid:
        for cell in row:
            if cell != '.':
                frequencies.add(cell)
    return frequencies

def get_antinodes_for_frequency(positions: List[Tuple[int, int]], rows: int, cols: int) -> Set[Tuple[int, int]]:
    """Returns all antinode positions for a set of positions with same frequency."""
    antinodes = set()
    
    # For each position in the grid
    for i in range(rows):
        for j in range(cols):
            point = (i, j)
            # Count how many antennas this point is collinear with
            collinear_count = 0
            collinear_antennas = set()
            
            # For each antenna pair
            for p1 in positions:
                for p2 in positions:
                    if p1 != p2 and is_collinear(p1, p2, point):
                        collinear_antennas.add(p1)
                        collinear_antennas.add(p2)
            
            # If point is collinear with at least 2 antennas, it's an antinode
            if len(collinear_antennas) >= 2:
                antinodes.add(point)
    
    return antinodes

def count_antinodes_harmonic(grid_str: str) -> int:
    """Count total antinodes based on harmonic rules."""
    # Convert input string to grid
    grid = grid_str.strip().split('\n')
    rows, cols = len(grid), len(grid[0])
    
    # Find all unique antinode positions
    antinodes = set()
    
    # For each frequency
    for freq in get_all_frequencies(grid):
        positions = get_positions_of_frequency(grid, freq)
        if len(positions) >= 2:  # Only consider frequencies with at least 2 antennas
            antinodes.update(get_antinodes_for_frequency(positions, rows, cols))
            
    return len(antinodes)

def solution() -> int:
    """Read input from stdin and return result."""
    return count_antinodes_harmonic(sys.stdin.read().strip())