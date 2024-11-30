from typing import List

def solve(grid: List[str]) -> int:
    rows, cols = len(grid), len(grid[0])
    start_row, start_col = -1, -1
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start_row, start_col = r, c
                break

    def get_neighbors(r, c):
        neighbors = []
        for dr, dc, char1, char2 in [(0, 1, '-', '|'), (0, -1, '-', '|'), (1, 0, '|', '-'), (-1, 0, '|', '-')]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (grid[nr][nc] == char1 or grid[nr][nc] == char2 or grid[nr][nc] == 'S'):
                neighbors.append((nr, nc))
            elif 0 <= nr < rows and 0 <= nc < cols:
                if dr == 0 and dc == 1 and (grid[nr][nc] == 'L' or grid[nr][nc] == 'F' or grid[nr][nc] == 'J' or grid[nr][nc] == '7'):
                        neighbors.append((nr,nc))
                elif dr == 0 and dc == -1 and (grid[nr][nc] == 'L' or grid[nr][nc] == 'F' or grid[nr][nc] == 'J' or grid[nr][nc] == '7'):
                    neighbors.append((nr, nc))
                elif dr == 1 and dc == 0 and (grid[nr][nc] == 'L' or grid[nr][nc] == 'F' or grid[nr][nc] == 'J' or grid[nr][nc] == '7'):
                    neighbors.append((nr, nc))
                elif dr == -1 and dc == 0 and (grid[nr][nc] == 'L' or grid[nr][nc] == 'F' or grid[nr][nc] == 'J' or grid[nr][nc] == '7'):
                    neighbors.append((nr, nc))

        return neighbors

    q = [(start_row, start_col, 0)]
    visited = set([(start_row, start_col)])
    max_dist = 0

    while q:
        r, c, dist = q.pop(0)
        max_dist = max(max_dist, dist)

        for nr, nc in get_neighbors(r, c):
            if (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc, dist + 1))

    return max_dist

def max_steps_in_loop(grid_str: str) -> int:
    grid = grid_str.strip().split('\n')
    return solve(grid)

def solution() -> int:
    grid_str = "" 
    while True:
        try:
           line = input()
           grid_str += line + "\n"
        except EOFError:
            break

    return max_steps_in_loop(grid_str)
