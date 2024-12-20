from collections import deque
from typing import Dict, List, Set, Tuple


def count_effective_cheats(input_map: str) -> int:
    # Parse the map
    grid = [list(line) for line in input_map.splitlines()]
    height = len(grid)
    width = len(grid[0])

    # Find start and end positions
    start = end = None
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 'S':
                start = (i, j)
                grid[i][j] = '.'  # Convert to normal track
            elif grid[i][j] == 'E':
                end = (i, j)
                grid[i][j] = '.'  # Convert to normal track

    def get_neighbors(pos: Tuple[int, int], allow_walls: bool = False) -> List[Tuple[int, int]]:
        r, c = pos
        neighbors = []
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < height and 0 <= nc < width:
                if allow_walls or grid[nr][nc] == '.':
                    neighbors.append((nr, nc))
        return neighbors

    def bfs(start_pos: Tuple[int, int], end_pos: Tuple[int, int], allow_walls:bool = False) -> Dict[Tuple[int, int], int]:
        distances = {start_pos: 0}
        queue = deque([(start_pos, 0)])
        visited = {start_pos}
        
        while queue:
            pos, cheat_count = queue.popleft()
            for next_pos in get_neighbors(pos, allow_walls):
                if next_pos not in visited:
                    distances[next_pos] = distances[pos] + 1
                    visited.add(next_pos)
                    queue.append((next_pos, cheat_count+1 if allow_walls else 0))
        return distances

    # Calculate normal path distances from start and end
    start_distances = bfs(start, end)
    end_distances = bfs(end, start)

    if end not in start_distances:
        return 0  # No valid path exists

    normal_path_length = start_distances[end]
    effective_cheats = 0

    # For each possible cheat start position
    for r1 in range(height):
        for c1 in range(width):
            if grid[r1][c1] != '.':
                continue
            start_pos = (r1, c1)
            if start_pos not in start_distances:
                continue

            # Try all possible cheat end positions within 2 moves
            for r2 in range(height):
              for c2 in range(width):
                if abs(r2 - r1) + abs(c2 - c1) > 2:
                  continue
                if (r2,c2) == (r1, c1):
                    continue
                
                cheat_start = (r1,c1)
                cheat_end = (r2,c2)

                queue = deque([(cheat_start,0, 0)])
                visited = {cheat_start}
                min_cheat_dist = float('inf')
                
                while queue:
                  pos, cheat_count, dist = queue.popleft()
                  if cheat_count > 2:
                      continue
                  if grid[pos[0]][pos[1]] == '.' and cheat_count > 0:
                    min_cheat_dist = min(min_cheat_dist, dist + end_distances.get(pos, float('inf')))
                  
                  for next_pos in get_neighbors(pos, cheat_count < 2):
                    if next_pos not in visited:
                      visited.add(next_pos)
                      queue.append((next_pos, cheat_count +1, dist + 1))

                if min_cheat_dist == float('inf'):
                  continue
                  
                cheat_path_length = start_distances[cheat_start] + min_cheat_dist

                if normal_path_length - cheat_path_length >= 100:
                  effective_cheats += 1

    return effective_cheats


def solution() -> int:
    # Read input from stdin
    input_data = ""
    try:
        while True:
            line = input()
            input_data += line + "\n"
    except EOFError:
        pass
    
    return count_effective_cheats(input_data.rstrip())
