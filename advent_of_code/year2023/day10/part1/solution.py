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

    connections = {}
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] != '.':
                neighbors = []
                if maze[r][c] in ('|', 'L', 'J', 'S'):
                    if r > 0 and maze[r - 1][c] != '.':
                        neighbors.append((r - 1, c))
                if maze[r][c] in ('|', 'F', '7', 'S'):
                    if r < rows - 1 and maze[r + 1][c] != '.':
                        neighbors.append((r + 1, c))
                if maze[r][c] in ('-', 'L', 'F', 'S'):
                    if c < cols - 1 and maze[r][c + 1] != '.':
                        neighbors.append((r, c + 1))
                if maze[r][c] in ('-', 'J', '7', 'S'):
                    if c > 0 and maze[r][c - 1] != '.':
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

def max_loop_distance(maze_str: str) -> int:
    maze: List[str] = maze_str.split('\n')
    return solve(maze)

def solution() -> int:
    maze: List[str] = []
    while True:
        try:
            line = input()
            maze.append(line)
        except EOFError:
            break

    return solve(maze)
