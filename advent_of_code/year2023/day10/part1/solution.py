from typing import List, Tuple


def get_neighbors(grid: List[str], r: int, c: int) -> List[Tuple[int, int]]:
    n, m = len(grid), len(grid[0])
    neighbors = []
    for dr, dc, char1, char2 in [(0, 1, "-", "-"), (0, -1, "-", "-"), (1, 0, "|", "|"), (-1, 0, "|", "|"),
                                     (0, 1, "L", "-"), (0, 1, "F", "-"),
                                     (-1, 0, "L", "|"), (-1, 0, "J", "|"),
                                     (0, -1, "J", "-"), (0, -1, "7", "-"),
                                     (1, 0, "F", "|"), (1, 0, "7", "|"),
                                      (0, 1, "S", "-"), (0, -1, "S", "-"), (1, 0, "S", "|"), (-1, 0, "S", "|")]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and grid[r][c] in [char1, 'S'] and grid[nr][nc] in [char2, 'S'] and grid[nr][nc] != '.':
            neighbors.append((nr, nc))
    return neighbors


def max_loop_distance(grid_str: str) -> int:
    grid: List[str] = grid_str.splitlines()
    n, m = len(grid), len(grid[0])
    start_r, start_c = -1, -1
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 'S':
                start_r, start_c = r, c
                break

    q = [(start_r, start_c, 0)]
    visited = set()
    max_dist = 0

    while q:
        r, c, dist = q.pop(0)
        if (r, c) in visited:
            continue
        visited.add((r, c))
        max_dist = max(max_dist, dist)

        for nr, nc in get_neighbors(grid, r, c):
            q.append((nr, nc, dist + 1))

    return max_dist


def solution() -> int:
    grid_str = ""
    while True:
        try:
            line = input()
            grid_str += line + "\n"
        except EOFError:
            break

    return max_loop_distance(grid_str)
