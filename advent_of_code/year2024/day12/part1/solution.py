from typing import List, Set, Tuple, Dict
import sys
from collections import deque

def get_region_perimeter(area: Set[Tuple[int, int]], grid: List[List[str]], rows: int, cols: int) -> int:
    """Calculate the perimeter of a given region."""
    perimeter = 0
    for r, c in area:
        # Check all four sides of the current cell
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            # If neighbor is out of bounds or not part of region, add to perimeter
            if (nr < 0 or nr >= rows or nc < 0 or nc >= cols 
                or (nr, nc) not in area):
                perimeter += 1
    return perimeter

def find_regions(grid: List[List[str]], rows: int, cols: int) -> List[Tuple[int, int]]:
    """Find all regions in the grid and return their areas and perimeters."""
    visited = set()
    regions = []

    def bfs(r: int, c: int, plant_type: str) -> Set[Tuple[int, int]]:
        """BFS to find connected region of same plant type."""
        queue = deque([(r, c)])
        region = {(r, c)}
        visited.add((r, c))
        
        while queue:
            curr_r, curr_c = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = curr_r + dr, curr_c + dc
                if (0 <= nr < rows and 0 <= nc < cols 
                    and (nr, nc) not in visited 
                    and grid[nr][nc] == plant_type):
                    queue.append((nr, nc))
                    region.add((nr, nc))
                    visited.add((nr, nc))
        return region

    # Find all regions
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                region = bfs(r, c, grid[r][c])
                area = len(region)
                perimeter = get_region_perimeter(region, grid, rows, cols)
                regions.append((area, perimeter))

    return regions

def calculate_total_fence_price(input_str: str) -> str:
    """Calculate the total fence price from the input garden map."""
    # Convert input string to grid
    grid = [list(line.strip()) for line in input_str.strip().split('\n')]
    rows, cols = len(grid), len(grid[0])
    
    # Find all regions and calculate their areas and perimeters
    regions = find_regions(grid, rows, cols)
    
    # Calculate total price
    total_price = sum(area * perimeter for area, perimeter in regions)
    
    return str(total_price)

def solution() -> str:
    """Read input from stdin and return the solution."""
    input_data = sys.stdin.read()
    return calculate_total_fence_price(input_data)

if __name__ == "__main__":
    print(solution())