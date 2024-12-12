from typing import Dict, Set, Tuple, List
import itertools


def fill_region(grid: List[List[str]], x: int, y: int, visited: Set[Tuple[int, int]], plant: str) -> List[Tuple[int, int]]:
    """DFS to fill a region and return all coordinates of the same plant type."""
    if (x, y) in visited or not (0 <= x < len(grid) and 0 <= y < len(grid[0])) or grid[x][y] != plant:
        return []
    
    visited.add((x, y))
    coords = [(x, y)]
    
    # Check all adjacent cells (up, down, left, right)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        coords.extend(fill_region(grid, x + dx, y + dy, visited, plant))
    
    return coords


def calculate_perimeter(region_coords: List[Tuple[int, int]], grid: List[List[str]]) -> int:
    """Calculate perimeter of a region by checking adjacent cells."""
    perimeter = 0
    region_set = set(region_coords)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for x, y in region_coords:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # If neighbor is outside grid or not part of the same region, add to perimeter
            if (not (0 <= nx < len(grid) and 0 <= ny < len(grid[0]))) or \
               ((nx, ny) not in region_set):
                perimeter += 1
                
    return perimeter


def process_garden_plot(garden_plot: str) -> int:
    """Process garden plot and return total fence price."""
    # Convert input string to 2D grid
    grid = [list(line.strip()) for line in garden_plot.strip().split('\n')]
    if not grid:
        return 0
        
    visited: Set[Tuple[int, int]] = set()
    total_price = 0
    
    # Iterate through each cell in the grid
    for i, j in itertools.product(range(len(grid)), range(len(grid[0]))):
        if (i, j) not in visited:
            # Find all coordinates in current region
            region_coords = fill_region(grid, i, j, visited, grid[i][j])
            if region_coords:
                area = len(region_coords)
                perimeter = calculate_perimeter(region_coords, grid)
                # Calculate price for this region
                region_price = area * perimeter
                total_price += region_price
    
    return total_price


def calculate_total_fence_price(input_str: str) -> str:
    """Calculate the total price of fencing all regions on the map."""
    total_price = process_garden_plot(input_str)
    return str(total_price)


def solution() -> str:
    """Read from stdin and return the solution."""
    import sys
    input_data = sys.stdin.read()
    return calculate_total_fence_price(input_data)