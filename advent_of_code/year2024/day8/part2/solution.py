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


def get_points_on_line(point1: Tuple[int, int], point2: Tuple[int, int], width: int, height: int) -> Set[Tuple[int, int]]:
    """Get all grid points that lie on the line segment between two points."""
    x1, y1 = point1
    x2, y2 = point2
    points = set()

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            points.add((x1, y))
    else:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
            if y.is_integer():
                y = int(y)
                if 0 <= y < height and is_collinear(point1, point2, (x, y)):
                    points.add((x, y))
    return points


def count_antinodes_harmonic(grid: str) -> int:
    """Count unique antinode locations within the grid bounds considering harmonics."""
    antinodes: Set[Tuple[int, int]] = set()
    rows = grid.strip().split('\n')
    height = len(rows)
    width = len(rows[0]) if rows else 0
    freq_coords = get_coordinates(grid)

    for freq, coords in freq_coords.items():
        if len(coords) >= 2:
            antinodes.update(coords)  # Antennas are antinodes if multiple exist
            for point1, point2 in combinations(coords, 2):
                line_points = get_points_on_line(point1, point2, width, height)
                antinodes.update(line_points)

    return len(antinodes)


def solution() -> int:
    """Read input from stdin and return result."""
    import sys
    grid = sys.stdin.read()
    return count_antinodes_harmonic(grid)