"""Calculate antinodes according to harmonic rules."""
from typing import Set, Tuple, List
import sys

def is_collinear(p1: Tuple[int, int], p2: Tuple[int, int], p3: Tuple[int, int]) -> bool:
    """Checks if three points are collinear horizontally, vertically, or diagonally."""
    if (p1[0] == p2[0] == p3[0]) or (p1[1] == p2[1] == p3[1]):
        return True
    return abs((p2[1] - p1[1]) * (p3[0] - p2[0])) == abs((p3[1] - p2[1]) * (p2[0] - p1[0]))

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
            for i in range(len(positions)):
                for j in range(i + 1, len(positions)):
                    if is_collinear(positions[i], positions[j], (r, c)):
                        antinodes.add((r, c))
                        break  # Inner loop can break early
                else:
                    continue  # Only executed if the inner loop did NOT break
                break  # Outer loop can break early
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