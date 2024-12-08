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

    # Find collinear antennas within each frequency group
    for freq, coords in freq_groups.items():
        if len(coords) < 2:
            continue

        n = len(coords)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue

                    line_points = get_line_points(coords[j][0], coords[j][1], coords[k][0], coords[k][1])
                    if coords[i] in line_points:
                        antinodes.add(coords[i])
                        break # Antenna i forms a line with antennas j and k, no need to check further for i
                if coords[i] in antinodes:
                    break # No need to check any other starting point j for this i
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
    """Counts unique antinode locations."""
    points = parse_input(grid)
    antinodes = find_collinear_points(points)
    return len(antinodes)