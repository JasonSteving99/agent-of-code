"""Calculate antinodes from resonant antennas considering harmonics."""
from collections import defaultdict
from itertools import combinations
from typing import List, Set, Tuple
import sys


def find_collinear_antinodes(p1: Tuple[int, int], p2: Tuple[int, int], max_rows: int, max_cols: int) -> Set[Tuple[int, int]]:
    """Find all grid points that are collinear with two given points within grid bounds."""
    antinodes = set()
    y1, x1 = p1
    y2, x2 = p2
    dx = x2 - x1
    dy = y2 - y1

    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    for x in range(max_cols):
        for y in range(max_rows):
            if dx == 0 and x == x1 and min_y <= y <= max_y:  # Handle vertical lines
                antinodes.add((y, x))
            elif dy == 0 and y == y1 and min_x <= x <= max_x:  # Handle horizontal lines
                antinodes.add((y, x))
            elif dx != 0 and dy != 0 and (y - y1) * dx == (x - x1) * dy and min_x <= x <= max_x and min_y <= y <= max_y:  # Handle diagonal lines
                antinodes.add((y, x))
    return antinodes


def get_grid_dimensions(grid: str) -> Tuple[int, int]:
    """Get the dimensions of the grid."""
    lines = grid.strip().split('\n')
    return len(lines), len(lines[0])


def get_antenna_positions(grid: str) -> dict:
    """Get positions of all antennas grouped by frequency."""
    lines = grid.strip().split('\n')
    antennas = defaultdict(list)
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != '.':
                antennas[char].append((y, x))
                
    return antennas


def count_harmonic_antinodes(input_grid: str) -> int:
    """Count unique antinode locations considering harmonics."""
    grid = input_grid.strip()
    rows, cols = get_grid_dimensions(grid)
    antennas = get_antenna_positions(grid)
    all_antinodes = set()

    # For each frequency
    for frequency, positions in antennas.items():
        # Skip if there's only one antenna of this frequency
        if len(positions) < 2:
            continue
            
        # Consider all pairs of antennas of the same frequency
        for ant1, ant2 in combinations(positions, 2):
            antinodes = find_collinear_antinodes(ant1, ant2, rows, cols)
            all_antinodes.update(antinodes)

    return len(all_antinodes)


def solution() -> int:
    """Read from stdin and return number of unique antinodes."""
    return count_harmonic_antinodes(sys.stdin.read())