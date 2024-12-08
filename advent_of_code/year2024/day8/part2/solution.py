"""Calculate the number of antinodes when taking harmonics into account."""
from typing import Dict, List, Set, Tuple
from collections import defaultdict


def get_coordinates(grid_str: str) -> Dict[str, List[Tuple[int, int]]]:
    """Extract coordinates for each frequency from grid string."""
    coords: Dict[str, List[Tuple[int, int]]] = defaultdict(list)
    rows = grid_str.strip().split('\n')
    
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char != '.':
                coords[char].append((x, y))
    
    return coords


def get_points_on_line(p1: Tuple[int, int], p2: Tuple[int, int], width: int, height: int) -> List[Tuple[int, int]]:
    """Get all grid points that lie on the line between p1 and p2 within bounds."""
    points = []
    x1, y1 = p1
    x2, y2 = p2

    if (x1,y1) == (x2, y2):
        return points

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    err = dx - dy    
    x, y = x1, y1

    while True:
        if 0 <= x < width and 0 <= y < height:
            points.append((x, y))
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


def count_harmonic_antinodes(grid: str) -> int:
    """Count unique antinode locations within the grid bounds considering harmonics."""
    antinodes: Set[Tuple[int, int]] = set()
    rows = grid.strip().split('\n')
    height = len(rows)
    width = len(rows[0])
    freq_coords = get_coordinates(grid)

    for freq, coords in freq_coords.items():
        if len(coords) < 2:
            continue

        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                line_points = get_points_on_line(coords[i], coords[j], width, height)
                antinodes.update(line_points)

    return len(antinodes)


def solution() -> int:
    """Read input from stdin and return result."""
    import sys
    grid = sys.stdin.read()
    return count_harmonic_antinodes(grid)