"""Calculate the number of antinodes in an antenna grid.

An antinode occurs when a point is in line with two antennas of the same frequency,
where one antenna is twice as far from the antinode as the other.
"""
from typing import List, Set, Tuple, Dict
from collections import defaultdict


def parse_grid(grid: str) -> List[List[str]]:
    """Convert string grid into 2D list."""
    return [list(line) for line in grid.strip().splitlines()]


def get_antenna_positions(grid: List[List[str]]) -> Dict[str, List[Tuple[int, int]]]:
    """Get positions of all antennas grouped by frequency."""
    antennas = defaultdict(list)
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != '.':
                antennas[char].append((x, y))
    return antennas


def is_in_bounds(point: Tuple[int, int], grid: List[List[str]]) -> bool:
    """Check if a point is within the grid boundaries."""
    return (0 <= point[0] < len(grid[0]) and 
            0 <= point[1] < len(grid))


def find_antinodes(ant1: Tuple[int, int], ant2: Tuple[int, int], grid: List[List[str]]) -> Set[Tuple[int, int]]:
    """Find antinodes for a pair of antennas with the same frequency."""
    x1, y1 = ant1
    x2, y2 = ant2
    antinodes = set()
    
    # Skip if antennas are at same position
    if (x1, y1) == (x2, y2):
        return antinodes
    
    # Check both directions for potential antinodes
    for direction in [-1, 1]:
        # Calculate antinode position
        # For any point P that divides the line between ant1 and ant2 in ratio 1:2
        dx = x2 - x1
        dy = y2 - y1
        
        # Antinode point is at 1/3 and 2/3 of the distance between antennas
        x_antinode = x1 + (dx * 2 // 3)
        y_antinode = y1 + (dy * 2 // 3)
        
        if is_in_bounds((x_antinode, y_antinode), grid):
            antinodes.add((x_antinode, y_antinode))
            
        x_antinode = x2 - (dx * 2 // 3)
        y_antinode = y2 - (dy * 2 // 3)
        
        if is_in_bounds((x_antinode, y_antinode), grid):
            antinodes.add((x_antinode, y_antinode))
    
    return antinodes


def count_antinodes(grid_str: str) -> int:
    """Count unique antinode locations in the grid."""
    grid = parse_grid(grid_str)
    antennas = get_antenna_positions(grid)
    all_antinodes = set()
    
    # For each frequency
    for freq, positions in antennas.items():
        # For each pair of antennas with same frequency
        for i, ant1 in enumerate(positions):
            for ant2 in positions[i+1:]:
                antinodes = find_antinodes(ant1, ant2, grid)
                all_antinodes.update(antinodes)
    
    return len(all_antinodes)


def solution() -> int:
    """Read input from stdin and return result."""
    import sys
    input_data = sys.stdin.read()
    return count_antinodes(input_data)