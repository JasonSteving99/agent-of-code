"""Calculate antinodes from antenna positions on a grid considering resonant harmonics."""
from typing import Dict, List, Set, Tuple


def get_coordinates(grid_str: str) -> Dict[str, List[Tuple[int, int]]]:
    """Extract coordinates for each frequency from grid string."""
    coords: Dict[str, List[Tuple[int, int]]] = {}
    rows = grid_str.strip().split('\n')

    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char != '.':
                if char not in coords:
                    coords[char] = []
                coords[char].append((x, y))

    return coords


def bresenham_line(p1: Tuple[int, int], p2: Tuple[int, int], width: int, height: int) -> Set[Tuple[int, int]]:
    """Generate points on the line segment between two points using Bresenham's algorithm."""
    x1, y1 = p1
    x2, y2 = p2
    points = set()
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    err = dx - dy

    while True:
        if 0 <= x1 < width and 0 <= y1 < height:
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


def get_collinear_points(points: List[Tuple[int, int]], width: int, height: int) -> Set[Tuple[int, int]]:
    """Get all collinear points between pairs of antennas within grid bounds."""
    antinodes: Set[Tuple[int, int]] = set()
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            antinodes.update(bresenham_line(points[i], points[j], width, height))
    return antinodes


def count_antinodes_harmonic(grid: str) -> int:
    """Count unique antinode locations within the grid bounds."""
    rows = grid.strip().split('\n')
    height = len(rows)
    width = len(rows[0])

    freq_coords = get_coordinates(grid)

    antinodes: Set[Tuple[int, int]] = set()

    for coords in freq_coords.values():
        antinodes.update(get_collinear_points(coords, width, height))

    return len(antinodes)


def solution() -> int:
    """Read input from stdin and return result."""
    import sys

    grid = sys.stdin.read()
    return count_antinodes_harmonic(grid)