"""Calculates antinodes based on resonant harmonics between antennas."""

from collections import defaultdict
from typing import List, Set, Tuple


def points_on_line(p1: Tuple[int, int], p2: Tuple[int, int]) -> Set[Tuple[int, int]]:
    """Returns all points that lie on a line between two points using Bresenham's line algorithm."""
    x1, y1 = p1
    x2, y2 = p2
    points = set()

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.add((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    return points


def get_grid_dimensions(grid: str) -> Tuple[int, int]:
    """Returns width and height of the grid."""
    lines = grid.strip().split('\n')
    return len(lines[0]), len(lines)


def get_antennas_by_freq(grid: str) -> dict:
    """Returns a dictionary of antenna frequencies mapping to their coordinates."""
    antennas = defaultdict(list)
    lines = grid.strip().split('\n')
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != '.':
                antennas[char].append((x, y))
                
    return antennas


def count_antinodes_harmonic(grid: str) -> int:
    """
    Calculates the number of unique antinode locations considering resonant harmonics.
    An antinode occurs at any grid position exactly in line with at least two antennas 
    of the same frequency, regardless of distance.
    """
    width, height = get_grid_dimensions(grid)
    antinodes: Set[Tuple[int, int]] = set()
    antennas_by_freq = get_antennas_by_freq(grid)
    
    # For each frequency and its antennas
    for freq, positions in antennas_by_freq.items():
        if len(positions) < 2:
            continue
            
        # Check all pairs of antennas of the same frequency
        for i, pos1 in enumerate(positions):
            for j, pos2 in enumerate(positions[i+1:], i+1):
                # Get all points on the line between these two antennas
                line_points = points_on_line(pos1, pos2)
                
                # Only keep points within grid bounds
                valid_points = {(x, y) for x, y in line_points 
                              if 0 <= x < width and 0 <= y < height}
                
                antinodes.update(valid_points)
                
    return len(antinodes)


def solution() -> int:
    """Read input from stdin and return the solution."""
    import sys
    return count_antinodes_harmonic(sys.stdin.read().strip())