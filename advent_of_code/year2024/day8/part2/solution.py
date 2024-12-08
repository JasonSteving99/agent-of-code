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


def get_collinear_points(points: List[Tuple[int, int]], width: int, height: int) -> Set[Tuple[int, int]]:
    """Get all collinear points between pairs of antennas within grid bounds."""
    if len(points) < 2:
        return set()
    
    antinodes: Set[Tuple[int, int]] = set()
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            
            # Calculate all points on the line segment between (x1, y1) and (x2, y2)
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            
            if dx == 0:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    if 0 <= x1 < width and 0 <= y < height:
                        antinodes.add((x1, y))
            elif dy == 0:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    if 0 <= x < width and 0 <= y1 < height:
                        antinodes.add((x, y1))
            else:  # Handle diagonal lines
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    y = y1 + (y2 - y1) * (x - x1) // (x2 - x1)  # Integer division ensures correct y-values for collinear points
                    if 0 <= x < width and 0 <= y < height:
                        antinodes.add((x, y))
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