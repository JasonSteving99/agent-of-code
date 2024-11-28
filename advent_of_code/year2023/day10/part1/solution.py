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
        if start:
            break
    
    pipes = {'|': {(-1, 0), (1, 0)}, '-': {(0, -1), (0, 1)}, 'L': {(1, 0), (0, 1)}, 'J': {(1, 0), (0, -1)}, '7': {(-1, 0), (0, -1)}, 'F': {(-1, 0), (0, 1)}}
    
    def get_neighbors(r: int, c: int) -> List[tuple[int, int]]:
        neighbors = []
        for dr, dc in pipes.get(maze[r][c], []):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (dr, dc) in pipes.get(maze[nr][nc], []):
                neighbors.append((nr, nc))
        return neighbors
    
    q = [(start, 0)]
    visited = {start}
    max_dist = 0
    
    while q:
        (r, c), dist = q.pop(0)
        max_dist = max(max_dist, dist)
        
        for nr, nc in get_neighbors(r, c):
            if (nr, nc) != start and (nr, nc) in visited:
                continue
            visited.add((nr, nc))
            q.append(((nr, nc), dist + 1))
            

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
