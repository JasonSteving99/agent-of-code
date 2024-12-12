from typing import List, Set, Tuple
from collections import deque
import sys


def find_regions(grid: List[List[str]]) -> List[Set[Tuple[int, int]]]:
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

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_r, new_c = r + dr, c + dc
                if (0 <= new_r < rows and 0 <= new_c < cols and
                    grid[new_r][new_c] == plant and
                    (new_r, new_c) not in visited):
                    queue.append((new_r, new_c))

        return region

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                regions.append(bfs(r, c, grid[r][c]))

    return regions


def calculate_perimeter(region: Set[Tuple[int, int]], grid: List[List[str]]) -> int:
    perimeter = 0
    for r, c in region:
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == grid[r][c]):
                perimeter += 1
    return perimeter


def calculate_total_fence_price(input_map: str) -> str:
    grid = [list(row) for row in input_map.strip().split('\n')]
    regions = find_regions(grid)
    total_price = 0

    for region in regions:
        area = len(region)
        perimeter = calculate_perimeter(region, grid)
        price = area * perimeter
        total_price += price

    return str(total_price)


def solution() -> str:
    input_data = sys.stdin.read().strip()
    return calculate_total_fence_price(input_data)


if __name__ == "__main__":
    print(solution())
