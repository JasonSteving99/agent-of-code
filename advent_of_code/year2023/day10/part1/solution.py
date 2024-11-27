from typing import List

def solve(maze: List[str]) -> int:
    rows = len(maze)
    cols = len(maze[0])
    start = None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
                break
        if start is not None:
            break

    if start is None:
        return 0

    def get_neighbors(r, c):
        neighbors = []
        if maze[r][c] in ('|', 'L', 'J', '7', 'F', 'S'):
            if r > 0 and maze[r - 1][c] in ('|', 'L', 'J', 'S'):
                neighbors.append((r - 1, c))
        if maze[r][c] in ('|', '7', 'F', 'L', 'J', 'S'):
            if r < rows - 1 and maze[r + 1][c] in ('|', '7', 'F', 'S'):
                neighbors.append((r + 1, c))
        if maze[r][c] in ('-', 'L', 'F', '7', 'J', 'S'):
            if c < cols - 1 and maze[r][c + 1] in ('-', 'L', 'F', 'S'):
                neighbors.append((r, c + 1))
        if maze[r][c] in ('-', 'J', '7', 'L', 'F', 'S'):
            if c > 0 and maze[r][c - 1] in ('-', 'J', '7', 'S'):
                neighbors.append((r, c - 1))
        return neighbors

    q = [(start, 0)]
    visited = {start}
    max_dist = 0

    while q:
        (r, c), dist = q.pop(0)
        max_dist = max(max_dist, dist)
        for nr, nc in get_neighbors(r, c):
            if (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append(((nr, nc), dist + 1))
    return max_dist

def max_loop_distance(maze: str) -> int:
    maze_list = maze.splitlines()
    return solve(maze_list)

def solution() -> int:
    maze: List[str] = []
    while True:
        try:
            line = input()
            maze.append(line)
        except EOFError:
            break
    return solve(maze)
