from typing import List


def calculate_total_fence_price(garden_map_str: str) -> str:
    """Calculates the total price of fencing all regions in the garden map."""
    if not garden_map_str:
        return "0"

    grid: List[List[str]] = [list(row) for row in garden_map_str.splitlines()]
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def calculate_region_price(start_row: int, start_col: int) -> int:
        plant_type = grid[start_row][start_col]
        region_cells = set()
        perimeter = 0
        queue = [(start_row, start_col)]
        region_cells.add((start_row, start_col))

        while queue:
            row, col = queue.pop(0)

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == plant_type and (nr, nc) not in region_cells:
                        queue.append((nr, nc))
                        region_cells.add((nr, nc))

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = row + dr, col + dc
                if not (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == plant_type):
                    perimeter += 1

        area = len(region_cells)
        visited.update(region_cells)
        return area * perimeter

    total_price = 0
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                total_price += calculate_region_price(r, c)

    return str(total_price)


def solution() -> str:
    import sys

    input_data = sys.stdin.read().strip()
    return calculate_total_fence_price(input_data)
