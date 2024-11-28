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
                char = maze_rows[r][c]
                if char in ('|', 'L', 'J', '7', 'F', 'S'):
                    if r > 0 and maze_rows[r - 1][c] != '.':
                        neighbors.append((r - 1, c))
                    if r < rows - 1 and maze_rows[r + 1][c] != '.':
                        neighbors.append((r + 1, c))
                if char in ('-', 'L', 'F', 'J', '7', 'S'):
                    if c > 0 and maze_rows[r][c - 1] != '.':
                        neighbors.append((r, c - 1))
                    if c < cols - 1 and maze_rows[r][c + 1] != '.':
                        neighbors.append((r, c + 1))
                graph[(r, c)] = neighbors

    if start:
        r, c = start
        pipe_type_start = ''
        neighbors_start = graph[start]
        
        # Check vertical and horizontal neighbors
        if (r > 0 and (r - 1, c) in neighbors_start) or (r < rows - 1 and (r + 1, c) in neighbors_start):
            pipe_type_start += '|'
        if (c > 0 and (r, c - 1) in neighbors_start) or (c < cols - 1 and (r, c + 1) in neighbors_start):
            pipe_type_start += '-'

        # Check for diagonal neighbors ONLY if no direct vertical or horizontal neighbors found
        if not pipe_type_start:
            for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:  # check diagonals
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze_rows[nr][nc] != '.':
                    # Infer pipe type based on diagonal
                    if dr == -1 and dc == -1:
                        pipe_type_start = '7'
                    elif dr == -1 and dc == 1:
                        pipe_type_start = 'J'
                    elif dr == 1 and dc == -1:
                        pipe_type_start = 'L'
                    elif dr == 1 and dc == 1:
                        pipe_type_start = 'F'
                    
                    graph[start] = [(nr, nc)] #set the neighbors to the found diagonal
                    break # only one diagonal
        else:
            graph[start] = []
            for nr, nc in neighbors_start:
                if maze_rows[nr][nc] != '.':
                    if ('|' in pipe_type_start and nr == r) or ('-' in pipe_type_start and nc == c):
                        continue  # Skip horizontal/vertical connection if it is part of a L,F,7,J shape
                    graph[start].append((nr, nc))

    distances = {start: 0} if start is not None else {}
    queue = [start] if start is not None else []
    max_dist = 0
    farthest_node = start

    while queue:
        curr = queue.pop(0)
        if curr not in graph:
            break # Handle cases where start is not defined properly
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
