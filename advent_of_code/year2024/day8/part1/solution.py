"""Solution for counting antinodes in antenna grid."""
from dataclasses import dataclass
import sys
from typing import Dict, List, Set, Tuple


@dataclass(frozen=True)
class Point:
    """Represents a point in 2D space."""
    x: int
    y: int


def parse_grid(input_str: str) -> Dict[str, List[Point]]:
    """Parse the input grid and return a dictionary of antenna frequencies and their locations."""
    antennas: Dict[str, List[Point]] = {}
    lines = input_str.strip().split('\n')
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append(Point(x, y))
                
    return antennas


def find_antinodes(a1: Point, a2: Point) -> Set[Point]:
    """Find antinodes for a pair of antennas with same frequency."""
    antinodes = set()
    
    # Vector from a1 to a2
    dx = a2.x - a1.x
    dy = a2.y - a1.y
    
    # Calculate antinode points
    # For antinode1: a1 is twice as far from antinode as a2
    # For antinode2: a2 is twice as far from antinode as a1
    
    # First antinode: extend a2->a1 by half
    antinode1_x = round(a2.x + dx / 2)
    antinode1_y = round(a2.y + dy / 2)
    antinodes.add(Point(antinode1_x, antinode1_y))
    
    # Second antinode: extend a1->a2 by half
    antinode2_x = round(a1.x - dx / 2)
    antinode2_y = round(a1.y - dy / 2)
    antinodes.add(Point(antinode2_x, antinode2_y))
    
    return antinodes


def is_in_bounds(point: Point, max_x: int, max_y: int) -> bool:
    """Check if a point is within the grid bounds."""
    return 0 <= point.x < max_x and 0 <= point.y < max_y


def count_antinodes(grid: str) -> int:
    """Count the total number of unique antinode locations."""
    lines = grid.strip().split('\n')
    height = len(lines)
    width = len(lines[0])
    
    # Parse the grid into a dictionary of frequencies and antenna locations
    antennas = parse_grid(grid)
    
    # Find all antinodes
    all_antinodes: Set[Point] = set()
    
    # For each frequency
    for frequency, antenna_points in antennas.items():
        # For each pair of antennas with the same frequency
        n = len(antenna_points)
        for i in range(n):
            for j in range(i + 1, n):
                antinodes = find_antinodes(antenna_points[i], antenna_points[j])
                # Only add antinodes that are within bounds
                for antinode in antinodes:
                    if is_in_bounds(antinode, width, height):
                        all_antinodes.add(antinode)
    
    return len(all_antinodes)


def solution() -> int:
    """Read input from stdin and return the solution."""
    input_data = sys.stdin.read()
    return count_antinodes(input_data)