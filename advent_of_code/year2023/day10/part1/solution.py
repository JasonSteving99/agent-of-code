from typing import List, Tuple, Dict

def build_loop_graph(maze_lines: List[str], r: int, c: int, graph: Dict[Tuple[int, int], List[Tuple[int, int]]], visited: set) -> None:
    rows = len(maze_lines)
    cols = len(maze_lines[0])

    visited.add((r, c))
    if (r, c) not in graph:
        graph[(r, c)] = []

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]: 
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and maze_lines[nr][nc] != '.' and (nr, nc) not in visited:
            graph[(r, c)].append((nr, nc))
            if (nr, nc) not in graph:
                graph[(nr, nc)] = []
            graph[(nr, nc)].append((r, c))
            build_loop_graph(maze_lines, nr, nc, graph, visited)

def max_loop_distance(maze: str) -> int:
    maze_lines = maze.splitlines()
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

    graph = {}
    visited = set()
    build_loop_graph(maze_lines, start[0], start[1], graph, visited)

    q = [(start, 0)]
    visited = {start}
    max_dist = 0

    while q:
        (r, c), dist = q.pop(0)
        max_dist = max(max_dist, dist)

        for neighbor in graph.get((r, c), []):
            if neighbor not in visited:
                visited.add(neighbor)
                q.append((neighbor, dist + 1))

    return max_dist

def solution() -> int:
    maze_str = ""
    while True:
        try:
            line = input()
            maze_str += line + "\n"
        except EOFError:
            break
    return max_loop_distance(maze_str.strip())
