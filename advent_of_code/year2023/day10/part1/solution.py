from typing import List, Tuple

def get_neighbors(maze: List[str], row: int, col: int) -> List[Tuple[int, int]]:
    rows = len(maze)
    cols = len(maze[0])
    neighbors = []
    piece = maze[row][col]

    if piece in ['|', 'S', 'L', 'J']:
        if row > 0 and maze[row - 1][col] != '.':
            neighbors.append((row - 1, col))
    if piece in ['|', 'S', '7', 'F']:
        if row < rows - 1 and maze[row + 1][col] != '.':
            neighbors.append((row + 1, col))
    if piece in ['-', 'S', 'F', 'L']:
        if col < cols - 1 and maze[row][col + 1] != '.':
            neighbors.append((row, col + 1))
    if piece in ['-', 'S', '7', 'J']:
        if col > 0 and maze[row][col - 1] != '.':
            neighbors.append((row, col - 1))

    return neighbors

def max_steps_in_pipe_loop(maze: List[str]) -> int:
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

    while q:
        (r, c), dist = q.pop(0)
        max_dist = max(max_dist, dist)

        for nr, nc in get_neighbors(maze, r, c):
            if (nr, nc) not in visited:
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
    return max_steps_in_pipe_loop(maze)
