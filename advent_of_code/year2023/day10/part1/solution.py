from typing import List


def solve(maze: List[str]) -> int:
    rows = len(maze)
    cols = len(maze[0])
    start = (-1, -1)  # Initialize with a default value
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
                break
        if start != (-1, -1):
            break

    if start == (-1, -1):  # 'S' not found
        raise ValueError("Start position 'S' not found in the maze.")

    directions = {'|': ((-1, 0), (1, 0)), '-': ((0, -1), (0, 1)), 'L': ((-1, 0), (0, 1)),
                  'J': ((-1, 0), (0, -1)), '7': ((1, 0), (0, -1)), 'F': ((1, 0), (0, 1))}

    def get_neighbors(r, c):
        if maze[r][c] == 'S':
            possible_directions = []
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # Explore all 4 directions
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '.':
                    possible_directions.append((dr, dc))
            
            if len(possible_directions) != 2:
                raise ValueError("Invalid number of connections to 'S'")  # or handle it differently

            dr1, dc1 = possible_directions[0]
            dr2, dc2 = possible_directions[1]
            
            if (dr1, dc1) == (-dr2, -dc2):
                if dr1 == 1:
                    maze[r] = maze[r][:c] + '|' + maze[r][c+1:]
                elif dr1 == -1:
                    maze[r] = maze[r][:c] + '|' + maze[r][c+1:]
                elif dc1 == 1:
                    maze[r] = maze[r][:c] + '-' + maze[r][c+1:]
                else:
                    maze[r] = maze[r][:c] + '-' + maze[r][c+1:]
                    
                return [(r+dr1, c+dc1), (r+dr2, c+dc2)]
            
            for dr1, dc1 in possible_directions:
                for dr2, dc2 in possible_directions:
                    if (dr1, dc1) != (dr2, dc2) and (dr1 + dr2, dc1 + dc2) == (0,0): #check for valid pipe
                        if dr1 == -1 and dc2 == 1:
                            maze[r] = maze[r][:c] + 'L' + maze[r][c+1:]
                        elif dr1 == -1 and dc2 == -1:
                            maze[r] = maze[r][:c] + 'J' + maze[r][c+1:]
                        elif dr1 == 1 and dc2 == -1:
                            maze[r] = maze[r][:c] + '7' + maze[r][c+1:]
                        else:
                            maze[r] = maze[r][:c] + 'F' + maze[r][c+1:]

                        return [(r + dr1, c + dc1), (r + dr2, c + dc2)]
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

