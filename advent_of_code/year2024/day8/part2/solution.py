from typing import Set, Tuple, List
import sys

def get_positions_of_frequency(grid: List[str], freq: str) -> List[Tuple[int, int]]:
    """Returns list of (row, col) coordinates where given frequency appears."""
    positions = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == freq:
                positions.append((i, j))
    return positions

def get_all_frequencies(grid: List[str]) -> Set[str]:
    """Returns set of all frequencies in the grid."""
    frequencies = set()
    for row in grid:
        for cell in row:
            if cell != '.':
                frequencies.add(cell)
    return frequencies

def are_collinear(p1: Tuple[int, int], p2: Tuple[int, int], p3: Tuple[int, int]) -> bool:
    """Returns True if three points are exactly collinear."""
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) == (p2[1] - p1[1]) * (p3[0] - p1[0])

def get_line_points(p1: Tuple[int, int], p2: Tuple[int, int], rows: int, cols: int) -> Set[Tuple[int, int]]:
    """Returns all grid points that lie on the line between p1 and p2 (inclusive)."""
    points = set()
    if p1 == p2:
        points.add(p1)
        return points

    if p1[0] == p2[0]:  # Vertical line
        for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
            if 0 <= y < cols:
                points.add((p1[0], y))
    elif p1[1] == p2[1]:  # Horizontal line
        for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
            if 0 <= x < rows:
                points.add((x, p1[1]))
    else:  # Diagonal line
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        for i in range(abs(dx) + 1):
            x = p1[0] + i * (1 if dx > 0 else -1)
            y = p1[1] + i * (1 if dy > 0 else -1)
            if 0 <= x < rows and 0 <= y < cols:
                points.add((x, y))

    return points

def count_part2_antinodes(grid_str: str) -> int:
    grid = grid_str.strip().split('\n')
    rows, cols = len(grid), len(grid[0])
    antinodes = set()
    for freq in get_all_frequencies(grid):
        positions = get_positions_of_frequency(grid, freq)
        if len(positions) < 2:
            continue
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                p1, p2 = positions[i], positions[j]
                line_points = get_line_points(p1, p2, rows, cols)
                antinodes.update(line_points)
    return len(antinodes)

def solution() -> int:
    return count_part2_antinodes(sys.stdin.read().strip())