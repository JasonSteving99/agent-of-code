from typing import List

def max_loop_distance(maze: str) -> int:
    maze_lines = maze.splitlines()
    rows = len(maze_lines)
    cols = len(maze_lines[0])
    start = None
    for r in range(rows):
        for c in range(cols):
            if maze_lines[r][c] == 'S':
                start = (r, c)
                break
        if start is not None:
            break

    graph = {}
    q = [start]
    visited = {start}

    while q:
        r, c = q.pop(0)
        neighbors = []

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]: 
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze_lines[nr][nc] != '.':
                neighbors.append((nr, nc))

        if (r, c) not in graph:
            graph[(r, c)] = []

        for nr, nc in neighbors:
            if (nr, nc) not in graph:
                graph[(nr, nc)] = []
            graph[(r,c)].append((nr, nc))
            graph[(nr, nc)].append((r,c))
            if (nr, nc) not in visited:
                q.append((nr, nc))
                visited.add((nr, nc))
                
    
    q = [(start, 0)]
    visited = {start}
    max_dist = 0

    while q:
        (r, c), dist = q.pop(0)
        max_dist = max(max_dist, dist)

        for neighbor in graph.get((r,c), []):
            if neighbor not in visited:
                visited.add(neighbor)
                q.append((neighbor, dist + 1))

    return max_dist

def solution() -> int:
    maze_str = ""
    while True:
        try:
            line = input()
            maze_str += line + "\n"
        except EOFError:
            break
    return max_loop_distance(maze_str.strip())
