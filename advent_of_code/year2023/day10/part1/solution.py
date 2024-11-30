from typing import List

def max_pipe_loop_distance(grid: str) -> int:
    grid_list = grid.splitlines()
    rows = len(grid_list)
    cols = len(grid_list[0])
    start = None
    for r in range(rows):
        for c in range(cols):
            if grid_list[r][c] == 'S':
                start = (r, c)
                break
        if start is not None:
            break

    connections = {}
    for r in range(rows):
        for c in range(cols):
            if grid_list[r][c] != '.':
                neighbors = []
                if grid_list[r][c] in ('|', 'L', 'J', 'S'):
                    if r > 0 and grid_list[r - 1][c] != '.':
                        neighbors.append((r - 1, c))
                if grid_list[r][c] in ('|', 'F', '7', 'S'):
                    if r < rows - 1 and grid_list[r + 1][c] != '.':
                        neighbors.append((r + 1, c))
                if grid_list[r][c] in ('-', 'L', 'F', 'S'):
                    if c < cols - 1 and grid_list[r][c + 1] != '.':
                        neighbors.append((r, c + 1))
                if grid_list[r][c] in ('-', 'J', '7', 'S'):
                    if c > 0 and grid_list[r][c - 1] != '.':
                        neighbors.append((r, c - 1))
                connections[(r, c)] = neighbors

    q = [(start, 0)]
    visited = {start}
    max_dist = 0
    while q:
        (r, c), dist = q.pop(0)
        max_dist = max(max_dist, dist)
        for nr, nc in connections[(r, c)]:
            if (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append(((nr, nc), dist + 1))

    return max_dist

def solution() -> int:
    grid = ""
    while True:
        try:
            line = input()
            grid += line + "\n"
        except EOFError:
            break

    return max_pipe_loop_distance(grid)
