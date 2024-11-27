from typing import List, Tuple, Dict


def solve(maze: List[str]) -> int:
    rows = len(maze)
    cols = len(maze[0])
    start: Tuple[int, int] = (-1, -1)
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
                break
        if start != (-1, -1):
            break

    if start == (-1, -1):
        raise ValueError("Start position 'S' not found in the maze.")

    r, c = start

    connected_pipes = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # Check surrounding pipes to infer 'S' type
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '.':
            connected_pipes.append((dr, dc))

    if len(connected_pipes) != 2:
        raise ValueError("Invalid input: 'S' must be connected to exactly two pipes.")
    
    s_type = ""
    if tuple(sorted(connected_pipes)) == ((-1, 0), (1, 0)):
        s_type = "|"
    elif tuple(sorted(connected_pipes)) == ((0, -1), (0, 1)):
        s_type = "-"
    elif tuple(sorted(connected_pipes)) == ((-1, 0), (0, -1)):
        s_type = "J"
    elif tuple(sorted(connected_pipes)) == ((-1, 0), (0, 1)):
        s_type = "L"
    elif tuple(sorted(connected_pipes)) == ((1, 0), (0, -1)):
        s_type = "7"
    elif tuple(sorted(connected_pipes)) == ((0, 1), (1, 0)):
         s_type = "F"
    else:
        raise ValueError("Invalid input: Invalid pipe configuration around 'S'")

    directions: Dict[str, Tuple[Tuple[int, int], Tuple[int, int]]] = {
        '|': ((-1, 0), (1, 0)), '-': ((0, -1), (0, 1)),
        'L': ((-1, 0), (0, 1)), 'J': ((-1, 0), (0, -1)),
        '7': ((1, 0), (0, -1)), 'F': ((1, 0), (0, 1))
    }

    def get_neighbors(r: int, c: int) -> List[Tuple[int, int]]:
        current_type = maze[r][c]
        if current_type == 'S':
            current_type = s_type
            
        neighbors = []
        for dr, dc in directions[current_type]:
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
