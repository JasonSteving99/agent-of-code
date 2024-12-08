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

def is_collinear_with_ratio(p1: Tuple[int, int], p2: Tuple[int, int], p3: Tuple[int, int]) -> bool:
    """
    Returns True if p3 is collinear with p1 and p2, and the ratio of distances
    p3p1:p3p2 is 2:1 or 1:2
    """
    # Vector from p3 to p1
    v1 = (p1[0] - p3[0], p1[1] - p3[1])
    # Vector from p3 to p2
    v2 = (p2[0] - p3[0], p2[1] - p3[1])
    
    # Cross product should be 0 for collinearity
    cross_prod = v1[0] * v2[1] - v1[1] * v2[0]
    if cross_prod != 0:
        return False
    
    # Calculate distances squared
    d1_sq = v1[0] * v1[0] + v1[1] * v1[1]
    d2_sq = v2[0] * v2[0] + v2[1] * v2[1]
    
    # Check if ratio of distances is 2:1 or 1:2
    return 2 * d1_sq == d2_sq or d1_sq == 2 * d2_sq

def get_antinode(p1: Tuple[int, int], p2: Tuple[int, int]) -> Tuple[int, int]:
    """Returns the antinode position given two antenna positions."""
    # Antinode divides the line segment in ratio 2:1 or 1:2
    if 2 * abs(p1[0] - p2[0]) > abs(p2[0] - p1[0]):
        x = p1[0] + (p2[0] - p1[0]) * 2
        y = p1[1] + (p2[1] - p1[1]) * 2
    else:
        x = p2[0] + (p1[0] - p2[0]) * 2
        y = p2[1] + (p1[1] - p2[1]) * 2
    return (x, y)

def get_all_frequencies(grid: List[str]) -> Set[str]:
    """Returns set of all frequencies in the grid."""
    frequencies = set()
    for row in grid:
        for cell in row:
            if cell != '.':
                frequencies.add(cell)
    return frequencies

def count_antinodes(grid_str: str) -> int:
    # Convert input string to grid
    grid = grid_str.strip().split('\n')
    rows, cols = len(grid), len(grid[0])
    
    # Find all unique positions of antinodes
    antinodes = set()
    
    # For each frequency
    for freq in get_all_frequencies(grid):
        positions = get_positions_of_frequency(grid, freq)
        
        # For each pair of antennas with same frequency
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                p1, p2 = positions[i], positions[j]
                
                # For each point in grid that could be an antinode
                for x in range(-rows, rows * 2):
                    for y in range(-cols, cols * 2):
                        p3 = (x, y)
                        if is_collinear_with_ratio(p1, p2, p3):
                            # Only count antinodes within grid bounds
                            if 0 <= x < rows and 0 <= y < cols:
                                antinodes.add(p3)

    return len(antinodes)

def solution() -> int:
    """Read input from stdin and return result."""
    return count_antinodes(sys.stdin.read().strip())