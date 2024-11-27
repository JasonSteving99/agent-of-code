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

    directions = {'|': ((-1, 0), (1, 0)), '-': ((0, -1), (0, 1)), 'L': ((-1, 0), (0, 1)),
                  'J': ((-1, 0), (0, -1)), '7': ((1, 0), (0, -1)), 'F': ((1, 0), (0, 1))}

    def get_neighbors(r, c):
        if maze[r][c] == 'S':
            possible_directions = []
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # Explore all 4 directions
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '.':
                    possible_directions.append((dr, dc))

            valid_neighbors = []
            for dr1, dc1 in possible_directions:
                for dr2, dc2 in possible_directions:
                    if (dr1, dc1) != (dr2, dc2) and (dr1 + dr2, dc1 + dc2) == (0, 0):  # Check for opposite direction
                        valid_neighbors = [(r + dr1, c + dc1), (r + dr2, c + dc2)]
                        return valid_neighbors

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
