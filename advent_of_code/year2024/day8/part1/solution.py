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
    
    dx = x2 - x1
    dy = y2 - y1
    
    # Calculate distances from the first antenna to potential antinode positions
    d1x = -dx // 2  # for the first antinode
    d1y = -dy // 2
    
    d2x = dx * 2  # for the second antinode
    d2y = dy * 2
    
    # Calculate the actual positions of the antinodes
    antinodes = {
        (x1 + d1x, y1 + d1y),  # antinode before the antennas
        (x2 + d2x, y2 + d2y)   # antinode after the antennas
    }
    
    return antinodes


def count_antinodes(input_data: str) -> int:
    """Count unique antinode locations within the grid boundaries."""
    grid = parse_grid(input_data)
    height = len(grid)
    width = len(grid[0])
    
    # Get all antenna positions grouped by frequency
    antennas = find_antennas(grid)
    
    # Set to store all valid antinode positions
    antinodes: Set[Tuple[int, int]] = set()
    
    # For each frequency group
    for freq, positions in antennas.items():
        # For each pair of antennas with the same frequency
        for ant1, ant2 in combinations(positions, 2):
            # Calculate antinode positions for this pair
            new_antinodes = calc_antinode_positions(ant1, ant2)
            
            # Add only the antinodes that are within grid boundaries
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