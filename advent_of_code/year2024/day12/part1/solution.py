from typing import List, Tuple, Dict, Set
from collections import deque


def calculate_total_fence_price(garden_map: str) -> str:
    """Calculate the total price of fencing for all regions in a garden map."""
    # Split map into rows
    grid = [list(line) for line in garden_map.strip().split("\n")]
    
    rows = len(grid)
    cols = len(grid[0])
    
    # Keep track of which plots we've already processed
    visited = set()
    total_price = 0

    # Helper function to check if coordinate is valid
    def is_valid(r: int, c: int) -> bool:
        return 0 <= r < rows and 0 <= c < cols

    # Helper function to get region size and perimeter using BFS
    def process_region(start_r: int, start_c: int, plant: str) -> Tuple[int, int]:
        queue = deque([(start_r, start_c)])
        region_coords = set([(start_r, start_c)])
        perimeter = 0
        
        while queue:
            r, c = queue.popleft()
            
            # Check all four directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                if is_valid(nr, nc):
                    if grid[nr][nc] == plant:
                        if (nr, nc) not in region_coords:
                            queue.append((nr, nc))
                            region_coords.add((nr, nc))
                    else:
                        # Found a boundary
                        perimeter += 1
                else:
                    # Edge of grid is part of perimeter
                    perimeter += 1
                    
        return len(region_coords), perimeter

    # Process each unvisited plot
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                plant = grid[r][c]
                area, perimeter = process_region(r, c, plant)
                
                # Mark all plots in this region as visited
                queue = deque([(r, c)])
                visited.add((r, c))
                
                while queue:
                    curr_r, curr_c = queue.popleft()
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        if is_valid(nr, nc) and grid[nr][nc] == plant and (nr, nc) not in visited:
                            queue.append((nr, nc))
                            visited.add((nr, nc))
                
                # Calculate price for this region
                price = area * perimeter
                total_price += price

    return str(total_price)