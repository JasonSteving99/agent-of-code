"""Solution for a grid-based antinode counting problem."""
from collections import defaultdict
from typing import Dict, List, Set, Tuple


def solution() -> int:
    """Read input from stdin and return the solution.
    
    Returns:
        int: Number of unique antinode locations
    """
    import sys
    input_text = sys.stdin.read().strip()
    return count_antinodes(input_text)


def get_antenna_positions(grid: List[str]) -> Dict[str, List[Tuple[int, int]]]:
    """Extract positions of all antennas by frequency.
    
    Args:
        grid: List of strings representing the grid
        
    Returns:
        Dict mapping frequency to list of (row, col) positions
    """
    positions = defaultdict(list)
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            char = grid[row][col]
            if char != '.':
                positions[char].append((row, col))
    return positions


def find_antinodes(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> Set[Tuple[int, int]]:
    """Find antinode positions for two antennas of same frequency.
    
    Args:
        pos1: (row, col) of first antenna
        pos2: (row, col) of second antenna
        
    Returns:
        Set of (row, col) antinode positions
    """
    r1, c1 = pos1
    r2, c2 = pos2
    
    # Vector from antenna 1 to antenna 2
    dr = r2 - r1
    dc = c2 - c1
    
    # Find antinode positions at 1/2 and 2x distances
    antinodes = set()
    
    # Mid antinode (antenna 2 is twice as far from antinode as antenna 1)
    antinode1 = (r1 - dr//2, c1 - dc//2)
    
    # Far antinode (antenna 1 is twice as far from antinode as antenna 2) 
    antinode2 = (r2 + dr, c2 + dc)
    
    antinodes.add(antinode1)
    antinodes.add(antinode2)
    
    return antinodes


def count_antinodes(input_text: str) -> int:
    """Count unique antinode locations in the grid.
    
    An antinode occurs at points collinear with two antennas of same frequency,
    where one antenna is twice as far from the antinode as the other.
    
    Args:
        input_text: String containing grid representation
        
    Returns:
        Number of unique antinode locations within grid bounds
    """
    # Parse grid
    grid = [line for line in input_text.strip().split('\n')]
    height = len(grid)
    width = len(grid[0])
    
    # Get antenna positions by frequency
    antenna_positions = get_antenna_positions(grid)
    
    # Find all antinodes
    all_antinodes = set()
    for freq, positions in antenna_positions.items():
        # Check all pairs of antennas with same frequency
        for i in range(len(positions)):
            pos1 = positions[i]
            for j in range(i + 1, len(positions)):
                pos2 = positions[j]
                antinodes = find_antinodes(pos1, pos2)
                
                # Only keep antinodes within grid bounds
                for antinode in antinodes:
                    r, c = antinode
                    if 0 <= r < height and 0 <= c < width:
                        all_antinodes.add(antinode)
    
    return len(all_antinodes)