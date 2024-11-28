from typing import List

def farthest_point_in_loop(maze: str) -> int:
    maze_rows: List[str] = maze.splitlines()
    rows = len(maze_rows)
    cols = len(maze_rows[0])
    start = None
    for r in range(rows):
        for c in range(cols):
            if maze_rows[r][c] == 'S':
                start = (r, c)
                break
        if start:
            break

    graph = {}
    for r in range(rows):
        for c in range(cols):
            if maze_rows[r][c] != '.':
                neighbors = []
                if maze_rows[r][c] in ('|', 'L', 'J', 'S'):
                    if r > 0 and maze_rows[r - 1][c] != '.':
                        neighbors.append((r - 1, c))
                    if r < rows - 1 and maze_rows[r + 1][c] != '.':
                        neighbors.append((r + 1, c))
                if maze_rows[r][c] in ('-', 'L', 'F', 'S'):
                    if c > 0 and maze_rows[r][c - 1] != '.':
                        neighbors.append((r, c - 1))
                    if c < cols - 1 and maze_rows[r][c + 1] != '.':
                        neighbors.append((r, c + 1))
                if maze_rows[r][c] in ('J', '7', 'S'):
                    if r > 0 and c > 0 and maze_rows[r-1][c-1] != '.' and maze_rows[r][c] == 'S':
                        neighbors.append((r-1,c-1))
                    if r < rows -1 and c < cols -1 and maze_rows[r+1][c+1] != '.' and maze_rows[r][c] == 'S':
                        neighbors.append((r+1,c+1))
                if maze_rows[r][c] in ('F', '7', 'S'):
                     if r > 0 and c < cols -1 and maze_rows[r-1][c+1] != '.' and maze_rows[r][c] == 'S':
                        neighbors.append((r-1,c+1))
                     if r < rows -1 and c > 0 and maze_rows[r+1][c-1] != '.' and maze_rows[r][c] == 'S':
                        neighbors.append((r+1,c-1))
                graph[(r, c)] = neighbors

    distances = {start: 0}
    queue = [start]
    max_dist = 0
    farthest_node = start

    while queue:
        curr = queue.pop(0)
        for neighbor in graph[curr]:
            if neighbor not in distances:
                distances[neighbor] = distances[curr] + 1
                queue.append(neighbor)
                if distances[neighbor] > max_dist:
                    max_dist = distances[neighbor]
                    farthest_node = neighbor

    return max_dist

def solution() -> int:
    maze: str = ""
    while True:
        try:
            line = input()
            maze += line + "\n"
        except EOFError:
            break
    return farthest_point_in_loop(maze)
