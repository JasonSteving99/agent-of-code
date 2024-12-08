"""Solution for the resonant collinearity problem."""
from collections import defaultdict
from typing import List, Set, Tuple, Dict


def count_antinodes(grid_str: str) -> int:
    """Count unique locations containing antinodes in the grid.
    
    Args:
        grid_str: String representation of the grid with antenna frequencies
        
    Returns:
        Number of unique antinode locations
    """
    # Parse the grid
    grid = [list(line) for line in grid_str.strip().splitlines()]
    height = len(grid)
    width = len(grid[0])
    
    # Collect antenna positions by frequency
    freq_positions: Dict[str, List[Tuple[int, int]]] = defaultdict(list)
    for y in range(height):
        for x in range(width):
            if grid[y][x] not in '.':
                freq_positions[grid[y][x]].append((x, y))
                
    # Find all antinodes
    antinodes: Set[Tuple[int, int]] = set()
    
    # For each frequency
    for freq, positions in freq_positions.items():
        # Check each pair of antennas with same frequency
        for i, (x1, y1) in enumerate(positions):
            for x2, y2 in positions[i + 1:]:
                # Calculate vector between antennas
                dx = x2 - x1
                dy = y2 - y1
                
                # Find both antinode positions
                for factor in (-0.5, 1.5):
                    antinode_x = int(x1 + (x1 + dx) * factor)
                    antinode_y = int(y1 + (y1 + dy) * factor)
                    
                    # Add antinode if it's within grid bounds
                    if (0 <= antinode_x < width and 
                        0 <= antinode_y < height):
                        antinodes.add((antinode_x, antinode_y))
    
    return len(antinodes)


def solution() -> int:
    """Read input from stdin and return the solution."""
    import sys
    input_data = sys.stdin.read()
    return count_antinodes(input_data)


if __name__ == "__main__":
    print(solution())