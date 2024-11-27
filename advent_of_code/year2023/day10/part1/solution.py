from typing import List, Tuple

def get_neighbors(maze: List[str], row: int, col: int) -> List[Tuple[int, int]]:
    rows = len(maze)
    cols = len(maze[0])
    neighbors = []
    piece = maze[row][col]

    if piece in ['|', 'S', 'L', 'J']:
        if row > 0 and maze[row - 1][col] in ['|', 'S', '7', 'F', 'L', 'J', '-']:
            neighbors.append((row - 1, col))
    if piece in ['|', 'S', '7', 'F']:
        if row < rows - 1 and maze[row + 1][col] in ['|', 'S', '7', 'F', 'L', 'J', '-']:
            neighbors.append((row + 1, col))
    if piece in ['-', 'S', 'F', 'L']:
        if col < cols - 1 and maze[row][col + 1] in ['|', 'S', '7', 'F', 'L', 'J', '-']:
            neighbors.append((row, col + 1))
    if piece in ['-', 'S', '7', 'J']:
        if col > 0 and maze[row][col - 1] in ['|', 'S', '7', 'F', 'L', 'J', '-']:
            neighbors.append((row, col - 1))

    return neighbors

def max_steps_in_pipe_loop(maze_str: str) -> int:
    maze = [row.rstrip() for row in maze_str.strip().splitlines()]
    rows = len(maze)
    cols = 0
    start_row, start_col = -1, -1
    for r in range(rows):
        cols = max(cols, len(maze[r]))
        for c in range(len(maze[r])):  # Iterate up to current row length
            if maze[r][c] == 'S':
                start_row, start_col = r, c
                break
        if start_row != -1:
            break

    if start_row == -1:
        return 0

    q = [((start_row, start_col), 0)]
    visited = {(start_row, start_col)}
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

    return max_steps_in_pipe_loop(maze_str)
