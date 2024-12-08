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


def is_collinear(point1: Tuple[int, int], point2: Tuple[int, int], 
                 point3: Tuple[int, int]) -> bool:
    """Check if three points are collinear."""
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    
    # Calculate the area of the triangle formed by the three points
    # If area is 0, points are collinear
    area = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
    return abs(area) == 0


def get_points_on_line(point1: Tuple[int, int], point2: Tuple[int, int], 
                      width: int, height: int) -> Set[Tuple[int, int]]:
    """Get all grid points that lie on the line between two points."""
    x1, y1 = point1
    x2, y2 = point2
    points = {(x1, y1), (x2, y2)}
    
    # For each point in the grid bounds
    for x in range(width):
        for y in range(height):
            if (x, y) != point1 and (x, y) != point2:
                if is_collinear(point1, point2, (x, y)):
                    # Check if point lies between the two endpoints
                    if (min(x1, x2) <= x <= max(x1, x2) and 
                        min(y1, y2) <= y <= max(y1, y2)):
                        points.add((x, y))
    
    return points


def count_antinodes_harmonic(grid: str) -> int:
    """Count unique antinode locations within the grid bounds considering harmonics."""
    antinodes: Set[Tuple[int, int]] = set()
    rows = grid.strip().split('\n')
    height = len(rows)
    width = len(rows[0])

    freq_coords = get_coordinates(grid)

    # For each frequency
    for freq, coords in freq_coords.items():
        # If there's more than one antenna of this frequency
        if len(coords) >= 2:
            # Add all antenna positions as antinodes (since they're collinear with others)
            antinodes.update(coords)
            
            # For each pair of antennas
            for point1, point2 in combinations(coords, 2):
                # Get all points that lie on the line between these antennas
                line_points = get_points_on_line(point1, point2, width, height)
                antinodes.update(line_points)

    return len(antinodes)


def solution() -> int:
    """Read input from stdin and return result."""
    import sys
    grid = sys.stdin.read()
    return count_antinodes_harmonic(grid)