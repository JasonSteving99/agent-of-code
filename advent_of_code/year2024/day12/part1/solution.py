from typing import Set, List, Tuple, Dict
from collections import deque
import sys


def calculate_total_fence_price(map_str: str) -> str:
    # Parse the input map into a 2D grid
    garden_map = [list(line) for line in map_str.strip().split('\n')]
    rows, cols = len(garden_map), len(garden_map[0])

    # Helper function for flood fill - returns area and perimeter
    def get_region_stats(start_r: int, start_c: int, plant: str) -> Tuple[int, int]:
        visited = set()
        queue = deque([(start_r, start_c)])
        area = 0
        perimeter = 0
        
        while queue:
            r, c = queue.popleft()
            if (r, c) in visited:
                continue
                
            visited.add((r, c))
            area += 1
            
            # Check all 4 directions
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                # If neighbor is out of bounds or different plant, add to perimeter
                if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or 
                    garden_map[nr][nc] != plant):
                    perimeter += 1
                # If neighbor is same plant and not visited, add to queue
                elif garden_map[nr][nc] == plant and (nr, nc) not in visited:
                    queue.append((nr, nc))
                    
        return area, perimeter

    # Process all cells in the grid
    processed = set()
    total_price = 0
    
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in processed:
                plant = garden_map[r][c]
                area, perimeter = get_region_stats(r, c, plant)
                # Add cells to processed set
                for pr in range(rows):
                    for pc in range(cols):
                        if garden_map[pr][pc] == plant and (pr, pc) not in processed:
                            processed.add((pr, pc))
                # Calculate and add price for this region
                price = area * perimeter
                total_price += price

    return str(total_price)


def solution() -> str:
    # Read input from stdin
    input_data = sys.stdin.read()
    return calculate_total_fence_price(input_data)


if __name__ == "__main__":
    print(solution())