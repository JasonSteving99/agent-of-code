"""Solution for pipe maze maximum loop distance problem."""

from collections import deque
from typing import Dict, List, Set, Tuple


def infer_pipe_type(grid: List[str], x: int, y: int) -> str:
    """Infer the pipe type at (x, y) based on neighbors."""
    rows, cols = len(grid), len(grid[0])
    possible_connections = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # N, S, W, E
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '.':
            possible_connections.append((dx, dy))

    if len(possible_connections) == 0:
        return '.'  # Isolated, treat as ground
    elif len(possible_connections) == 2:
        if tuple(-dx for dx, _ in possible_connections) == tuple(dy for _, dy in possible_connections):
            return '|' if possible_connections[0][1] == 0 else '-'
        elif possible_connections == [(-1, 0), (0, 1)]: return 'L'
        elif possible_connections == [(-1, 0), (0, -1)]: return 'J'
        elif possible_connections == [(1, 0), (0, -1)]: return '7'
        elif possible_connections == [(1, 0), (0, 1)]: return 'F'
    # If no specific type can be inferred, assume all are possible (like 'S')
    return 'S'


def max_loop_distance(grid_str: str) -> int:
    """Calculate maximum distance within pipe loop from start position."""
    grid = grid_str.strip().split('\n')
    rows, cols = len(grid), len(grid[0])

    start_pos = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start_pos = (r, c)
                break
        if start_pos: break

    if not start_pos:
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '.':
                    start_pos = (r, c)
                    break
            if start_pos: break

    if not start_pos: return 0  # No pipes at all

    connections = {
        '|': [(-1, 0), (1, 0)], '-': [(0, -1), (0, 1)],
        'L': [(-1, 0), (0, 1)], 'J': [(-1, 0), (0, -1)],
        '7': [(1, 0), (0, -1)], 'F': [(1, 0), (0, 1)],
        'S': [(-1, 0), (1, 0), (0, -1), (0, 1)]
    }

    def is_valid(r, c): return 0 <= r < rows and 0 <= c < cols

    def can_connect(from_pos, to_pos):
        fr, fc = from_pos
        tr, tc = to_pos
        from_pipe = infer_pipe_type(grid, fr, fc) if grid[fr][fc] == 'S' else grid[fr][fc]
        to_pipe = infer_pipe_type(grid, tr, tc) if grid[tr][tc] == 'S' else grid[tr][tc]
        if from_pipe not in connections or to_pipe not in connections: return False
        dr, dc = tr - fr, tc - fc
        return (dr, dc) in connections[from_pipe] and (-dr, -dc) in connections[to_pipe]

    distances = {start_pos: 0}
    q = deque([start_pos])
    visited = {start_pos}
    while q:
        curr = q.popleft()
        cr, cc = curr
        for dr, dc in connections[infer_pipe_type(grid, cr, cc) if grid[cr][cc] == 'S' else grid[cr][cc]]:
            nr, nc = cr + dr, cc + dc
            if is_valid(nr, nc) and (nr, nc) not in visited and can_connect(curr, (nr, nc)):
                distances[(nr, nc)] = distances[curr] + 1
                visited.add((nr, nc))
                q.append((nr, nc))

    return max(distances.values())


def solution() -> int:
    import sys
    return max_loop_distance(sys.stdin.read())
