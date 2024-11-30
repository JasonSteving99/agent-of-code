from typing import List

def solve(grid: List[str]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    start = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
                break
        if start is not None:
            break

    connections = {}
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '.':
                neighbors = []
                if grid[r][c] in ('|', 'L', 'J', 'S'):
                    if r > 0 and grid[r - 1][c] != '.':
                        neighbors.append((r - 1, c))
                if grid[r][c] in ('|', 'F', '7', 'S'):
                    if r < rows - 1 and grid[r + 1][c] != '.':
                        neighbors.append((r + 1, c))
                if grid[r][c] in ('-', 'L', 'F', 'S'):
                    if c < cols - 1 and grid[r][c + 1] != '.':
                        neighbors.append((r, c + 1))
                if grid[r][c] in ('-', 'J', '7', 'S'):
                    if c > 0 and grid[r][c - 1] != '.':
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
    grid = []
    while True:
        try:
            line = input()
            grid.append(line)
        except EOFError:
            break
    return solve(grid)
