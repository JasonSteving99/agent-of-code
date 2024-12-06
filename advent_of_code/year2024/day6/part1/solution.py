from typing import List, Set, Tuple
import sys

def count_guard_visited_positions(input_str: str) -> int:
    # Parse the input grid
    grid = [list(line.strip()) for line in input_str.splitlines()]
    rows, cols = len(grid), len(grid[0])
    
    # Find guard's starting position and facing direction
    guard_pos = None
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '^':
                guard_pos = (i, j)
                facing = 0  # 0: up, 1: right, 2: down, 3: left
                break
        if guard_pos:
            break

    if not guard_pos:
        return 0

    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited: Set[Tuple[int, int]] = {guard_pos}
    
    curr_pos = guard_pos
    curr_facing = facing
    
    while True:
        # Check if we're still in bounds
        row, col = curr_pos
        if not (0 <= row < rows and 0 <= col < cols):
            break
            
        # Check position in front
        next_row = row + directions[curr_facing][0]
        next_col = col + directions[curr_facing][1]
        
        # If next position is out of bounds or has an obstacle, turn right
        if (not (0 <= next_row < rows and 0 <= next_col < cols) or 
            grid[next_row][next_col] == '#'):
            # Turn right (increment facing by 1 modulo 4)
            curr_facing = (curr_facing + 1) % 4
        else:
            # Move forward
            curr_pos = (next_row, next_col)
            visited.add(curr_pos)
    
    return len(visited)

def solution() -> int:
    # Read from stdin
    input_str = sys.stdin.read()
    return count_guard_visited_positions(input_str)