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
                if not (0 <= nr < rows and 0 <= nc < cols and (nr, nc) in region):
                    perimeter += 1
        
        return len(region), perimeter

    # Process each unvisited cell
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                plant = grid[r][c]
                area, perimeter = get_region_stats(r, c, plant)

                total_price += area * perimeter

                # Mark all cells in the found region as visited
                q = deque([(r,c)])
                visited.add((r,c))
                while q:
                    cr, cc = q.popleft()
                    for nr, nc in [(cr+1, cc), (cr-1, cc), (cr, cc+1), (cr, cc-1)]:
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == plant and (nr, nc) not in visited:
                            q.append((nr, nc))
                            visited.add((nr, nc))

    return str(total_price)