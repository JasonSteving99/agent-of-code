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
                
                if not is_valid(nr, nc):
                    perimeter += 1  # Edge of the grid
                elif grid[nr][nc] != plant:
                    perimeter += 1  # Different plant or unvisited
                    
        return len(region_coords), perimeter

    # Process each unvisited plot
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                plant = grid[r][c]
                area, perimeter = process_region(r, c, plant)

                # Mark all connected plots of the same type as visited 
                q = deque([(r, c)])
                visited.add((r, c))
                while q:
                    cr, cc = q.popleft()
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = cr + dr, cc + dc
                        if (is_valid(nr, nc) and (nr, nc) not in visited and grid[nr][nc] == plant):
                            visited.add((nr, nc))
                            q.append((nr, nc))
                            
                total_price += area * perimeter

    return str(total_price)