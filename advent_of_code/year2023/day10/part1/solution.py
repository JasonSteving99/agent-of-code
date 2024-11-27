from typing import List

def max_loop_distance(maze: str) -> int:
    maze_lines = maze.splitlines()
    rows = len(maze_lines)
    cols = len(maze_lines[0])

    start_row, start_col = -1, -1
    for r in range(rows):
        for c in range(cols):
            if maze_lines[r][c] == 'S':
                start_row, start_col = r, c
                break
        if start_row != -1:
            break

    if start_row == -1:
        return 0  # Handle cases where 'S' is not found

    def get_neighbors(r, c):
        neighbors = []
        for dr, dc, pipe_char in [(0, 1, '-'), (0, -1, '-'), (1, 0, '|'), (-1, 0, '|')]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbor_char = maze_lines[nr][nc]
                if neighbor_char != '.':
                    if neighbor_char == 'S' or neighbor_char == pipe_char or \
                       (pipe_char == '|' and neighbor_char in 'LJ7F') or \
                       (pipe_char == '-' and neighbor_char in '7FJL'):
                        neighbors.append((nr, nc))
        return neighbors

    q = [((start_row, start_col), 0)]
    visited = {(start_row, start_col)}
    max_dist = 0

    while q:
        (r, c), dist = q.pop(0)
        max_dist = max(max_dist, dist)
        for nr, nc in get_neighbors(r, c):
            if (nr, nc) not in visited:

                neighbor_count = len(get_neighbors(nr, nc))           
                is_start = maze_lines[nr][nc] == 'S'
                if  is_start or neighbor_count == 2:
                    visited.add((nr, nc))
                    q.append(((nr, nc), dist + 1))

    return max_dist

def solution() -> int:
    maze_str: str = ""
    while True:
        try:
            line = input()
            maze_str += line + "\n"
        except EOFError:
            break
    return max_loop_distance(maze_str)