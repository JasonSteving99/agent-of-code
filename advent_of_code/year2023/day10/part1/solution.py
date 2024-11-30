from typing import List

def solve(maze: str) -> int:
    grid = [list(row) for row in maze.splitlines()]
    rows = len(grid)
    cols = len(grid[0])

    def find_start():
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'S':
                    return r, c
        return None

    start_row, start_col = find_start()

    connections = {
        '|': {(-1, 0), (1, 0)},
        '-': {(0, -1), (0, 1)},
        'L': {(0, 1), (-1, 0)},
        'J': {(0, -1), (-1, 0)},
        '7': {(1, 0), (0, -1)},
        'F': {(1, 0), (0, 1)},
    }

    def get_neighbors(r, c):
        neighbors = []
        for dr, dc in connections.get(grid[r][c], []):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                for dr2, dc2 in connections.get(grid[nr][nc], []):
                    if (nr + dr2 == r and nc + dc2 == c):
                        neighbors.append((nr, nc))
                        break
        return neighbors

    q = [(start_row, start_col, 0)]
    visited = set([(start_row, start_col)])
    max_dist = 0

    while q:
        r, c, dist = q.pop(0)
        max_dist = max(max_dist, dist)

        for nr, nc in get_neighbors(r,c):
            if (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc, dist + 1))

    return max_dist

def solution() -> int:
    maze_str: str = ""
    while True:
        try:
            line = input()
            maze_str += line + "\n"
        except EOFError:
            break
    return solve(maze_str[:-1])