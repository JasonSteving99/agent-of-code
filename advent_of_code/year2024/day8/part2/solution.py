"""Solution for Day 8 Part 2 - Resonant Collinearity."""
from typing import List, Set, Dict, Tuple
import sys
import collections

def parse_grid(grid_str: str) -> List[List[str]]:
    """Parse input grid into a 2D array."""
    return [list(line) for line in grid_str.splitlines()]

def get_coordinates(grid: List[List[str]]) -> Dict[str, List[Tuple[int, int]]]:
    """Get coordinates of all antennas by frequency."""
    freqs: Dict[str, List[Tuple[int, int]]] = collections.defaultdict(list)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            char = grid[i][j]
            if char.isalnum():  # Only process alphanumeric characters
                # Convert uppercase to lowercase to treat them as same frequency
                freq = char.lower()
                freqs[freq].append((i, j))
    return freqs

def is_collinear(p1: Tuple[int, int], p2: Tuple[int, int], p3: Tuple[int, int]) -> bool:
    """Determine if three points are collinear."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    # Using slope method to check collinearity
    # (y2-y1)*(x3-x2) = (y3-y2)*(x2-x1)
    return (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)

def find_collinear_points(points: List[Tuple[int, int]], grid_height: int, grid_width: int) -> Set[Tuple[int, int]]:
    """Find all points that are collinear with at least two antennas."""
    antinodes: Set[Tuple[int, int]] = set()
    
    # If we have fewer than 2 points, there can't be any antinodes
    if len(points) < 2:
        return antinodes
    
    # Add antenna positions as antinodes (as per part 2 rules)
    antinodes.update(points)
    
    # Check all possible grid positions
    for i in range(grid_height):
        for j in range(grid_width):
            current = (i, j)
            # Skip if this point is already known to be an antinode
            if current in antinodes:
                continue
            
            # Check if this point is collinear with any two antennas
            for k in range(len(points)):
                for l in range(k + 1, len(points)):
                    if is_collinear(points[k], current, points[l]):
                        antinodes.add(current)
                        # Once we find a collinear set, we can stop checking this point
                        break
                if current in antinodes:
                    break
                    
    return antinodes

def count_part2_antinodes(grid_str: str) -> int:
    """Count the total number of unique antinode locations in part 2."""
    # Parse the grid
    grid = parse_grid(grid_str)
    height = len(grid)
    width = len(grid[0])
    
    # Get coordinates grouped by frequency
    freq_coords = get_coordinates(grid)
    
    # Find all antinodes for each frequency
    all_antinodes: Set[Tuple[int, int]] = set()
    for coords in freq_coords.values():
        antinodes = find_collinear_points(coords, height, width)
        all_antinodes.update(antinodes)
    
    return len(all_antinodes)

def solution() -> int:
    """Read from stdin and solve the problem."""
    input_data = sys.stdin.read().strip()
    return count_part2_antinodes(input_data)

if __name__ == "__main__":
    print(solution())