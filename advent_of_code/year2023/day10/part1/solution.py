from typing import List, Tuple


def get_pipe_char(grid: List[str], r: int, c: int) -> str:
    neighbors = []
    n, m = len(grid), len(grid[0])
    if r > 0 and grid[r - 1][c] != '.':
        neighbors.append((r - 1, c))
    if r < n - 1 and grid[r + 1][c] != '.':
        neighbors.append((r + 1, c))
    if c > 0 and grid[r][c - 1] != '.':
        neighbors.append((r, c - 1))
    if c < m - 1 and grid[r][c + 1] != '.':
        neighbors.append((r, c + 1))

    if len(neighbors) != 2:
        return 'S'  # Should not happen in valid input.

    n1, n2 = neighbors

    if (n1[0] == r - 1 and n2[0] == r + 1) or (n2[0] == r - 1 and n1[0] == r + 1):
        return "|"
    if (n1[1] == c - 1 and n2[1] == c + 1) or (n2[1] == c - 1 and n1[1] == c + 1):
        return "-"
    if (n1[0] == r - 1 and n2[1] == c + 1) or (n2[0] == r - 1 and n1[1] == c + 1):
        return "L"
    if (n1[0] == r - 1 and n2[1] == c - 1) or (n2[0] == r - 1 and n1[1] == c - 1):
        return "J"
    if (n1[0] == r + 1 and n2[1] == c - 1) or (n2[0] == r + 1 and n1[1] == c - 1):
        return "7"
    if (n1[0] == r + 1 and n2[1] == c + 1) or (n2[0] == r + 1 and n1[1] == c + 1):
        return "F"
    return 'S'


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
                grid[r] = grid[r][:c] + get_pipe_char(grid, r, c) + grid[r][c+1:]
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

