from typing import List, Tuple


def get_neighbors(grid: List[str], r: int, c: int) -> List[Tuple[int, int]]:
    n, m = len(grid), len(grid[0])
    neighbors = []
    if grid[r][c] in "|-S":
        if r > 0 and grid[r - 1][c] != '.':
            neighbors.append((r - 1, c))
        if r < n - 1 and grid[r + 1][c] != '.':
            neighbors.append((r + 1, c))
    if grid[r][c] in "-S":
        if c > 0 and grid[r][c - 1] != '.':
            neighbors.append((r, c - 1))
        if c < m - 1 and grid[r][c + 1] != '.':
            neighbors.append((r, c + 1))
    if grid[r][c] in "L7S":
        if r > 0 and grid[r - 1][c] != '.':
            neighbors.append((r - 1, c))
        if c < m - 1 and grid[r][c + 1] != '.':
            neighbors.append((r, c + 1))
    if grid[r][c] in "JFS":
        if r > 0 and grid[r - 1][c] != '.':
            neighbors.append((r - 1, c))
        if c > 0 and grid[r][c - 1] != '.':
            neighbors.append((r, c - 1))
    if grid[r][c] in "F|S":
        if r < n - 1 and grid[r + 1][c] != '.':
            neighbors.append((r + 1, c))
        if c < m - 1 and grid[r][c + 1] != '.':
            neighbors.append((r, c + 1))
    if grid[r][c] in "7-S":
        if r < n - 1 and grid[r + 1][c] != '.':
            neighbors.append((r + 1, c))
        if c > 0 and grid[r][c - 1] != '.':
            neighbors.append((r, c - 1))
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
