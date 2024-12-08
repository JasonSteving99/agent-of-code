"""Calculate antinodes from antenna positions on a grid."""
from collections import defaultdict
from typing import Dict, List, Set, Tuple


def get_coordinates(grid_str: str) -> Dict[str, List[Tuple[int, int]]]:
    """Extract coordinates for each frequency from grid string."""
    coords: Dict[str, List[Tuple[int, int]]] = defaultdict(list)
    rows = grid_str.strip().split('\n')
    
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char != '.':
                coords[char].append((x, y))
    
    return coords


def get_antinode_positions(coord1: Tuple[int, int], coord2: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Calculate antinode positions for a pair of same-frequency antennas."""
    x1, y1 = coord1
    x2, y2 = coord2
    
    if (x1, y1) == (x2, y2):
        return []

    dx = x2 - x1
    dy = y2 - y1

    antinode1 = (x1 - dx, y1 - dy)
    antinode2 = (x2 + dx, y2 + dy)
    
    return [antinode1, antinode2]


def count_antinodes(grid: str) -> int:
    """Count unique antinode locations within the grid bounds."""
    antinodes: Set[Tuple[int, int]] = set()
    rows = grid.strip().split('\n')
    height = len(rows)
    width = len(rows[0])

    freq_coords = get_coordinates(grid)

    for freq, coords in freq_coords.items():
        for i, coord1 in enumerate(coords):
            for coord2 in coords[i+1:]:
                new_antinodes = get_antinode_positions(coord1, coord2)

                for antinode in new_antinodes:
                    x, y = antinode
                    if 0 <= x < width and 0 <= y < height:
                        antinodes.add(antinode)

    return len(antinodes)


def solution() -> int:
    """Read input from stdin and return result."""
    import sys
    grid = sys.stdin.read()
    return count_antinodes(grid)