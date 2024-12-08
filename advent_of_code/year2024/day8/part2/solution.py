"""
Solution for Part 2 of the resonant collinearity problem.
Calculates antinodes based on harmonic resonance between antennas.
"""
from collections import defaultdict
from itertools import combinations
from typing import List, Set, Tuple, Dict


def get_line_points(x1: int, y1: int, x2: int, y2: int) -> Set[Tuple[int, int]]:
    """Returns all points that lie on a straight line between two points (inclusive)."""
    points = set()
    points.add((x1, y1))
    points.add((x2, y2))
    
    dx = x2 - x1
    dy = y2 - y1
    
    # Handle vertical lines
    if dx == 0:
        y_min, y_max = min(y1, y2), max(y1, y2)
        for y in range(y_min, y_max + 1):
            points.add((x1, y))
        return points
    
    # Handle horizontal lines
    if dy == 0:
        x_min, x_max = min(x1, x2), max(x1, x2)
        for x in range(x_min, x_max + 1):
            points.add((x, y1))
        return points
    
    # Handle diagonal lines
    if abs(dx) == abs(dy):
        step_x = 1 if dx > 0 else -1
        step_y = 1 if dy > 0 else -1
        steps = abs(dx)
        for i in range(steps + 1):
            points.add((x1 + i * step_x, y1 + i * step_y))
        return points
    
    return points


def find_collinear_points(points: List[Tuple[int, int, str]]) -> Set[Tuple[int, int]]:
    """Find all points that are collinear with at least two antennas of the same frequency."""
    freq_groups: Dict[str, List[Tuple[int, int]]] = defaultdict(list)
    antinodes = set()
    
    # Group points by frequency
    for x, y, freq in points:
        freq_groups[freq].append((x, y))
    
    # Process each frequency group
    for freq_points in freq_groups.values():
        if len(freq_points) < 3:  # Need at least 3 points for collinearity to create antinode
            continue
            
        for x, y in freq_points:
            is_antinode = False
            for x1, y1 in freq_points:
                for x2, y2 in freq_points:
                    if (x, y) != (x1, y1) and (x,y) != (x2, y2) and (x1, y1) != (x2, y2) \
                        and (x, y) in get_line_points(x1, y1, x2, y2):
                            is_antinode = True
                            break
                if is_antinode:
                    break
            if is_antinode:
                antinodes.add((x, y))

    return antinodes


def parse_input(grid: str) -> List[Tuple[int, int, str]]:
    """Parse the input grid into a list of antenna positions with frequencies."""
    points = []
    for y, line in enumerate(grid.strip().split('\n')):
        for x, char in enumerate(line):
            if char != '.':
                points.append((x, y, char))
    return points


def count_harmonic_antinodes(grid: str) -> int:
    """
    Count the number of unique antinode locations in the grid,
    considering harmonic resonance between antennas.
    
    Args:
        grid: String representation of the antenna grid
    
    Returns:
        Number of unique antinode locations
    """
    # Parse input into list of antenna positions with frequencies
    points = parse_input(grid)
    
    # Find all collinear points
    antinodes = find_collinear_points(points)
    
    return len(antinodes)