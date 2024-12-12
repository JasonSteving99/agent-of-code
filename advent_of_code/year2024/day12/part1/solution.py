from typing import List, Set, Tuple
from collections import deque


def calculate_total_fence_price(garden_map: str) -> str:
    """Calculate the total fence price for all garden regions."""
    # Convert input to 2D grid
    grid = [list(line) for line in garden_map.strip().splitlines()]
    rows, cols = len(grid), len(grid[0])
    visited = set()
    total_price = 0

    def get_neighbors(r: int, c: int) -> List[Tuple[int, int]]:
        """Get valid neighboring cells with same plant type."""
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and 
                grid[nr][nc] == grid[r][c]):
                neighbors.append((nr, nc))
        return neighbors

    def calculate_region_stats(start_r: int, start_c: int) -> Tuple[int, int]:
        """Calculate area and perimeter of a region starting at given position."""
        plant_type = grid[start_r][start_c]
        area = 0
        perimeter = 0
        region = set()
        queue = deque([(start_r, start_c)])
        region.add((start_r, start_c))

        while queue:
            r, c = queue.popleft()
            area += 1
            # Check all four sides for perimeter calculation
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < rows and 0 <= nc < cols):
                    perimeter += 1
                elif grid[nr][nc] != plant_type:
                    perimeter += 1
                elif (nr, nc) not in region:
                    queue.append((nr, nc))
                    region.add((nr, nc))

        return area, perimeter

    # Process each unvisited cell
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                # Start of a new region
                current_type = grid[r][c]
                area = 0
                perimeter = 0
                
                # Find all cells in this region and calculate stats
                queue = deque([(r, c)])
                region = set()
                
                while queue:
                    curr_r, curr_c = queue.popleft()
                    if (curr_r, curr_c) in visited:
                        continue
                        
                    visited.add((curr_r, curr_c))
                    region.add((curr_r, curr_c))
                    
                    for neighbor in get_neighbors(curr_r, curr_c):
                        if neighbor not in visited:
                            queue.append(neighbor)
                
                # Calculate area and perimeter for the complete region
                area, perimeter = calculate_region_stats(r, c)
                region_price = area * perimeter
                total_price += region_price

    return str(total_price)

def solution() -> str:
    """Read input from stdin and return the solution."""
    import sys
    return calculate_total_fence_price(sys.stdin.read())