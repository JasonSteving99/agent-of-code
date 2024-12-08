from typing import Dict, List, Set, Tuple
import sys


def get_antennas_by_frequency(grid: List[str]) -> Dict[str, List[Tuple[int, int]]]:
    """Extract antenna positions by frequency from the grid."""
    antennas: Dict[str, List[Tuple[int, int]]] = {}
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != '.':
                if cell not in antennas:
                    antennas[cell] = []
                antennas[cell].append((i, j))
    return antennas


def is_valid_point(point: Tuple[int, int], grid: List[str]) -> bool:
    """Check if a point is within grid boundaries."""
    rows, cols = len(grid), len(grid[0])
    return 0 <= point[0] < rows and 0 <= point[1] < cols


def find_antinodes(p1: Tuple[int, int], p2: Tuple[int, int], grid: List[str]) -> List[Tuple[int, int]]:
    """Find antinode positions for two antennas of same frequency."""
    antinodes = []
    
    # Vector from p1 to p2
    dy = p2[0] - p1[0]
    dx = p2[1] - p1[1]

    for multiplier in [-1, 1]:
        # Calculate antinode positions based on proportional distances (2/3 and 1/3)
        antinode1_r = p1[0] + (2 * dy) // 3
        antinode1_c = p1[1] + (2 * dx) // 3
        antinode1 = (int(antinode1_r), int(antinode1_c))

        antinode2_r = p1[0] + dy // 3
        antinode2_c = p1[1] + dx // 3
        antinode2 = (int(antinode2_r), int(antinode2_c))


        if is_valid_point(antinode1, grid):
            antinodes.append(antinode1)
        if is_valid_point(antinode2, grid):
            antinodes.append(antinode2)
            
    return antinodes


def count_antinodes(input_data: str) -> int:
    """
    Count unique antinode locations in the grid based on antenna frequencies and positions.
    
    Args:
        input_data: A string representation of the grid with antennas.
        
    Returns:
        The number of unique antinode locations within the grid boundaries.
    """
    grid = [line.strip() for line in input_data.strip().split('\n')]
    antennas_by_freq = get_antennas_by_frequency(grid)
    antinodes: Set[Tuple[int, int]] = set()

    for freq, positions in antennas_by_freq.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                new_antinodes = find_antinodes(positions[i], positions[j], grid)
                antinodes.update(new_antinodes)

    return len(antinodes)


def solution() -> int:
    """Read input from stdin and solve the problem."""
    input_data = sys.stdin.read()
    return count_antinodes(input_data)
