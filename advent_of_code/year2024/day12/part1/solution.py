from typing import Set, List, Tuple, Dict
from collections import deque
import sys


def calculate_total_fence_price(map_str: str) -> str:
    # Parse the input map into a 2D grid
    garden_map = [list(line) for line in map_str.strip().split('\n')]
    rows, cols = len(garden_map), len(garden_map[0])

    # Helper function for flood fill
    def get_region_stats(start_r: int, start_c: int, plant: str) -> Tuple[int, int, set]:
        q = deque([(start_r, start_c)])
        visited: Set[Tuple[int, int]] = set()
        area = 0
        perimeter = 0

        while q:
            r, c = q.popleft()
            if (r, c) in visited:
                continue
            visited.add((r, c))
            area += 1

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if garden_map[nr][nc] != plant:
                        perimeter += 1
                    elif (nr, nc) not in visited:
                        q.append((nr, nc))
                else:
                    perimeter += 1

        return area, perimeter, visited

    visited_cells: Set[Tuple[int, int]] = set()
    total_price = 0
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited_cells:
                plant_type = garden_map[r][c]
                area, perimeter, visited = get_region_stats(r, c, plant_type)
                total_price += area * perimeter
                visited_cells.update(visited)    
    return str(total_price)


def solution() -> str:
    map_str = sys.stdin.read()
    return calculate_total_fence_price(map_str)


if __name__ == "__main__":
    print(solution())