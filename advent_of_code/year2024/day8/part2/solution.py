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

def get_all_frequencies(grid: List[str]) -> Set[str]:
    """Returns set of all frequencies in the grid."""
    frequencies = set()
    for row in grid:
        for cell in row:
            if cell != '.':
                frequencies.add(cell)
    return frequencies

def are_collinear(p1: Tuple[int, int], p2: Tuple[int, int], p3: Tuple[int, int]) -> bool:
    """Returns True if three points are exactly collinear."""
    # Calculate cross product of vectors
    # (x2-x1)(y3-y1) - (y2-y1)(x3-x1) = 0 for collinear points
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) == (p2[1] - p1[1]) * (p3[0] - p1[0])

def get_line_points(p1: Tuple[int, int], p2: Tuple[int, int], rows: int, cols: int) -> Set[Tuple[int, int]]:
    """Returns all grid points that lie on the line between p1 and p2 (inclusive)."""
    points = set()
    # Add endpoints
    points.add(p1)
    points.add(p2)
    
    # Check all grid points between min and max coordinates
    min_x = min(p1[0], p2[0])
    max_x = max(p1[0], p2[0])
    min_y = min(p1[1], p2[1])
    max_y = max(p1[1], p2[1])
    
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if 0 <= x < rows and 0 <= y < cols:
                point = (x, y)
                if are_collinear(p1, p2, point):
                    points.add(point)
    
    return points

def count_part2_antinodes(grid_str: str) -> int:
    # Convert input string to grid
    grid = grid_str.strip().split('\n')
    rows, cols = len(grid), len(grid[0])
    
    # Find all unique positions of antinodes
    antinodes = set()
    
    # For each frequency
    for freq in get_all_frequencies(grid):
        positions = get_positions_of_frequency(grid, freq)
        
        # If there's only one antenna of this frequency, it doesn't create antinodes
        if len(positions) < 2:
            continue
            
        # For each pair of antennas with same frequency
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                p1, p2 = positions[i], positions[j]
                
                # Get all points on the line between these antennas
                line_points = get_line_points(p1, p2, rows, cols)
                antinodes.update(line_points)
                
                # Any third antenna that's collinear with these two creates
                # additional antinodes along their line
                for k in range(len(positions)):
                    if k != i and k != j:
                        p3 = positions[k]
                        if are_collinear(p1, p2, p3):
                            antinodes.update(get_line_points(p1, p3, rows, cols))
                            antinodes.update(get_line_points(p2, p3, rows, cols))

    return len(antinodes)

def solution() -> int:
    """Read input from stdin and return result."""
    return count_part2_antinodes(sys.stdin.read().strip())