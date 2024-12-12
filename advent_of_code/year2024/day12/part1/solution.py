"""Calculate total cost of garden fencing."""
from typing import Dict, List, Set, Tuple
from collections import defaultdict


def get_neighbours(x: int, y: int, max_x: int, max_y: int) -> List[Tuple[int, int]]:
    """Return valid neighbouring coordinates."""
    neighbours = []
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < max_x and 0 <= new_y < max_y:
            neighbours.append((new_x, new_y))
    return neighbours


def find_region(grid: List[str], start_x: int, start_y: int, visited: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    """Find all coordinates in a region using flood fill."""
    max_y, max_x = len(grid), len(grid[0])
    region = set()
    stack = [(start_x, start_y)]
    plant_type = grid[start_y][start_x]
    
    while stack:
        x, y = stack.pop()
        if (x, y) not in visited:
            if grid[y][x] == plant_type:
                region.add((x, y))
                visited.add((x, y))
                for nx, ny in get_neighbours(x, y, max_x, max_y):
                    if grid[ny][nx] == plant_type:
                        stack.append((nx, ny))
    return region


def calculate_perimeter(region: Set[Tuple[int, int]], grid: List[str]) -> int:
    """Calculate the perimeter of a region."""
    perimeter = 0
    max_y, max_x = len(grid), len(grid[0])

    for x, y in region:
        for nx, ny in get_neighbours(x, y, max_x, max_y):
            if (nx, ny) not in region:
                perimeter += 1
    return perimeter


def calculate_region_price(region: Set[Tuple[int, int]], grid: List[str]) -> int:
    """Calculate price for a region (area * perimeter)."""
    area = len(region)
    perimeter = calculate_perimeter(region, grid)
    return area * perimeter



def calculate_total_fence_price(input_map: str) -> str:
    """Calculate total price of fencing all regions."""
    grid = input_map.strip().split('\n')
    if not grid:
        return "0"

    visited: Set[Tuple[int, int]] = set()
    total_price = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x, y) not in visited:
                region = find_region(grid, x, y, visited)
                price = calculate_region_price(region, grid)
                total_price += price

    return str(total_price)


def solution() -> str:
    """Read input from stdin and solve."""
    import sys
    input_map = "".join(sys.stdin.readlines())
    return calculate_total_fence_price(input_map)