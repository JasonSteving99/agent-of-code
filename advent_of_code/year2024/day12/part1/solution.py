from typing import Set, Tuple, Dict, List
import sys
from collections import deque


def solution() -> str:
    # Read input from stdin
    input_str = sys.stdin.read().strip()
    return calculate_total_fence_price(input_str)


def calculate_total_fence_price(input_map: str) -> str:
    """Calculate the total price of fencing for all garden regions."""
    # Convert input string to 2D grid
    grid = [list(line) for line in input_map.splitlines()]
    rows = len(grid)
    cols = len(grid[0])
    
    # Track visited cells to avoid duplicates
    visited = set()
    total_price = 0

    # Helper function to count perimeter and area
    def get_region_stats(start_r: int, start_c: int, plant: str) -> Tuple[int, int]:
        region = set()
        queue = deque([(start_r, start_c)])
        region.add((start_r, start_c))
        
        while queue:
            r, c = queue.popleft()
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if (0 <= nr < rows and 0 <= nc < cols and 
                    grid[nr][nc] == plant and 
                    (nr, nc) not in region):
                    queue.append((nr, nc))
                    region.add((nr, nc))
        
        # Calculate perimeter
        perimeter = 0
        for r, c in region:
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or
                    grid[nr][nc] != plant):
                    perimeter += 1
        
        return len(region), perimeter

    # Process each unvisited cell
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                plant = grid[r][c]
                area, perimeter = get_region_stats(r, c, plant)
                
                # Mark all cells in this region as visited
                queue = deque([(r, c)])
                visited.add((r, c))
                while queue:
                    curr_r, curr_c = queue.popleft()
                    for nr, nc in [(curr_r+1, curr_c), (curr_r-1, curr_c), 
                                 (curr_r, curr_c+1), (curr_r, curr_c-1)]:
                        if (0 <= nr < rows and 0 <= nc < cols and 
                            grid[nr][nc] == plant and 
                            (nr, nc) not in visited):
                            queue.append((nr, nc))
                            visited.add((nr, nc))
                
                # Calculate price for this region
                price = area * perimeter
                total_price += price

    return str(total_price)