from enum import Enum
from typing import List, Set, Tuple

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

def count_guard_visited_positions(input_str: str) -> int:
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string.")
    if not input_str:
        raise ValueError("Input string cannot be empty.")

    # Parse input grid
    grid = [list(line) for line in input_str.strip().split('\n')]
    rows, cols = len(grid), len(grid[0])
    
    # Find guard start position and direction
    start_pos = None
    start_dir = None
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '^':
                start_pos = (i, j)
                start_dir = Direction.UP
            elif grid[i][j] == '>':
                start_pos = (i, j)
                start_dir = Direction.RIGHT
            elif grid[i][j] == 'v':
                start_pos = (i, j)
                start_dir = Direction.DOWN
            elif grid[i][j] == '<':
                start_pos = (i, j)
                start_dir = Direction.LEFT
    
    if not start_pos:
        raise ValueError("Invalid grid: No guard found.")

    # Movement vectors for each direction (row, col)
    moves = {
        Direction.UP: (-1, 0),
        Direction.RIGHT: (0, 1),
        Direction.DOWN: (1, 0),
        Direction.LEFT: (0, -1)
    }

    # Turn right mapping
    turn_right = {
        Direction.UP: Direction.RIGHT,
        Direction.RIGHT: Direction.DOWN,
        Direction.DOWN: Direction.LEFT,
        Direction.LEFT: Direction.UP
    }

    def is_valid_pos(pos: Tuple[int, int]) -> bool:
        return 0 <= pos[0] < rows and 0 <= pos[1] < cols

    def has_obstacle(pos: Tuple[int, int], direction: Direction) -> bool:
        next_row = pos[0] + moves[direction][0]
        next_col = pos[1] + moves[direction][1]
        if not is_valid_pos((next_row, next_col)):
            return True
        return grid[next_row][next_col] == '#'

    visited: Set[Tuple[int, int]] = set()
    curr_pos = start_pos
    curr_dir = start_dir

    while is_valid_pos(curr_pos):
        if has_obstacle(curr_pos, curr_dir):
            curr_dir = turn_right[curr_dir]
            if has_obstacle(curr_pos, curr_dir):
                break  # No valid move after turning
        
        # Move forward
        curr_pos = (
            curr_pos[0] + moves[curr_dir][0],
            curr_pos[1] + moves[curr_dir][1]
        )
        if is_valid_pos(curr_pos):
            visited.add(curr_pos)
        else:
            break

    return len(visited)

def solution() -> int:
    # Read input from stdin
    import sys
    input_str = sys.stdin.read()
    return count_guard_visited_positions(input_str)