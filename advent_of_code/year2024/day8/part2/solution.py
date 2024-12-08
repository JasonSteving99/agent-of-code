"""Solution for Part 2 of the Resonant Collinearity problem."""
from typing import List, Set, Tuple
import sys
from collections import defaultdict


def get_positions(grid: List[str]) -> defaultdict[str, List[Tuple[int, int]]]:
    """Extract positions of each frequency from the grid."""
    positions = defaultdict(list)
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char.isalnum():
                # Treat uppercase and lowercase as same frequency
                freq = char.lower()
                positions[freq].append((x, y))
    return positions


def get_all_points_on_line(p1: Tuple[int, int], p2: Tuple[int, int], 
                          max_x: int, max_y: int) -> Set[Tuple[int, int]]:
    """Get all grid points that lie on the line between p1 and p2, inclusive."""
    points = set()
    x1, y1 = p1
    x2, y2 = p2
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    err = (dx if dx > dy else -dy) // 2

    while True:
        if 0 <= x1 < max_x and 0 <= y1 < max_y:
            points.add((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = err
        if e2 > -dx:
            err -= dy
            x1 += sx
        if e2 < dy:
            err += dx
            y1 += sy
    return points


def count_part2_antinodes(input_data: str) -> int:
    """
    Count the number of unique antinode positions in the grid according to part 2 rules.
    An antinode occurs at any position inline with at least two antennas of the same frequency.
    """
    # Parse the grid
    grid = [line for line in input_data.strip().splitlines()]
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

        # Check all combinations of two points
        for i, p1 in enumerate(pos_list):
            for j, p2 in enumerate(pos_list[i + 1:], i + 1):
                # Add all points on the line between these two antennas
                antinodes.update(get_all_points_on_line(p1, p2, width, height))

    return len(antinodes)


def solution() -> int:
    """Read from stdin and solve the problem."""
    return count_part2_antinodes(sys.stdin.read())


if __name__ == "__main__":
    print(solution())
