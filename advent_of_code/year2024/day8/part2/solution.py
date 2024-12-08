"""Solution for Part 2 - Count inline antinodes across grid lines."""
from dataclasses import dataclass
from collections import defaultdict
from typing import Dict, List, Set, Tuple


@dataclass(frozen=True)
class Point:
    """Represents a 2D point."""
    x: int
    y: int


def get_grid_dimensions(grid: str) -> Tuple[int, int]:
    """Get dimensions of input grid."""
    lines = grid.strip().splitlines()
    return len(lines[0]), len(lines)


def parse_antenna_positions(grid: str) -> Dict[str, List[Point]]:
    """Parse grid into mapping of frequencies to their antenna positions."""
    lines = grid.strip().splitlines()
    antennas = defaultdict(list)
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char.isalnum():  # Consider only alphanumeric characters
                # Normalize frequencies - uppercase = lowercase
                freq = char.lower()
                antennas[freq].append(Point(x, y))
                
    return antennas


def get_inline_points(p1: Point, p2: Point, width: int, height: int) -> Set[Point]:
    """Get all points that lie on the straight line between two points."""
    points = set()
    
    # Handle vertical line
    if p1.x == p2.x:
        start, end = min(p1.y, p2.y), max(p1.y, p2.y)
        points.update(Point(p1.x, y) for y in range(start, end + 1))
        return points
    
    # Handle horizontal line
    if p1.y == p2.y:
        start, end = min(p1.x, p2.x), max(p1.x, p2.x)
        points.update(Point(x, p1.y) for x in range(start, end + 1))
        return points
        
    # Handle diagonal line
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    
    # Check if line is diagonal at 45 degrees
    if abs(dx) == abs(dy):
        step_x = 1 if dx > 0 else -1
        step_y = 1 if dy > 0 else -1
        
        x, y = p1.x, p1.y
        while True:
            points.add(Point(x, y))
            if x == p2.x:
                break
            x += step_x
            y += step_y
    
    return points


def count_part2_antinodes(grid: str) -> int:
    """
    Count unique antinode positions in the grid based on part 2 rules.
    An antinode occurs at any point inline with two antennas of same frequency.
    """
    width, height = get_grid_dimensions(grid)
    antennas = parse_antenna_positions(grid)
    antinodes = set()
    
    # For each frequency
    for positions in antennas.values():
        # Need at least 2 antennas of same frequency
        if len(positions) < 2:
            continue
            
        # Check all pairs of antennas with same frequency
        for i, p1 in enumerate(positions):
            for p2 in positions[i + 1:]:
                # All points inline between these antennas are antinodes
                inline_points = get_inline_points(p1, p2, width, height)
                antinodes.update(inline_points)
    
    return len(antinodes)


def solution() -> int:
    """Read from stdin and return result."""
    import sys
    return count_part2_antinodes(sys.stdin.read())