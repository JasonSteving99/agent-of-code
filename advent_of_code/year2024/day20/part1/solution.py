```python
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

    def bfs(start_pos: Tuple[int, int], end_pos: Tuple[int, int]) -> Dict[Tuple[int, int], int]:
        distances = {start_pos: 0}
        queue = deque([start_pos])
        
        while queue:
            pos = queue.popleft()
            for next_pos in get_neighbors(pos):
                if next_pos not in distances:
                    distances[next_pos] = distances[pos] + 1
                    queue.append(next_pos)
        
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
            for r2 in range(max(0, r1-2), min(height, r1+3)):
                for c2 in range(max(0, c1-2), min(width, c1+3)):
                    end_pos = (r2, c2)
                    if abs(r2-r1) + abs(c2-c1) > 2:  # Manhattan distance check
                        continue

                    # Check if this is a valid cheat (ends on track)
                    if grid[r2][c2] != '.':
                        continue

                    if end_pos not in end_distances:
                        continue

                    # Calculate total path length with this cheat
                    cheat_path_length = (
                        start_distances[start_pos] +  # Path to cheat start
                        abs(r2-r1) + abs(c2-c1) +    # Cheat length (Manhattan distance)
                        end_distances[end_pos]        # Path from cheat end to goal
                    )

                    # Check if this cheat saves at least 100 picoseconds
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

```