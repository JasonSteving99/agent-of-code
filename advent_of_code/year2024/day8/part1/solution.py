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
    
    # Calculate vector from antenna1 to antenna2
    dy = y2 - y1
    dx = x2 - x1
    
    # Each antenna pair produces two antinodes - one on each side
    antinodes = []
    
    # Calculate positions that are half the distance from antenna1
    # and twice the distance from antenna2
    for mult in [1/2, 3/2]:  # These multipliers give us points on both sides
        antinode_y = y1 + dy * mult
        antinode_x = x1 + dx * mult
        
        # Only add if the coordinates are integers
        if antinode_y.is_integer() and antinode_x.is_integer():
            antinodes.append((int(antinode_y), int(antinode_x)))
            
    return antinodes


def count_antinodes(grid: str) -> int:
    """Count unique antinode locations within the grid boundaries."""
    freq_positions, rows, cols = parse_grid(grid)
    
    # Set to store unique antinode positions
    antinodes: Set[Tuple[int, int]] = set()
    
    # For each frequency
    for freq, positions in freq_positions.items():
        # For each pair of antennas with the same frequency
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                # Find antinodes for this pair
                pair_antinodes = find_antinodes(positions[i], positions[j])
                
                # Add antinodes that are within grid boundaries
                for pos in pair_antinodes:
                    y, x = pos
                    if 0 <= y < rows and 0 <= x < cols:
                        antinodes.add(pos)
    
    return len(antinodes)


def solution() -> int:
    """Read input from stdin and solve the problem."""
    from sys import stdin
    input_data = "".join(stdin.readlines())
    return count_antinodes(input_data)

if __name__ == "__main__":
    print(solution())