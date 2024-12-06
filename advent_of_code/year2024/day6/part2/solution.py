from typing import List, Set, Tuple
import sys

def simulate_path(grid: List[str], start_pos: Tuple[int, int], marked_cells: Set[Tuple[int, int]]) -> bool:
    """Simulate guard path and return True if loops, False if exits grid"""
    R, C = len(grid), len(grid[0])
    # Directions: up, right, down, left
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    curr_dir = 0  # Start facing up

    row, col = start_pos
    visited_states = set()  # (row, col, direction)
    
    while True:
        if (row, col, curr_dir) in visited_states:
            return True  # Found a loop
        
        visited_states.add((row, col, curr_dir))
        marked_cells.add((row, col))
        
        # Check forward position
        next_row = row + dirs[curr_dir][0]
        next_col = col + dirs[curr_dir][1]
        
        # Check if out of bounds or hits obstacle
        if (next_row < 0 or next_row >= R or next_col < 0 or next_col >= C):
            return False  # Guard exits grid
        
        if grid[next_row][next_col] == '#':
            curr_dir = (curr_dir + 1) % 4  # Turn right
        else:
            row, col = next_row, next_col  # Move forward

def count_obstruction_locations(map_str: str) -> int:
    # Parse map into grid
    grid = [list(line) for line in map_str.strip().split('\n')]
    R, C = len(grid), len(grid[0])
    
    # Find guard's starting position
    start_pos = None
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '^':
                start_pos = (i, j)
                grid[i][j] = '.'
                break
        if start_pos:
            break
            
    assert start_pos is not None
    
    # Try each possible location for the new obstruction
    loop_positions = 0
    
    for i in range(R):
        for j in range(C):
            # Skip if position already has obstacle or is guard start
            if grid[i][j] != '.' or (i, j) == start_pos:
                continue
                
            # Place temporary obstruction
            grid[i][j] = '#'
            marked_cells = set()
            
            # Check if this creates a loop
            if simulate_path(grid, start_pos, marked_cells):
                loop_positions += 1
                
            # Remove temporary obstruction
            grid[i][j] = '.'
            
    return loop_positions

def solution() -> int:
    # Read input from stdin
    map_str = sys.stdin.read()
    return count_obstruction_locations(map_str)

if __name__ == '__main__':
    print(solution())