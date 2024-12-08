"""Day 8: Resonant Collinearity Solution."""
from collections import defaultdict
from typing import Dict, List, Set, Tuple


def parse_grid(grid_str: str) -> Tuple[Dict[str, List[Tuple[int, int]]], int, int]:
    """Parse the input grid into a dictionary mapping frequencies to their antenna positions."""
    lines = grid_str.strip().splitlines()
    rows, cols = len(lines), len(lines[0])
    
    # Map each frequency to list of its antenna positions
    freq_positions: Dict[str, List[Tuple[int, int]]] = defaultdict(list)
    
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != '.':
                freq_positions[char].append((i, j))
                
    return freq_positions, rows, cols


def find_antinodes(antenna1: Tuple[int, int], antenna2: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Find antinode positions for a pair of antennas of the same frequency."""
    y1, x1 = antenna1
    y2, x2 = antenna2

    dy = y2 - y1
    dx = x2 - x1

    antinodes = []

    for mult in [-1, 2]:
        ay = y1 + dy * mult
        ax = x1 + dx * mult

        if ay.is_integer() and ax.is_integer():
            antinodes.append((int(ay), int(ax)))

    return antinodes


def count_antinodes(grid: str) -> int:
    """Count unique antinode locations within the grid boundaries."""
    freq_positions, rows, cols = parse_grid(grid)
    
    antinodes: Set[Tuple[int, int]] = set()
    
    for freq, positions in freq_positions.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                pair_antinodes = find_antinodes(positions[i], positions[j])
                
                for y, x in pair_antinodes:
                    if 0 <= y < rows and 0 <= x < cols:
                        antinodes.add((y, x))
    
    return len(antinodes)


def solution() -> int:
    """Read input from stdin and solve the problem."""
    from sys import stdin
    input_data = "".join(stdin.readlines())
    return count_antinodes(input_data)

if __name__ == "__main__":
    print(solution())
