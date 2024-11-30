from typing import List

def solve(maze: List[str]) -> int:
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
        if maze[r][c] in ('|', 'L', 'J', 'S'):
            if r > 0 and maze[r-1][c] in ('|', '7', 'F', 'S'):
                neighbors.append((r-1, c))
            if r < rows -1 and maze[r+1][c] in ('|', 'L', 'J', 'S'):
                neighbors.append((r+1, c))
        if maze[r][c] in ('-', 'L', 'F', 'S'):
            if c > 0 and maze[r][c-1] in ('-', 'J', '7', 'S'):
                neighbors.append((r, c-1))
            if c < cols -1 and maze[r][c+1] in ('-', 'F', 'L', 'S'):
                neighbors.append((r, c+1))
        if maze[r][c] in ('7', 'J', 'S'):
             if r < rows - 1 and c > 0 and maze[r+1][c-1] in ('7', 'L', 'F', 'J','S'):
                 neighbors.append((r+1,c-1))
             if r > 0 and c < cols -1 and maze[r-1][c+1] in ('7', 'L', 'F', 'J', 'S'):
                 neighbors.append((r-1, c+1))
        if maze[r][c] in ('F', 'L', 'S'):
            if r < rows - 1 and c < cols - 1 and maze[r+1][c+1] in ('F', 'L', 'J', '7', 'S'):
                neighbors.append((r+1, c+1))
            if r > 0 and c > 0 and maze[r-1][c-1] in ('F', 'L', 'J', '7', 'S'):
                 neighbors.append((r-1, c-1))           
        return neighbors
    
    q = [(start_row, start_col, 0)]
    visited = set()
    max_dist = 0
    while q:
        r, c, dist = q.pop(0)
        if (r, c) in visited:
            continue
        visited.add((r,c))
        max_dist = max(max_dist, dist)
        for nr, nc in get_neighbors(r,c):
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
    maze = maze_str.strip().split('\n')
    result = solve(maze)
    return result