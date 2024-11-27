from typing import List


def solve(maze: List[str]) -> int:
    rows = len(maze)
    cols = len(maze[0])
    start = (-1, -1)
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
                break
        if start != (-1, -1):
            break

    if start == (-1, -1):
        raise ValueError("Start position 'S' not found in the maze.")

    directions = {'|': ((-1, 0), (1, 0)), '-': ((0, -1), (0, 1)), 'L': ((-1, 0), (0, 1)),
                  'J': ((-1, 0), (0, -1)), '7': ((1, 0), (0, -1)), 'F': ((1, 0), (0, 1))}

    def get_neighbors(r, c):
        if maze[r][c] == 'S':
            neighbors = []
            connected_pipes = []
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # Check surrounding pipes to infer 'S' type
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '.':
                    connected_pipes.append((dr, dc))

            if len(connected_pipes) == 2:
                if tuple(sorted(connected_pipes)) == ((-1, 0), (1, 0)):
                    current_directions = directions['|']
                elif tuple(sorted(connected_pipes)) == ((0, -1), (0, 1)):
                    current_directions = directions['-']
                elif tuple(sorted(connected_pipes)) == ((-1, 0), (0, -1)):
                    current_directions = directions['J']
                elif tuple(sorted(connected_pipes)) == ((-1, 0), (0, 1)):
                    current_directions = directions['L']
                elif tuple(sorted(connected_pipes)) == ((1, 0), (0, -1)):
                    current_directions = directions['7']
                elif tuple(sorted(connected_pipes)) == ((0, 1), (1, 0)):
                    current_directions = directions['F']
                else:
                    raise ValueError("Start position 'S' is invalid because it's not connected to a valid pipe.")

                for dr, dc in current_directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '.':
                        neighbors.append((nr, nc))
            else:
                raise ValueError("Start position 'S' is invalid because it's not connected to exactly two pipes.")
            return neighbors

        else:
            neighbors = []
            for dr, dc in directions[maze[r][c]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '.':
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


def max_steps_in_loop(maze: str) -> int:
    maze_lines = maze.splitlines()
    return solve(maze_lines)


def solution() -> int:
    maze_lines: List[str] = []
    while True:
        try:
            line = input()
            maze_lines.append(line)
        except EOFError:
            break

    result = solve(maze_lines)
    return result
