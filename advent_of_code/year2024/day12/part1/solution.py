"""Solution for Garden Groups puzzle."""
from collections import deque
from dataclasses import dataclass
from typing import Dict, List, Set, Tuple

@dataclass
class Region:
    """Represents a region of connected garden plots."""
    symbol: str
    coords: Set[Tuple[int, int]]
    area: int = 0
    perimeter: int = 0

def get_adjacent_coords(coord: Tuple[int, int], max_rows: int, max_cols: int) -> List[Tuple[int, int]]:
    """Get valid adjacent coordinates (up, down, left, right)."""
    row, col = coord
    adjacent = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < max_rows and 0 <= new_col < max_cols:
            adjacent.append((new_row, new_col))
    return adjacent

def find_region(grid: List[List[str]], start: Tuple[int, int], visited: Set[Tuple[int, int]]) -> Region:
    """Find a complete region starting from given coordinates using BFS."""
    symbol = grid[start[0]][start[1]]
    region = Region(symbol=symbol, coords=set())
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
            
        visited.add(current)
        region.coords.add(current)
        region.area += 1
        
        # Check adjacent cells
        for adj in get_adjacent_coords(current, len(grid), len(grid[0])):
            if grid[adj[0]][adj[1]] == symbol and adj not in visited:
                queue.append(adj)
    
    # Calculate perimeter
    perimeter = 0
    for coord in region.coords:
        for adj in get_adjacent_coords(coord, len(grid), len(grid[0])):
            if adj not in region.coords:
                perimeter += 1
    
    region.perimeter = perimeter
    return region

def calculate_total_fence_price(garden_map: str) -> str:
    """Calculate the total price for fencing all regions in the garden map."""
    # Convert input string to 2D grid
    grid = [list(line) for line in garden_map.strip().split('\n')]
    rows, cols = len(grid), len(grid[0])
    
    # Find all regions
    visited: Set[Tuple[int, int]] = set()
    regions: List[Region] = []
    
    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited:
                region = find_region(grid, (row, col), visited)
                regions.append(region)
    
    # Calculate total price
    total_price = sum(region.area * region.perimeter for region in regions)
    return str(total_price)

def solution() -> str:
    """Read input from stdin and solve the problem."""
    import sys
    return calculate_total_fence_price(sys.stdin.read())