"""Day 8: Resonant Collinearity Part 2 Solution."""
from collections import defaultdict
from itertools import combinations
from typing import Dict, List, Set, Tuple


def parse_grid(grid_str: str) -> Tuple[Dict[str, List[Tuple[int, int]]], int, int]:
    """Parse the input grid into a dictionary mapping frequencies to their antenna positions."""
    lines = grid_str.strip().splitlines()
    rows, cols = len(lines), len(lines[0])
    
    # Map each frequency to list of its antenna positions
    freq_positions: Dict[str, List[Tuple[int, int]]] = defaultdict(list)
    
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != '.' and char != '#':
                freq_positions[char].append((i, j))
                
    return freq_positions, rows, cols


def is_collinear(p1: Tuple[int, int], p2: Tuple[int, int], p3: Tuple[int, int]) -> bool:
    """Check if three points are collinear."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    # Using cross product to check collinearity
    return (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)


def find_collinear_points(antenna_positions: List[Tuple[int, int]], rows: int, cols: int) -> Set[Tuple[int, int]]:
    """Find all points that are collinear with at least two antennas."""
    antinodes: Set[Tuple[int, int]] = set()

    if len(antenna_positions) < 2:
        return antinodes

    for i in range(rows):
        for j in range(cols):
            point = (i, j)

            # Check if this point is collinear with any pair of antennas
            for ant1, ant2 in combinations(antenna_positions, 2):
                if is_collinear(ant1, ant2, point):
                    antinodes.add(point)
                    break

    return antinodes


def count_harmonic_antinodes(grid: str) -> int:
    """Count unique antinode locations considering resonant harmonics within the grid boundaries."""
    freq_positions, rows, cols = parse_grid(grid)
    
    antinodes: Set[Tuple[int, int]] = set()
    
    # Process each frequency group separately
    for freq, positions in freq_positions.items():
        freq_antinodes = find_collinear_points(positions, rows, cols)        
        antinodes.update(freq_antinodes)

        # Add the antenna positions themselves as they're considered antinodes
        if len(positions) > 1:
            antinodes.update(positions)

    return len(antinodes)


def solution() -> int:
    """Read input from stdin and solve the problem."""
    from sys import stdin
    input_data = "".join(stdin.readlines())
    return count_harmonic_antinodes(input_data)


if __name__ == "__main__":
    print(solution())