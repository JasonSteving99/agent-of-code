"""Calculate antinodes according to harmonic rules."""
from typing import Set, Tuple, List
import sys

def is_collinear(p1: Tuple[int, int], p2: Tuple[int, int], p3: Tuple[int, int]) -> bool:
    """Checks if three points are collinear."""
    return (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) == 0

def get_positions_of_frequency(grid: List[str], freq: str) -> List[Tuple[int, int]]:
    """Returns list of (row, col) coordinates where given frequency appears."""
    return [(r, c) for r, row in enumerate(grid) for c, cell in enumerate(row) if cell == freq]

def get_all_frequencies(grid: List[str]) -> Set[str]:
    """Returns set of all frequencies in the grid."""
    return {cell for row in grid for cell in row if cell != '.'}

def get_antinodes_for_frequency(positions: List[Tuple[int, int]], rows: int, cols: int) -> Set[Tuple[int, int]]:
    """Returns all antinode positions for a set of positions with same frequency."""
    antinodes: Set[Tuple[int, int]] = set()
    for r in range(rows):
        for c in range(cols):
            count = 0
            for pos in positions:
                if is_collinear(positions[0], (r, c), pos):
                    count += 1
            if count >= 2:
                antinodes.add((r, c))
    return antinodes

def count_antinodes_harmonic(grid_str: str) -> int:
    """Count total antinodes based on harmonic rules."""
    grid = grid_str.strip().split('\n')
    rows, cols = len(grid), len(grid[0])
    antinodes: Set[Tuple[int, int]] = set()
    for freq in get_all_frequencies(grid):
        positions = get_positions_of_frequency(grid, freq)
        if len(positions) >= 2:
            antinodes.update(get_antinodes_for_frequency(positions, rows, cols))
    return len(antinodes)

def solution() -> int:
    """Read input from stdin and return result."""
    grid_str = sys.stdin.read()
    return count_antinodes_harmonic(grid_str)