from collections import deque
from typing import Dict, List, Set, Tuple, Optional

def get_start_end_positions(grid: List[str]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    start = end = None
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (i, j)
            elif cell == 'E':
                end = (i, j)
            if start and end:
                break
    return start, end

def find_shortest_path(grid: List[str], start: Tuple[int, int], end: Tuple[int, int]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue: deque[Tuple[int, int, int]] = deque([(start[0], start[1], 0)])
    visited: Set[Tuple[int, int]] = {start}
    
    while queue:
        r, c, steps = queue.popleft()
        if (r, c) == end:
            return steps
            
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and 
                (nr, nc) not in visited and 
                grid[nr][nc] in '.SE'):
                visited.add((nr, nc))
                queue.append((nr, nc, steps + 1))
    return float('inf')

def try_cheat(grid: List[str], start: Tuple[int, int], end: Tuple[int, int], 
              cheat_start: Tuple[int, int], cheat_end: Tuple[int, int],
              normal_time: int) -> Optional[int]:
    # Validate cheat positions
    if not (0 <= cheat_start[0] < len(grid) and 0 <= cheat_start[1] < len(grid[0])):
        return None
    if not (0 <= cheat_end[0] < len(grid) and 0 <= cheat_end[1] < len(grid[0])):
        return None
        
    # Check if cheat is valid (max 2 steps)
    manhattan_dist = abs(cheat_end[0] - cheat_start[0]) + abs(cheat_end[1] - cheat_start[1])
    if manhattan_dist > 2:
        return None
        
    # Find path to cheat start
    time_to_cheat = find_shortest_path(grid, start, cheat_start)
    if time_to_cheat == float('inf'):
        return None
        
    # Find path from cheat end to finish
    time_after_cheat = find_shortest_path(grid, cheat_end, end)
    if time_after_cheat == float('inf'):
        return None
        
    total_time = time_to_cheat + manhattan_dist + time_after_cheat
    time_saved = normal_time - total_time
    return time_saved if time_saved > 0 else None

def count_effective_cheats(racetrack: str) -> int:
    # Convert string to grid
    grid = racetrack.strip().split('\n')
    
    # Find start and end positions
    start, end = get_start_end_positions(grid)
    
    # Find normal shortest path time
    normal_time = find_shortest_path(grid, start, end)
    
    # Try all possible cheat combinations
    rows, cols = len(grid), len(grid[0])
    cheats_saving: Set[int] = set()
    
    for r1 in range(rows):
        for c1 in range(cols):
            if grid[r1][c1] == '#':
                continue
            for r2 in range(rows):
                for c2 in range(cols):
                    if grid[r2][c2] == '#':
                        continue
                    time_saved = try_cheat(grid, start, end, (r1, c1), (r2, c2), normal_time)
                    if time_saved is not None and time_saved >= 100:
                        cheats_saving.add(time_saved)
    
    return len(cheats_saving)

def solution() -> int:
    racetrack = input().strip()
    while True:
        try:
            line = input().strip()
            racetrack += '\n' + line
        except EOFError:
            break
    return count_effective_cheats(racetrack)