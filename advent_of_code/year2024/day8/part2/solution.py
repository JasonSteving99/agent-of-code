"""Solution for Part 2 of the Resonant Collinearity problem."""
from typing import List, Set, Tuple
import sys
from collections import defaultdict


def get_positions(grid: List[str]) -> defaultdict[str, List[Tuple[int, int]]]:
    """Extract positions of each frequency from the grid."""
    positions = defaultdict(list)
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != '\n':
                # Treat uppercase and lowercase as same frequency
                freq = char.lower()
                positions[freq].append((x, y))
    return positions


def is_collinear(p1: Tuple[int, int], p2: Tuple[int, int], p3: Tuple[int, int]) -> bool:
    """Check if three points are collinear using cross product method."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    # Using cross product: (x2-x1)(y3-y1) - (y2-y1)(x3-x1) = 0 for collinear points
    return (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1)


def get_all_points_on_line(p1: Tuple[int, int], p2: Tuple[int, int], 
                          max_x: int, max_y: int) -> Set[Tuple[int, int]]:
    """Get all grid points that lie on the line between p1 and p2, inclusive."""
    points = set()
    x1, y1 = p1
    x2, y2 = p2
    
    if x1 == x2:  # Vertical line
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if 0 <= x1 < max_x and 0 <= y < max_y:
                points.add((x1, y))
    elif y1 == y2:  # Horizontal line
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if 0 <= x < max_x and 0 <= y1 < max_y:
                points.add((x, y1))
    else:  # Diagonal line
        dx = x2 - x1
        dy = y2 - y1
        steps = max(abs(dx), abs(dy))
        
        for i in range(steps + 1):
            x = x1 + (dx * i) // steps
            y = y1 + (dy * i) // steps
            if 0 <= x < max_x and 0 <= y < max_y:
                points.add((x, y))
    
    return points


def count_part2_antinodes(input_data: str) -> int:
    """
    Count the number of unique antinode positions in the grid according to part 2 rules.
    An antinode occurs at any position inline with at least two antennas of the same frequency.
    """
    # Parse the grid
    grid = [line.strip() for line in input_data.strip().splitlines()]
    height = len(grid)
    width = len(grid[0])
    
    # Get positions of each frequency
    positions = get_positions(grid)
    
    # Set to store all antinode positions
    antinodes = set()
    
    # For each frequency
    for freq, pos_list in positions.items():
        # Need at least 2 antennas of the same frequency
        if len(pos_list) < 2:
            continue
            
        # Add antenna positions themselves as antinodes (if more than one of same frequency)
        if len(pos_list) > 1:
            antinodes.update(pos_list)
        
        # Check all combinations of three points
        for i, p1 in enumerate(pos_list):
            for j, p2 in enumerate(pos_list[i+1:], i+1):
                # Add all points on the line between these two antennas
                antinodes.update(get_all_points_on_line(p1, p2, width, height))

    return len(antinodes)


def solution() -> int:
    """Read from stdin and solve the problem."""
    return count_part2_antinodes(sys.stdin.read())


if __name__ == "__main__":
    print(solution())