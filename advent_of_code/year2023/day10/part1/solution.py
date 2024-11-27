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
            tile = '|'
        
        if r > 0 and maze[r-1][c] != '.':
            neighbor_tile = maze[r-1][c]
            if neighbor_tile == 'S': neighbor_tile = '|'
            if (tile in '|7FJ' and neighbor_tile in '|LJ7') or (neighbor_tile in '|7FJ' and tile in '|LJ7'):
                neighbors.append((r - 1, c))
        if r < rows - 1 and maze[r+1][c] != '.':
            neighbor_tile = maze[r+1][c]
            if neighbor_tile == 'S': neighbor_tile = '|'
            if (tile in '|LF' and neighbor_tile in '|7LF') or (neighbor_tile in '|LF' and tile in '|7LF'):
                neighbors.append((r + 1, c))
        if c > 0 and maze[r][c-1] != '.':
            neighbor_tile = maze[r][c-1]
            if neighbor_tile == 'S': neighbor_tile = '|'
            if (tile in '-LJ7' and neighbor_tile in '-7FJ') or (neighbor_tile in '-LJ7' and tile in '-7FJ'):
                neighbors.append((r, c - 1))
        if c < cols - 1 and maze[r][c+1] != '.':
            neighbor_tile = maze[r][c+1]
            if neighbor_tile == 'S': neighbor_tile = '|'
            if (tile in '-LF' and neighbor_tile in '-LJF') or (neighbor_tile in '-LF' and tile in '-LJF'):
                neighbors.append((r, c + 1))
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
