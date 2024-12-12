from typing import List, Set, Tuple, Dict
from collections import deque
import sys


def find_regions(grid: List[List[str]]) -> List[Set[Tuple[int, int]]]:
    """Find all connected regions in the grid using BFS."""
    rows, cols = len(grid), len(grid[0])
    visited = set()
    regions = []
    
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                region_type = grid[r][c]
                region = set()
                queue = deque([(r, c)])
                visited.add((r, c))
                
                while queue:
                    curr_r, curr_c = queue.popleft()
                    region.add((curr_r, curr_c))
                    
                    # Check all 4 directions
                    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        new_r, new_c = curr_r + dr, curr_c + dc
                        if (0 <= new_r < rows and 
                            0 <= new_c < cols and 
                            grid[new_r][new_c] == region_type and 
                            (new_r, new_c) not in visited):
                            queue.append((new_r, new_c))
                            visited.add((new_r, new_c))
                
                regions.append(region)
    
    return regions


def calculate_perimeter(region: Set[Tuple[int, int]], grid: List[List[str]]) -> int:
    """Calculate the perimeter of a region."""
    perimeter = 0
    rows, cols = len(grid), len(grid[0])
    
    for r, c in region:
        region_type = grid[r][c]
        # Check all 4 directions
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_r, new_c = r + dr, c + dc
            # Count edge if out of bounds or different type
            if (new_r < 0 or new_r >= rows or 
                new_c < 0 or new_c >= cols or 
                (new_r, new_c) not in region):
                perimeter += 1
    
    return perimeter


def calculate_total_fencing_price(garden_map: str) -> str:
    """Calculate the total price of fencing all regions."""
    # Convert input string to 2D grid
    grid = [list(row) for row in garden_map.strip().split('\n')]
    
    # Find all regions
    regions = find_regions(grid)
    
    total_price = 0
    # Calculate price for each region
    for region in regions:
        area = len(region)
        perimeter = calculate_perimeter(region, grid)
        region_price = area * perimeter
        total_price += region_price
    
    return str(total_price)


def solution() -> str:
    """Read input from stdin and solve the problem."""
    # Read input from stdin
    garden_map = sys.stdin.read().strip()
    return calculate_total_fencing_price(garden_map)