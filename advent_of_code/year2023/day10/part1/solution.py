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
    
    pipes = {'|': {0, 2}, '-': {1, 3}, 'L': {0, 1}, 'J': {0, 3}, '7': {2, 3}, 'F': {1, 2}}
    
    def get_neighbors(r, c):
        neighbors = []
        if maze[r][c] == 'S':
            symbol = ''
            if r > 0 and maze[r-1][c] != '.':
                symbol += '|' if maze[r-1][c] not in '7F' else '7' if maze[r-1][c] == '7' else 'F'
            if r < rows - 1 and maze[r+1][c] != '.':
                symbol += '|' if maze[r+1][c] not in 'LJ' else 'L' if maze[r+1][c] == 'L' else 'J'
            if c > 0 and maze[r][c-1] != '.':
                symbol += '-' if maze[r][c-1] not in 'JF' else 'J' if maze[r][c-1] == 'J' else 'F'
            if c < cols - 1 and maze[r][c+1] != '.':
                symbol += '-' if maze[r][c+1] not in 'L7' else 'L' if maze[r][c+1] == 'L' else '7'
                
            if len(symbol) > 2: return []
            if len(symbol) == 1: return []            
            if '|' in symbol and '-': symbol = 'L' if 'L' in "L-" else 'J' if 'J' in "J-" else 'F' if 'F' in 'F-' else '7'
            if len(symbol) == 0: return [] 
                
            
            for dr, dc, direction in [(0, 1, 1), (0, -1, 3), (1, 0, 2), (-1, 0, 0)]: 
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '.' and direction in pipes[symbol if symbol else maze[nr][nc]]:
                    neighbors.append((nr, nc))
        else:        
            for dr, dc, direction in [(0, 1, 1), (0, -1, 3), (1, 0, 2), (-1, 0, 0)]: 
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '.' and direction in pipes[maze[r][c]] and direction in pipes[maze[nr][nc] if maze[nr][nc] != 'S' else symbol]:
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

def solution() -> int:
    input_str = ""
    while True:
        try:
            line = input()
            input_str += line + "\n"
        except EOFError:
            break
    maze = input_str.strip().split('\n')

    result = solve(maze)

    return result