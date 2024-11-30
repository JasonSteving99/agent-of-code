from typing import List, Tuple, Dict, Set

def build_loop_graph(maze_lines: List[str], r: int, c: int, graph: Dict[Tuple[int, int], List[Tuple[int, int]]], visited: Set[Tuple[int, int]], loop_members: Set[Tuple[int, int]]) -> None:
    rows = len(maze_lines)
    cols = len(maze_lines[0])
    current_pipe = maze_lines[r][c]
    visited.add((r, c))
    loop_members.add((r, c))
    if (r, c) not in graph:
        graph[(r, c)] = []

    valid_pipes = {
        '|' : [(1, 0), (-1, 0)],
        '-' : [(0, 1), (0, -1)],
        'L' : [(0, 1), (-1, 0)],
        'J' : [(0, -1), (-1, 0)],
        '7' : [(1, 0), (0, -1)],
        'F' : [(1, 0), (0, 1)],
        'S' : [(0, 1), (0, -1), (1, 0), (-1, 0)]
    }
    
    for dr, dc in valid_pipes.get(current_pipe, []):
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
            next_pipe = maze_lines[nr][nc]
            
            valid_reverse_pipes = {
                '|' : [(1, 0), (-1, 0)],
                '-' : [(0, 1), (0, -1)],
                'L' : [(0, -1), (1,0)],
                'J' : [(0, 1), (1, 0)],
                '7' : [(-1,0), (0, 1)],
                'F' : [(-1, 0), (0, -1)],
                'S' : [(0, 1), (0, -1), (1, 0), (-1, 0)]
            }
            
            ndr, ndc = r - dr, c -dc #we need the reverse
            
            if next_pipe == 'S' or current_pipe == 'S' or (ndr, ndc) in valid_reverse_pipes.get(next_pipe, []):
                graph[(r, c)].append((nr, nc))
                if (nr, nc) not in graph:
                    graph[(nr, nc)] = []
                graph[(nr, nc)].append((r, c))
                build_loop_graph(maze_lines, nr, nc, graph, visited, loop_members)


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
    loop_members = set()
    build_loop_graph(maze_lines, start[0], start[1], graph, visited, loop_members)

    q = [(start, 0)]
    visited = {start}
    max_dist = 0

    while q:
        (r, c), dist = q.pop(0)
        max_dist = max(max_dist, dist)

        for neighbor in graph.get((r, c), []):
            if neighbor not in visited and neighbor in loop_members:
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
