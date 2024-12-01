"""Solution for finding the maximum steps in a pipe maze."""
from typing import Tuple, Set, List, Optional
import sys

def max_steps_in_pipe_maze(grid_str: str) -> int:
    # Convert input string to grid
    grid = grid_str.strip().split('\n')
    rows, cols = len(grid), len(grid[0])

    # Find starting position 'S'
    start_pos = None
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                start_pos = (i, j)
                break
        if start_pos:
            break

    # Handle case where 'S' is not found
    if start_pos is None:
        return 0
    
    # Define possible pipe connections
    pipe_connections = {
        '|': [(1, 0), (-1, 0)],  # vertical
        '-': [(0, 1), (0, -1)],  # horizontal
        'L': [(-1, 0), (0, 1)],  # up and right
        'J': [(-1, 0), (0, -1)], # up and left
        '7': [(1, 0), (0, -1)],  # down and left
        'F': [(1, 0), (0, 1)],   # down and right
        '.': [],                  # ground
        'S': [(1, 0), (-1, 0), (0, 1), (0, -1)]  # start (try all directions)
    }

    def is_valid_pos(pos: Tuple[int, int]) -> bool:
        return 0 <= pos[0] < rows and 0 <= pos[1] < cols

    def get_connected_neighbors(pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        r, c = pos
        char = grid[r][c]
        connections = []
        
        for dr, dc in pipe_connections[char]:
            new_pos = (r + dr, c + dc)
            if not is_valid_pos(new_pos):
                continue
                
            # Check if the neighbor pipe connects back
            back_r, back_c = new_pos
            neighbor_char = grid[back_r][back_c]
            if neighbor_char == 'S':
                # For start position, always consider it as a potential connection
                connections.append(new_pos)
                continue
                
            # Check if the neighbor's pipe connects back to current position
            neighbor_connections = pipe_connections[neighbor_char]
            if (-dr, -dc) in neighbor_connections:
                connections.append(new_pos)
                
        return connections

    def find_loop(start: Tuple[int, int]) -> Set[Tuple[int, int]]:
        visited = {start}
        queue = [(start, [start])]
        
        while queue:
            pos, path = queue.pop(0)
            for next_pos in get_connected_neighbors(pos):
                if next_pos == start and len(path) > 2:
                    # Found a loop back to start
                    return set(path)
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, path + [next_pos]))
        return set()

    # Find the main loop
    loop_tiles = find_loop(start_pos)
    if not loop_tiles:
        return 0

    # Calculate distances from start
    distances = {start_pos: 0}
    queue = [(start_pos, 0)]
    max_distance = 0

    while queue:
        pos, dist = queue.pop(0)
        for next_pos in get_connected_neighbors(pos):
            if next_pos in loop_tiles and next_pos not in distances:
                distances[next_pos] = dist + 1
                max_distance = max(max_distance, dist + 1)
                queue.append((next_pos, dist + 1))

    return max_distance

def solution() -> int:
    """Read from stdin and return the solution."""
    input_data = sys.stdin.read()
    return max_steps_in_pipe_maze(input_data)

if __name__ == "__main__":
    print(solution())