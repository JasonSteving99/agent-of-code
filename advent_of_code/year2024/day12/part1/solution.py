"""Solution for Garden Groups."""
from collections import deque
from typing import List, Set, Tuple


def is_shared_edge(grid: List[str], r: int, c: int, dr: int, dc: int, plant_type: str) -> bool:
    """Check if edge is shared with same type."""
    rows, cols = len(grid), len(grid[0])
    nr, nc = r + dr, c + dc
    return 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == plant_type


def get_region_data(grid: List[str], start_row: int, start_col: int, visited: Set[Tuple[int, int]]) -> tuple[int, int]:
    """Find area and perimeter of a region starting at given coordinates using BFS."""
    rows, cols = len(grid), len(grid[0])
    plant_type = grid[start_row][start_col]
    area = 0
    perimeter = 0
    queue = deque([(start_row, start_col)])

    while queue:
        row, col = queue.popleft()
        if (row, col) in visited:
            continue

        visited.add((row, col))
        area += 1

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Check adjacent cells
            if not is_shared_edge(grid, row, col, dr, dc, plant_type):
                perimeter += 1

            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == plant_type and (nr, nc) not in visited:
                queue.append((nr, nc))

    return area, perimeter


def calculate_total_fence_price(input_map: str) -> str:
    """Calculate total fence price."""
    grid = input_map.strip().split('\n')
    rows, cols = len(grid), len(grid[0])
    visited: Set[Tuple[int, int]] = set()
    total_price = 0

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                area, perimeter = get_region_data(grid, i, j, visited)
                total_price += area * perimeter

    return str(total_price)


def solution() -> str:
    """Read from stdin and solve."""
    import sys
    input_data = sys.stdin.read()
    return calculate_total_fence_price(input_data)
