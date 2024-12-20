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

    def bfs(start_pos: Tuple[int, int], allow_walls: bool = False) -> Dict[Tuple[int, int], int]:
        distances = {start_pos: 0}
        queue = deque([(start_pos, 0)])
        visited = {start_pos}

        while queue:
            pos, cheat_steps = queue.popleft()
            for next_pos in get_neighbors(pos, allow_walls and cheat_steps < 2):
                if next_pos not in visited:
                  distances[next_pos] = distances[pos] + 1
                  visited.add(next_pos)
                  queue.append((next_pos, cheat_steps+1 if allow_walls else 0))
        return distances

    # Calculate normal path distances from start to end
    start_distances = bfs(start)
    if end not in start_distances:
        return 0
    normal_path_length = start_distances[end]

    effective_cheats = 0
    visited_cheats = set()
    queue = deque([(start,0)])
    visited_positions = {start}
    
    while queue:
        current_pos, current_dist = queue.popleft()
        for next_pos in get_neighbors(current_pos):
          if next_pos not in visited_positions:
            visited_positions.add(next_pos)
            queue.append((next_pos, current_dist+1))

        for r2 in range(height):
          for c2 in range(width):
            if abs(r2 - current_pos[0]) + abs(c2 - current_pos[1]) > 2:
                continue
            if (r2,c2) == current_pos:
                continue

            cheat_start = current_pos
            cheat_end = (r2,c2)

            cheat_distances = bfs(cheat_start, True)

            if cheat_end not in cheat_distances:
                continue
            
            min_dist_end = float('inf')
            for p, dist in cheat_distances.items():
              if dist <=2 and grid[p[0]][p[1]]=='.':
                remaining_dist_to_end = bfs(p).get(end, float('inf'))
                min_dist_end = min(min_dist_end, dist + remaining_dist_to_end)
            
            if min_dist_end == float('inf'):
                continue
            
            cheat_path_length = current_dist + min_dist_end
            if normal_path_length - cheat_path_length >= 100 and (cheat_start, cheat_end) not in visited_cheats:
              effective_cheats += 1
              visited_cheats.add((cheat_start, cheat_end))

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
