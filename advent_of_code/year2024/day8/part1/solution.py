"""
Count antinodes in a grid based on antenna positions and frequencies.

An antinode occurs at a point that is collinear with two antennas of the same frequency 
where one antenna is twice as far from the point as the other.
"""
from typing import Dict, List, Set, Tuple
from collections import defaultdict
import math

def get_antennas(grid: str) -> Dict[str, List[Tuple[int, int]]]:
    """Parse grid to get antenna positions by frequency."""
    antennas = defaultdict(list)
    for y, line in enumerate(grid.strip().splitlines()):
        for x, char in enumerate(line):
            if char != '.':
                antennas[char].append((x, y))
    return antennas

def is_twice_distance(p1: Tuple[int, int], p2: Tuple[int, int], 
                     p3: Tuple[int, int]) -> bool:
    """Check if p2 is twice as far from p1 as p3 is from p1."""
    d1 = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    d2 = math.sqrt((p3[0] - p1[0])**2 + (p3[1] - p1[1])**2)
    return abs(d1 - 2*d2) < 1e-10 or abs(d2 - 2*d1) < 1e-10

def are_collinear(p1: Tuple[int, int], p2: Tuple[int, int], 
                  p3: Tuple[int, int]) -> bool:
    """Check if three points are collinear."""
    # Using the area of triangle formed by three points
    area = p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])
    return abs(area) < 1e-10

def find_antinode(p1: Tuple[int, int], p2: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Find antinodes for two antennas of same frequency."""
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dist = math.sqrt(dx*dx + dy*dy)
    
    # Unit vector perpendicular to line between antennas
    if dist == 0:
        return []
    perp_x = -dy/dist
    perp_y = dx/dist
    
    # Points at 1/2 and 2x distance along perpendicular lines
    antinodes = []
    for factor in [-1, 1]:
        for ratio in [0.5, 2.0]:
            mid_x = (p1[0] + p2[0])/2
            mid_y = (p1[1] + p2[1])/2
            antinode_x = round(mid_x + factor * dist * ratio * perp_x)
            antinode_y = round(mid_y + factor * dist * ratio * perp_y)
            antinodes.append((antinode_x, antinode_y))
    
    return antinodes

def get_grid_bounds(grid: str) -> Tuple[int, int]:
    """Get width and height of grid."""
    lines = grid.strip().splitlines()
    return len(lines[0]), len(lines)

def count_antinodes(grid: str) -> int:
    """Count unique antinode locations within grid bounds."""
    width, height = get_grid_bounds(grid)
    antennas = get_antennas(grid)
    antinodes: Set[Tuple[int, int]] = set()
    
    # Find antinodes for each pair of same-frequency antennas
    for freq, positions in antennas.items():
        for i, p1 in enumerate(positions):
            for p2 in positions[i+1:]:
                # Find potential antinodes
                for antinode in find_antinode(p1, p2):
                    x, y = antinode
                    if 0 <= x < width and 0 <= y < height:
                        # Verify this is a valid antinode
                        if are_collinear(p1, p2, antinode) and \
                           is_twice_distance(antinode, p1, p2):
                            antinodes.add(antinode)
    
    return len(antinodes)

def solution() -> int:
    """Read input from stdin and solve the problem."""
    import sys
    grid = sys.stdin.read()
    return count_antinodes(grid)

if __name__ == "__main__":
    print(solution())