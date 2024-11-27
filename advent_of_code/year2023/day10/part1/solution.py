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

        if maze[r][c] == 'S':
            possible_pipes = ['|', '-', 'L', 'J', '7', 'F']
            for pipe in possible_pipes:
                temp_maze = [row[:] for row in maze]  # create a copy to avoid modifying the original
                temp_maze[r] = temp_maze[r][:c] + pipe + temp_maze[r][c + 1:]
                current_neighbors = []

                allowed_moves = {
                    '|': {(-1, 0), (1, 0)},
                    '-': {(0, -1), (0, 1)},
                    'L': {(-1, 0), (0, 1)},
                    'J': {(-1, 0), (0, -1)},
                    '7': {(1, 0), (0, -1)},
                    'F': {(1, 0), (0, 1)},
                }

                for dr, dc in allowed_moves[pipe]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and temp_maze[nr][nc] != '.':
                        neighbor_tile = temp_maze[nr][nc]
                        if neighbor_tile == 'S':
                            neighbor_tile = pipe # Fix: Set S to current testing pipe
                        if (dr, dc) in allowed_moves.get(neighbor_tile, {}) or (-dr, -dc) in allowed_moves.get(pipe, {}):
                            current_neighbors.append((nr, nc))
                if len(current_neighbors) == 2:
                    neighbors = current_neighbors
                    break # Only find one valid pipe type for S
            return neighbors

        tile = maze[r][c]
        allowed_moves = {
            '|': {(-1, 0), (1, 0)},
            '-': {(0, -1), (0, 1)},
            'L': {(-1, 0), (0, 1)},
            'J': {(-1, 0), (0, -1)},
            '7': {(1, 0), (0, -1)},
            'F': {(1, 0), (0, 1)},
        }

        for dr, dc in allowed_moves[tile]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '.':
                neighbor_tile = maze[nr][nc]
                if (dr, dc) in allowed_moves.get(neighbor_tile, {}) or (-dr, -dc) in allowed_moves.get(tile, {}):
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
