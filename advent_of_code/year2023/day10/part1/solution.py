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
        tile = maze[r][c]
        if tile == 'S':
            tile = ''

        for dr, dc, valid_pipes in [(-1, 0, '|LJ7'), (1, 0, '|7LF'), (0, -1, '-7FJ'), (0, 1, '-LJF')]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '.':
                neighbor_tile = maze[nr][nc]
                if neighbor_tile == 'S':
                    neighbor_tile = ''

                if tile == '':
                    neighbors.append((nr, nc))
                elif (tile in valid_pipes or neighbor_tile in valid_pipes) and \
                     (tile != '|' or neighbor_tile != '-') and \
                     (tile != '-' or neighbor_tile != '|'):
                    neighbors.append((nr, nc))

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
