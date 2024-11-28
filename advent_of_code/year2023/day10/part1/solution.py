from typing import List, Tuple

def solve(maze: List[str]) -> int:
    rows = len(maze)
    cols = len(maze[0])

    start_row, start_col = -1, -1
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start_row, start_col = r, c
                break

    graph = {}
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] != '.':
                neighbors = []
                if maze[r][c] in ('-', 'L', 'J', 'S'):  # Check north
                    if r > 0 and maze[r - 1][c] != '.':
                        neighbors.append((r - 1, c))
                if maze[r][c] in ('-', 'F', '7', 'S'):  # Check south
                    if r < rows - 1 and maze[r + 1][c] != '.':
                        neighbors.append((r + 1, c))
                if maze[r][c] in ('|', 'L', 'F', 'S'):  # Check east
                    if c < cols - 1 and maze[r][c + 1] != '.':
                        neighbors.append((r, c + 1))
                if maze[r][c] in ('|', 'J', '7', 'S'):  # Check west
                    if c > 0 and maze[r][c - 1] != '.':
                        neighbors.append((r, c - 1))
                graph[(r, c)] = neighbors

    distances = {node: -1 for node in graph}
    distances[(start_row, start_col)] = 0
    queue = [(start_row, start_col)]

    while queue:
        current = queue.pop(0)
        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    max_distance = 0
    for distance in distances.values():
        max_distance = max(max_distance, distance)

    return max_distance

def solution() -> int:
    maze: List[str] = []
    while True:
        try:
            line = input()
            maze.append(line)
        except EOFError:
            break
    return solve(maze)
