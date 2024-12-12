"""Solution for Garden Groups."""
from collections import deque
from typing import List, Set, Tuple, Dict


def get_region_data(grid: List[str], start_row: int, start_col: int, visited: Set[Tuple[int, int]]) -> tuple[int, int]:
    """Find area and perimeter of a region starting at given coordinates using BFS."""
    rows, cols = len(grid), len(grid[0])
    plant_type = grid[start_row][start_col]
    area = 0
    perimeter = 0

    queue: deque[tuple[int, int]] = deque([(start_row, start_col)])
    while queue:
        row, col = queue.popleft()
        if (row, col) in visited:
            continue

        visited.add((row, col))
        area += 1

        # Check all four sides for perimeter and connected plots
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # If out of bounds or different plant type, add to perimeter
            if (new_row < 0 or new_row >= rows or 
                new_col < 0 or new_col >= cols or 
                grid[new_row][new_col] != plant_type):
                perimeter += 1
            # If same plant type and not visited, add to queue
            elif (new_row, new_col) not in visited:
                queue.append((new_row, new_col))

    return area, perimeter


def calculate_total_fence_price(input_map: str) -> str:
    """Calculate the total price of fencing all regions on the map."""
    # Convert input string to grid
    grid = input_map.strip().split('\n')
    rows, cols = len(grid), len(grid[0])
    
    visited: Set[Tuple[int, int]] = set()
    total_price = 0

    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                area, perimeter = get_region_data(grid, i, j, visited)
                region_price = area * perimeter
                total_price += region_price

    return str(total_price)


def solution() -> str:
    """Read from stdin and solve the problem."""
    import sys
    input_data = sys.stdin.read()
    return calculate_total_fence_price(input_data)