"""Solution for calculating unique antinode locations in an antenna grid."""
from typing import List, Set, Tuple
import sys


def get_antennas(grid: List[str]) -> List[Tuple[int, int, str]]:
    """Extract antenna positions and frequencies from the grid."""
    antennas = []
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != '.':
                antennas.append((x, y, char))
    return antennas


def find_antinodes(antennas: List[Tuple[int, int, str]], width: int, height: int) -> Set[Tuple[int, int]]:
    """Find all unique antinode locations within grid bounds."""
    antinodes: Set[Tuple[int, int]] = set()

    freq_groups = {}
    for x, y, freq in antennas:
        freq_groups.setdefault(freq, []).append((x, y))

    for freq, positions in freq_groups.items():
        if len(positions) < 2:
            continue

        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                dx = x2 - x1
                dy = y2 - y1

                for ratio in [1/3, 2/3]:
                    ax = int(x1 + dx * ratio)
                    ay = int(y1 + dy * ratio)

                    if 0 <= ax < width and 0 <= ay < height:
                        antinodes.add((ax, ay))

    return antinodes


def count_antinodes(grid_str: str) -> int:
    """Count unique antinode locations within the grid's boundaries."""
    grid = [line.strip() for line in grid_str.strip().split('\n')]
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0

    antennas = get_antennas(grid)
    antinodes = find_antinodes(antennas, width, height)

    return len(antinodes)


def solution() -> int:
    """Read input from stdin and return the solution."""
    grid_str = sys.stdin.read()
    return count_antinodes(grid_str)


if __name__ == "__main__":
    print(solution())