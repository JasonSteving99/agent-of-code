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

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if 0 <= y < height:
                points.append((x1, y))
        return points

    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if 0 <= x < width:
                points.append((x, y1))
        return points

    dx = x2 - x1
    dy = y2 - y1
    
    for i in range(max(abs(dx), abs(dy)) + 1):
        x = x1 + (i * dx) // max(abs(dx), abs(dy))
        y = y1 + (i * dy) // max(abs(dx), abs(dy))
        if 0 <= x < width and 0 <= y < height:            
            points.append((x,y))
            
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