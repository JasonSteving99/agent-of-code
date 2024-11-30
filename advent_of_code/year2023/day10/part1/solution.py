from typing import List


def furthest_point_in_pipe_maze(maze_str: str) -> int:
    maze = maze_str.strip().split('\n')
    rows = len(maze)
    cols = len(maze[0])
    start_row, start_col = -1, -1
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start_row, start_col = r, c
                break

    def get_neighbors(r, c):
        neighbors = []
        if maze[r][c] in ('|', 'L', 'J', '7', 'F', 'S'):
            if r > 0 and maze[r - 1][c] in ('|', '7', 'F', 'L', 'J', 'S'):
                neighbors.append((r - 1, c))
            if r < rows - 1 and maze[r + 1][c] in ('|', 'L', 'J', '7', 'F', 'S'):
                neighbors.append((r + 1, c))
        if maze[r][c] in ('-', 'L', 'F', '7', 'J', 'S'):
            if c > 0 and maze[r][c - 1] in ('-', 'J', '7', 'L', 'F', 'S'):
                neighbors.append((r, c - 1))
            if c < cols - 1 and maze[r][c + 1] in ('-', 'F', 'L', '7', 'J', 'S'):
                neighbors.append((r, c + 1))

        if maze[r][c] in ('L', 'F', '7', 'J', 'S'):
            if r > 0 and c > 0 and maze[r-1][c-1] in ('L', '7', 'F', 'J', 'S'):
                if maze[r][c] in ('L', '7', 'S') and maze[r-1][c-1] in ('7', 'L','S', 'F','J'):
                    neighbors.append((r-1, c-1))
                elif maze[r][c] in ('J', 'F', 'S') and maze[r-1][c-1] in ('F', 'J', 'S','L','7'):
                    neighbors.append((r-1,c-1))
            if r < rows-1 and c < cols -1 and maze[r+1][c+1] in ('L', '7', 'F', 'J', 'S'):
                if maze[r][c] in ('L', '7', 'S') and maze[r+1][c+1] in ('L', '7','S', 'F', 'J'):
                    neighbors.append((r+1,c+1))
                elif maze[r][c] in ('J', 'F','S') and maze[r+1][c+1] in ('F','J','S', '7', 'L'):
                    neighbors.append((r+1,c+1))
            if r > 0 and c < cols - 1 and maze[r - 1][c + 1] in ('J', 'F','L', '7', 'S'):
                if maze[r][c] in ('J','F','S') and maze[r-1][c+1] in ('J','F','S', 'L','7'):
                    neighbors.append((r - 1, c + 1))
                elif maze[r][c] in ('L', '7','S') and maze[r-1][c+1] in ('L', '7','S','J','F'):
                    neighbors.append((r - 1, c + 1))

            if r < rows - 1 and c > 0 and maze[r + 1][c - 1] in ('J', 'F','L', '7', 'S'):
                if maze[r][c] in ('J','F','S') and maze[r + 1][c - 1] in ('F','J','S','7', 'L'):
                    neighbors.append((r + 1, c - 1))
                elif maze[r][c] in ('7', 'L', 'S') and maze[r+1][c-1] in ('7', 'L', 'S', 'J','F'):
                    neighbors.append((r + 1, c - 1))
        return neighbors

    q = [(start_row, start_col, 0)]
    visited = set()
    max_dist = 0
    while q:
        r, c, dist = q.pop(0)
        if (r, c) in visited:
            continue
        visited.add((r, c))
        max_dist = max(max_dist, dist)
        for nr, nc in get_neighbors(r, c):
            if (nr, nc) not in visited:
                q.append((nr, nc, dist + 1))

    return max_dist

def solution() -> int:
    maze_str = ""
    while True:
        try:
            line = input()
            maze_str += line + "\n"
        except EOFError:
            break

    result = furthest_point_in_pipe_maze(maze_str)
    return result