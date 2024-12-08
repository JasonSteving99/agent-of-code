"""Module for calculating unique antinode locations in a signal map."""
from typing import List, Set, Tuple
from collections import defaultdict


def parse_grid(grid_str: str) -> List[List[str]]:
    """Parse the input grid string into a 2D list."""
    return [list(line) for line in grid_str.strip().splitlines()]


def get_antenna_positions(grid: List[List[str]], frequency: str) -> List[Tuple[int, int]]:
    """Get positions of antennas with the given frequency."""
    positions = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == frequency:
                positions.append((x, y))
    return positions


def is_collinear(p1: Tuple[int, int], p2: Tuple[int, int], p3: Tuple[int, int]) -> bool:
    """Check if three points are collinear."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)


def get_distance_squared(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    """Get squared distance between two points."""
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2


def find_antinodes(grid: List[List[str]], frequency: str) -> Set[Tuple[int, int]]:
    """Find all antinode positions for a given frequency."""
    antennas = get_antenna_positions(grid, frequency)
    antinodes = set()
    
    if len(antennas) < 2:
        return antinodes
        
    height = len(grid)
    width = len(grid[0])
    
    # Check each potential antinode position
    for y in range(height):
        for x in range(width):
            pos = (x, y)
            
            # Check all pairs of antennas
            for i, a1 in enumerate(antennas):
                for a2 in antennas[i + 1:]:
                    if not is_collinear(a1, a2, pos):
                        continue
                        
                    d1 = get_distance_squared(pos, a1)
                    d2 = get_distance_squared(pos, a2)
                    
                    # Check if one distance is twice the other
                    if d1 * 2 == d2 or d2 * 2 == d1:
                        antinodes.add(pos)
                        
    return antinodes


def count_antinodes(input_str: str) -> int:
    """Count total unique antinode locations in the map."""
    grid = parse_grid(input_str)
    
    # Get all frequencies (unique non-dot characters)
    frequencies = {c for row in grid for c in row if c != '.'}
    
    # Find antinodes for each frequency
    all_antinodes = set()
    for freq in frequencies:
        freq_antinodes = find_antinodes(grid, freq)
        all_antinodes.update(freq_antinodes)
    
    return len(all_antinodes)


def solution() -> int:
    """Read input from stdin and return result."""
    import sys
    return count_antinodes(sys.stdin.read())