"""Calculate the number of antinodes when taking harmonics into account."""
from typing import Dict, List, Set, Tuple
from collections import defaultdict


def get_coordinates(grid_str: str) -> Dict[str, List[Tuple[int, int]]]:
    """Extract coordinates for each frequency from grid string."""
    coords: Dict[str, List[Tuple[int, int]]] = defaultdict(list)
    rows = grid_str.strip().split('\n')
    
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char != '.':
                coords[char].append((x, y))
    
    return coords


def is_collinear(p1: Tuple[int, int], p2: Tuple[int, int], p3: Tuple[int, int]) -> bool:
    """Check if three points are collinear."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    # Using cross product to check collinearity
    return (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)


def get_points_on_line(p1: Tuple[int, int], p2: Tuple[int, int], width: int, height: int) -> List[Tuple[int, int]]:
    """Get all grid points that lie on the line between p1 and p2 within bounds."""
    points = []
    x1, y1 = p1
    x2, y2 = p2
    
    # If same point, return empty list
    if (x1, y1) == (x2, y2):
        return points
        
    # Handle vertical lines
    if x1 == x2:
        start_y = min(y1, y2)
        end_y = max(y1, y2)
        for y in range(start_y, end_y + 1):
            if 0 <= x1 < width and 0 <= y < height:
                points.append((x1, y))
        return points
    
    # Handle horizontal lines
    if y1 == y2:
        start_x = min(x1, x2)
        end_x = max(x1, x2)
        for x in range(start_x, end_x + 1):
            if 0 <= x < width and 0 <= y1 < height:
                points.append((x, y1))
        return points
        
    # Handle diagonal lines
    dx = x2 - x1
    dy = y2 - y1
    gcd = abs(dx)
    for i in range(abs(dy)):
        gcd = min(gcd, abs(dy))
        while gcd > 1:
            if dx % gcd == 0 and dy % gcd == 0:
                break
            gcd -= 1
            
    step_x = dx // gcd
    step_y = dy // gcd
    
    points = []
    for i in range(gcd + 1):
        x = x1 + i * step_x
        y = y1 + i * step_y
        if 0 <= x < width and 0 <= y < height:
            points.append((x, y))
            
    return points


def count_harmonic_antinodes(grid: str) -> int:
    """Count unique antinode locations within the grid bounds considering harmonics."""
    antinodes: Set[Tuple[int, int]] = set()
    rows = grid.strip().split('\n')
    height = len(rows)
    width = len(rows[0])

    freq_coords = get_coordinates(grid)

    # For each frequency
    for freq, coords in freq_coords.items():
        # If there's only one antenna of this frequency, skip
        if len(coords) < 2:
            continue
            
        # For each antenna
        for i, coord1 in enumerate(coords):
            # Add antenna position as antinode if there's another of same frequency
            antinodes.add(coord1)
            
            # Check collinearity with pairs of other antennas
            for j, coord2 in enumerate(coords[i+1:], i+1):
                # Add points on line between antennas
                line_points = get_points_on_line(coord1, coord2, width, height)
                antinodes.update(line_points)
                
                # Check if any other antennas are collinear with this pair
                for coord3 in coords[j+1:]:
                    if is_collinear(coord1, coord2, coord3):
                        # Add all points on the line that includes coord3
                        line_points = get_points_on_line(coord1, coord3, width, height)
                        antinodes.update(line_points)

    return len(antinodes)


def solution() -> int:
    """Read input from stdin and return result."""
    import sys
    grid = sys.stdin.read()
    return count_harmonic_antinodes(grid)