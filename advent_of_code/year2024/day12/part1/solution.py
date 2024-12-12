from typing import List, Tuple, Dict, Set


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

    # Helper function to get region size and perimeter using DFS
    def process_region(start_r: int, start_c: int, plant: str) -> Tuple[Set[Tuple[int, int]], int]:
        stack = [(start_r, start_c)]
        region_coords = set()
        perimeter = 0

        while stack:
            r, c = stack.pop()
            if (r, c) in region_coords:
                continue
            region_coords.add((r, c))

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                if not is_valid(nr, nc):
                    perimeter += 1
                elif grid[nr][nc] != plant:
                    perimeter +=1
                elif (nr, nc) not in region_coords:
                    stack.append((nr, nc))
        return region_coords, perimeter

    # Process each unvisited plot
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                plant = grid[r][c]
                region_coords, perimeter = process_region(r, c, plant)
                area = len(region_coords)
                visited.update(region_coords)
                total_price += area * perimeter
                
    return str(total_price)