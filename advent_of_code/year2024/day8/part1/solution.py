"""Solution for calculating unique antinode locations in an antenna grid."""
from typing import List, Set, Tuple
import sys


def get_antennas(grid: List[str]) -> List[Tuple[int, int, str]]:
    """Extract antenna positions and frequencies from the grid."""
    antennas = []
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char not in '.':  # Not empty space
                antennas.append((x, y, char))
    return antennas


def find_antinodes(antennas: List[Tuple[int, int, str]], width: int, height: int) -> Set[Tuple[int, int]]:
    """Find all unique antinode locations within grid bounds."""
    antinodes = set()
    
    # Group antennas by frequency
    freq_groups = {}
    for x, y, freq in antennas:
        if freq not in freq_groups:
            freq_groups[freq] = []
        freq_groups[freq].append((x, y))
    
    # For each frequency group with at least 2 antennas
    for freq, positions in freq_groups.items():
        if len(positions) < 2:
            continue
            
        # Check every pair of antennas with same frequency
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                
                # Vector from first to second antenna
                dx = x2 - x1
                dy = y2 - y1
                
                # Calculate antinode positions (1/3 and 2/3 points on the line)
                for ratio in [1/3, 2/3]:
                    antinode_x = x1 + dx * ratio
                    antinode_y = y1 + dy * ratio
                    
                    # Only count if antinode has integer coordinates and is within bounds
                    if (antinode_x.is_integer() and antinode_y.is_integer() and 
                        0 <= antinode_x < width and 0 <= antinode_y < height):
                        antinodes.add((int(antinode_x), int(antinode_y)))
    
    return antinodes


def count_antinodes(grid_str: str) -> int:
    """Count unique antinode locations within the grid's boundaries."""
    # Parse grid
    grid = [line.strip() for line in grid_str.strip().split('\n')]
    height = len(grid)
    width = len(grid[0])
    
    # Get antenna positions and find antinodes
    antennas = get_antennas(grid)
    antinodes = find_antinodes(antennas, width, height)
    
    return len(antinodes)


def solution() -> int:
    """Read input from stdin and return the solution."""
    return count_antinodes(sys.stdin.read())


if __name__ == "__main__":
    print(solution())