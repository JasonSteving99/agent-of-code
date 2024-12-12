from typing import List, Set, Tuple
from collections import deque
import sys


def find_regions(grid: List[List[str]]) -> List[Set[Tuple[int, int]]]:
    """Find all connected regions of same-type plants in the grid."""
    rows, cols = len(grid), len(grid[0])
    visited = set()
    regions = []
    
    def bfs(start_r: int, start_c: int, plant: str) -> Set[Tuple[int, int]]:
        region = set()
        queue = deque([(start_r, start_c)])
        
        while queue:
            r, c = queue.popleft()
            if (r, c) in visited:
                continue
                
            visited.add((r, c))
            region.add((r, c))
            
            # Check all 4 adjacent cells
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_r, new_c = r + dr, c + dc
                if (0 <= new_r < rows and 0 <= new_c < cols and
                    grid[new_r][new_c] == plant and
                    (new_r, new_c) not in visited):
                    queue.append((new_r, new_c))
        
        return region
    
    # Find all regions using BFS
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                regions.append(bfs(r, c, grid[r][c]))
    
    return regions


def calculate_perimeter(region: Set[Tuple[int, int]], grid: List[List[str]]) -> int:
    """Calculate the perimeter of a region."""
    perimeter = 0
    plant_type = grid[next(iter(region))[0]][next(iter(region))[1]]
    
    for r, c in region:
        # Check all 4 sides
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_r, new_c = r + dr, c + dc
            # If adjacent cell is outside grid or different plant type, add to perimeter
            if (new_r < 0 or new_r >= len(grid) or
                new_c < 0 or new_c >= len(grid[0]) or
                grid[new_r][new_c] != plant_type):
                perimeter += 1
    
    return perimeter


def calculate_total_fence_price(input_map: str) -> str:
    # Convert input string to grid
    grid = [list(row) for row in input_map.strip().split('\n')]
    
    # Find all regions
    regions = find_regions(grid)
    
    # Calculate total price
    total_price = 0
    for region in regions:
        area = len(region)  # Area is number of plots in region
        perimeter = calculate_perimeter(region, grid)
        price = area * perimeter
        total_price += price
    
    return str(total_price)


def solution() -> str:
    """Read from stdin and solve the problem."""
    input_data = sys.stdin.read().strip()
    return calculate_total_fence_price(input_data)


if __name__ == "__main__":
    print(solution())