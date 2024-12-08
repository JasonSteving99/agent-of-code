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


def are_collinear(p1: Tuple[int, int], p2: Tuple[int, int], p3: Tuple[int, int]) -> bool:
    """Check if three points are collinear using cross product."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    # Using the cross product method to check collinearity:
    # (y2-y1)(x3-x1) = (y3-y1)(x2-x1)
    return (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)


def get_collinear_points(points: List[Tuple[int, int]], width: int, height: int) -> Set[Tuple[int, int]]:
    """Get all points that are collinear with at least two antennas."""
    if len(points) < 2:
        return set()

    antinodes: Set[Tuple[int, int]] = set()
    
    # Check each point in the grid
    for y in range(height):
        for x in range(width):
            current = (x, y)
            # For each pair of antennas
            for i, p1 in enumerate(points):
                for p2 in points[i + 1:]:
                    if are_collinear(current, p1, p2):
                        antinodes.add(current)
                        break
                if current in antinodes:
                    break
                    
    return antinodes


def count_antinodes_harmonic(grid: str) -> int:
    """Count unique antinode locations within the grid bounds."""
    rows = grid.strip().split('\n')
    height = len(rows)
    width = len(rows[0])
    
    # Get coordinates for each frequency
    freq_coords = get_coordinates(grid)
    
    # Calculate all antinodes
    antinodes: Set[Tuple[int, int]] = set()
    
    # For each frequency
    for coords in freq_coords.values():
        # Add all points that are collinear with at least two antennas
        # of the same frequency
        antinodes.update(get_collinear_points(coords, width, height))

    return len(antinodes)


def solution() -> int:
    """Read input from stdin and return result."""
    import sys
    grid = sys.stdin.read()
    return count_antinodes_harmonic(grid)