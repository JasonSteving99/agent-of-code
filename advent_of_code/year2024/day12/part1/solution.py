from typing import List, Set, Tuple
from collections import deque
import sys


def get_regions(grid: List[str]) -> List[Set[Tuple[int, int]]]:
    rows, cols = len(grid), len(grid[0])
    visited = set()
    regions = []
    
    def get_neighbors(r: int, c: int) -> List[Tuple[int, int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbors.append((nr, nc))
        return neighbors

    def bfs(start_r: int, start_c: int, plant: str) -> Set[Tuple[int, int]]:
        region = set()
        queue = deque([(start_r, start_c)])
        region.add((start_r, start_c))
        visited.add((start_r, start_c))
        
        while queue:
            r, c = queue.popleft()
            for nr, nc in get_neighbors(r, c):
                if (nr, nc) not in visited and grid[nr][nc] == plant:
                    queue.append((nr, nc))
                    region.add((nr, nc))
                    visited.add((nr, nc))
        return region

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                regions.append(bfs(r, c, grid[r][c]))
    
    return regions


def calculate_perimeter(region: Set[Tuple[int, int]], grid: List[str]) -> int:
    perimeter = 0
    for r, c in region:
        # Check all four sides
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            # Count as perimeter if out of bounds or different plant
            if (nr, nc) not in region:
                perimeter += 1
    return perimeter


def calculate_total_fence_price(input_map: str) -> str:
    # Convert input string to grid
    grid = input_map.strip().split('\n')
    
    # Get all regions using BFS
    regions = get_regions(grid)
    
    # Calculate total price for all regions
    total_price = 0
    for region in regions:
        area = len(region)
        perimeter = calculate_perimeter(region, grid)
        price = area * perimeter
        total_price += price
    
    return str(total_price)


def solution() -> str:
    # Read input from stdin
    return calculate_total_fence_price(sys.stdin.read())

if __name__ == "__main__":
    print(solution())