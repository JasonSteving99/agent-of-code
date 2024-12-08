"""Calculate antinodes from antenna positions on a grid considering resonant harmonics."""
from collections import defaultdict
from itertools import combinations
from typing import Dict, List, Set, Tuple


def get_coordinates(grid_str: str) -> Dict[str, List[Tuple[int, int]]]:
    """Extract coordinates for each frequency from grid string."""
    coords: Dict[str, List[Tuple[int, int]]] = defaultdict(list)
    rows = grid_str.strip().split('\n')

    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char != '.':
                coords[char].append((x, y))
    return coords


def is_collinear(point1: Tuple[int, int], point2: Tuple[int, int], point3: Tuple[int, int]) -> bool:
    """Check if three points are collinear using the area method."""
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    return (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0


def get_points_on_line(point1: Tuple[int, int], point2: Tuple[int, int]) -> Set[Tuple[int, int]]:
    """Get all grid points that lie on the line segment between two points using Bresenham's line algorithm."""
    x1, y1 = point1
    x2, y2 = point2
    points = set()
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    err = dx - dy

    x, y = x1, y1
    while True:
        points.add((x, y))
        if x == x2 and y == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy

    return points


def count_antinodes_harmonic(grid: str) -> int:
    """Count unique antinode locations within the grid bounds considering harmonics."""
    antinodes: Set[Tuple[int, int]] = set()
    freq_coords = get_coordinates(grid)

    for freq, coords in freq_coords.items():
        if len(coords) >= 2:
            antinodes.update(coords)  # Antennas are antinodes if multiple exist
            for point1, point2 in combinations(coords, 2):
                line_points = get_points_on_line(point1, point2)
                antinodes.update(line_points)
    return len(antinodes)


def solution() -> int:
    """Read input from stdin and return result."""
    import sys

    grid = sys.stdin.read()
    return count_antinodes_harmonic(grid)