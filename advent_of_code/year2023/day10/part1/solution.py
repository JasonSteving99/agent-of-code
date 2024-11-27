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
        return 0

    def get_neighbors(r, c):
        neighbors = []
        possible_pipes = []
        if maze_lines[r][c] == 'S':
            possible_pipes = ['-', '|', 'L', 'J', '7', 'F']
        elif maze_lines[r][c] == '-':
            possible_pipes = ['-', 'L', 'J', '7', 'F']
        elif maze_lines[r][c] == '|':
            possible_pipes = ['|', 'L', 'J', '7', 'F']
        elif maze_lines[r][c] in ('L','J','7','F'):
            possible_pipes = ['-', '|', 'L', 'J', '7', 'F']            

        for dr, dc, char in [(0, 1, '-'), (0, -1, '-'), (1, 0, '|'), (-1, 0, '|')]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbor_char = maze_lines[nr][nc]
                if neighbor_char != '.':
                    if (char == '-' and neighbor_char in possible_pipes and (neighbor_char == '-' or
                        (neighbor_char == 'L' and dc == 1) or (neighbor_char == 'J' and dc == -1) or
                        (neighbor_char == '7' and dr == 1) or (neighbor_char == 'F' and dr == 1))) or \
                    (char == '|' and neighbor_char in possible_pipes and (neighbor_char == '|' or
                        (neighbor_char == 'L' and dc == -1) or (neighbor_char == 'J' and dc == 1) or
                        (neighbor_char == '7' and dr == -1) or (neighbor_char == 'F' and dc == -1))):
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