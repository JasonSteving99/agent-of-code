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

    q = [(start, 0)]
    visited = {start}
    max_dist = 0
    graph = {}

    while q:
        (r, c), dist = q.pop(0)
        max_dist = max(max_dist, dist)

        neighbors = []
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # Check all 4 directions
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] != '.':
                    neighbors.append((nr, nc))
                    
        if (r,c) not in graph:
            graph[(r,c)] = []
        
        if len(neighbors) == 2:
            for nr, nc in neighbors:
                if (nr, nc) not in visited:
                    q.append(((nr, nc), dist + 1))
                    visited.add((nr, nc))
                    if (nr,nc) not in graph:
                        graph[(nr,nc)] = []
                    graph[(r,c)].append((nr,nc))
                    graph[(nr,nc)].append((r,c))
                    
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
    maze = maze_str.strip().split('\n')
    return solve(maze)
