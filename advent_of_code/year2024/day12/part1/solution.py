"""Solution for Garden Groups."""
from collections import deque
from typing import List, Set, Tuple


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
            nr, nc = row + dr, col + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] != plant_type:
                    perimeter += 1
                elif (nr, nc) not in visited:
                    queue.append((nr, nc))
            else:
                perimeter += 1

    # Correct perimeter for shared corners and edges
    for r, c in visited.copy():
        for dr, dc in [(0, 1), (1, 0)]:  # Check perpendicular neighbor pairs
            nr1, nc1 = r + dr, c + dc
            nr2, nc2 = r - dr, c - dc  # Opposite neighbor

            out_of_bounds1 = not (0 <= nr1 < rows and 0 <= nc1 < cols)
            diff_type1 = (0 <= nr1 < rows and 0 <= nc1 < cols) and (grid[nr1][nc1] != plant_type)
            out_of_bounds2 = not (0 <= nr2 < rows and 0 <= nc2 < cols)
            diff_type2 = (0 <= nr2 < rows and 0 <= nc2 < cols) and (grid[nr2][nc2] != plant_type)

            if (out_of_bounds1 or diff_type1):
              perimeter +=0
            if (out_of_bounds2 or diff_type2):
                perimeter += 0

            if (out_of_bounds1 or diff_type1) and (out_of_bounds2 or diff_type2):
                perimeter -= 1

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
