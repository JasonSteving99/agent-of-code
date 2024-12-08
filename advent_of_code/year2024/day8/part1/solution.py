"""Day 8: Count unique antinodes locations based on resonant frequencies."""
from typing import List, Set, Tuple
import sys
from itertools import combinations


def parse_grid(data: str) -> List[List[str]]:
    """Parse the input string into a 2D grid."""
    return [list(line.strip()) for line in data.splitlines()]


def find_antennas(grid: List[List[str]]) -> dict[str, List[Tuple[int, int]]]:
    """Find all antenna positions grouped by frequency."""
    antennas = {}
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas


def calc_antinode_positions(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> Set[Tuple[int, int]]:
    """Calculate the antinode positions for a pair of antennas."""
    x1, y1 = pos1
    x2, y2 = pos2

    antinodes = {
        (round(2 * x1 - 0.5 * x2), round(2 * y1 - 0.5 * y2)),
        (round(2 * x2 - 0.5 * x1), round(2 * y2 - 0.5 * y1)),
    }
    return antinodes


def count_antinodes(input_data: str) -> int:
    """Count unique antinode locations within the grid boundaries."""
    grid = parse_grid(input_data)
    height = len(grid)
    width = len(grid[0])

    antennas = find_antennas(grid)
    antinodes: Set[Tuple[int, int]] = set()

    for freq, positions in antennas.items():
        for ant1, ant2 in combinations(positions, 2):
            new_antinodes = calc_antinode_positions(ant1, ant2)
            for x, y in new_antinodes:
                if 0 <= x < width and 0 <= y < height:
                    antinodes.add((x, y))

    return len(antinodes)


def solution() -> int:
    """Read input from stdin and return the solution."""
    input_data = sys.stdin.read()
    return count_antinodes(input_data)


if __name__ == "__main__":
    print(solution())