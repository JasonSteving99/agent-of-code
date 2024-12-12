from typing import List, Set, Tuple
import sys

def get_neighbors(x: int, y: int, grid: List[List[str]], rows: int, cols: int) -> List[Tuple[int, int]]:
    """Get valid neighboring coordinates."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < rows and 0 <= new_y < cols:
            neighbors.append((new_x, new_y))
    return neighbors

def find_region(start_x: int, start_y: int, grid: List[List[str]], visited: Set[Tuple[int, int]]) -> Tuple[int, int]:
    """Find region starting from given coordinates and return area and perimeter."""
    if (start_x, start_y) in visited:
        return 0, 0

    rows, cols = len(grid), len(grid[0])
    plant_type = grid[start_x][start_y]

    queue = [(start_x, start_y)]
    area = 0
    perimeter = 0
    region_coords = set()

    while queue:
        x, y = queue.pop(0)
        if (x, y) in region_coords:
            continue

        region_coords.add((x, y))
        visited.add((x, y))
        area += 1

        neighbors = get_neighbors(x, y, grid, rows, cols)        
        sides = 4
        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == plant_type:
                    sides -= 1
                    if (nx, ny) not in region_coords:  # Check before adding
                        queue.append((nx, ny))
        perimeter += sides            

    return area, perimeter

def calculate_total_fence_price(garden_map: str) -> int:
    """Calculate total fence price for all regions in the garden."""
    grid = [list(row) for row in garden_map.strip().split('\n')]
    rows, cols = len(grid), len(grid[0])

    total_price = 0
    visited = set()

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                area, perimeter = find_region(i, j, grid, visited)
                region_price = area * perimeter
                total_price += region_price

    return total_price

def solution() -> int:
    """Read input from stdin and return the solution."""
    garden_map = sys.stdin.read()
    return calculate_total_fence_price(garden_map)