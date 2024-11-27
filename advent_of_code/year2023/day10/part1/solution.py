from typing import List

def max_loop_distance(maze: str) -> int:
    maze_lines = maze.strip().split('\n')
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

    if start is None:
        return 0

    pipes = {'|': {0, 2}, '-': {1, 3}, 'L': {0, 1}, 'J': {0, 3}, '7': {2, 3}, 'F': {1, 2}, 'S': {0, 1, 2, 3}}

    def get_neighbors(r, c):
        neighbors = []
        current_symbol = maze_lines[r][c]

        if current_symbol == 'S':
            symbol = ''
            if r > 0 and maze_lines[r - 1][c] != '.':
                symbol += '|' if maze_lines[r - 1][c] not in '7F' else '7' if maze_lines[r - 1][c] == '7' else 'F'
            if r < rows - 1 and maze_lines[r + 1][c] != '.':
                symbol += '|' if maze_lines[r + 1][c] not in 'LJ' else 'L' if maze_lines[r + 1][c] == 'L' else 'J'
            if c > 0 and maze_lines[r][c - 1] != '.':
                symbol += '-' if maze_lines[r][c - 1] not in 'JF' else 'J' if maze_lines[r][c - 1] == 'J' else 'F'
            if c < cols - 1 and maze_lines[r][c + 1] != '.':
                symbol += '-' if maze_lines[r][c + 1] not in 'L7' else 'L' if maze_lines[r][c + 1] == 'L' else '7'

            if len(symbol) > 2 or len(symbol) < 2:
                return []  # Invalid 'S' connection
            if '|' in symbol and '-':
                symbol = 'L' if 'L' in "L-" else 'J' if 'J' in "J-" else 'F' if 'F' in 'F-' else '7'

            for dr, dc, direction in [(0, 1, 1), (0, -1, 3), (1, 0, 2), (-1, 0, 0)]: 
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze_lines[nr][nc] != '.' and direction in pipes[symbol]:
                    neighbors.append((nr, nc))
        else:
            for dr, dc, direction in [(0, 1, 1), (0, -1, 3), (1, 0, 2), (-1, 0, 0)]: 
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze_lines[nr][nc] != '.' and direction in pipes[current_symbol if current_symbol != 'S' else symbol ] and direction in pipes[maze_lines[nr][nc] if maze_lines[nr][nc] != 'S' else symbol]:
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

    result = max_loop_distance(input_str)

    return result
