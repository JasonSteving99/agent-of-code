```python
from collections import deque
from dataclasses import dataclass
from typing import List, Set, Tuple, Dict, Optional

@dataclass(frozen=True)
class Point:
    row: int
    col: int

def parse_maze(maze_str: str) -> Tuple[List[List[str]], Point, Point]:
    """Parse the maze string into a 2D list and find start/end positions."""
    maze = [list(line) for line in maze_str.strip().splitlines()]
    start = end = None
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = Point(i, j)
                maze[i][j] = '.'  # Replace S with . for easier processing
            elif cell == 'E':
                end = Point(i, j)
                maze[i][j] = '.'  # Replace E with . for easier processing
    return maze, start, end

def get_normal_distance(maze: List[List[str]], start: Point, end: Point) -> Dict[Point, int]:
    """Calculate distances to all reachable points using normal movement."""
    distances: Dict[Point, int] = {start: 0}
    queue = deque([start])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        current = queue.popleft()
        for dr, dc in directions:
            new_row, new_col = current.row + dr, current.col + dc
            new_point = Point(new_row, new_col)
            
            if (0 <= new_row < len(maze) and 
                0 <= new_col < len(maze[0]) and 
                maze[new_row][new_col] == '.' and 
                new_point not in distances):
                distances[new_point] = distances[current] + 1
                queue.append(new_point)
    
    return distances

def try_cheat(maze: List[List[str]], start: Point, end: Point, base_distance: int) -> int:
    """Calculate number of cheats that save at least 100 picoseconds."""
    height, width = len(maze), len(maze[0])
    valid_cheats = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Calculate distances from both start and end for normal movement
    start_distances = get_normal_distance(maze, start, end)
    end_distances = get_normal_distance(maze, end, start)
    
    # Try all possible cheat start positions
    for row in range(height):
        for col in range(width):
            if maze[row][col] != '.':
                continue
            start_pos = Point(row, col)
            if start_pos not in start_distances:
                continue
            
            # Try all possible cheat end positions within 2 steps
            seen = set()
            to_check = deque([(start_pos, 0)])
            
            while to_check:
                pos, steps = to_check.popleft()
                if steps > 2:
                    continue
                
                if pos in seen:
                    continue
                seen.add(pos)
                
                # If we can reach the end from here normally
                if pos in end_distances:
                    # Calculate total path length with cheat
                    total_distance = (start_distances[start_pos] +  # Distance to cheat start
                                   steps +                         # Cheat length
                                   end_distances[pos])            # Distance from cheat end to finish
                    
                    # If this cheat saves at least 100 picoseconds
                    if base_distance - total_distance >= 100:
                        valid_cheats += 1
                
                # Try moving in all directions (through walls)
                for dr, dc in directions:
                    new_row, new_col = pos.row + dr, pos.col + dc
                    if 0 <= new_row < height and 0 <= new_col < width:
                        to_check.append((Point(new_row, new_col), steps + 1))
    
    return valid_cheats

def solve_maze(maze_str: str) -> int:
    """
    Solve the maze and return the number of cheats that would save at least 100 picoseconds.
    """
    # Parse the maze
    maze, start, end = parse_maze(maze_str)
    
    # Get the base distance (without cheating)
    base_distances = get_normal_distance(maze, start, end)
    if end not in base_distances:
        return 0  # No solution possible
    
    base_distance = base_distances[end]
    
    # Find all possible cheats that save at least 100 picoseconds
    return try_cheat(maze, start, end, base_distance)
```