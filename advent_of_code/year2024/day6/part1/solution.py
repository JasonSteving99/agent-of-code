from typing import List, Set, Tuple
import sys

def parse_guard_map(input_map: str) -> Tuple[List[List[str]], Tuple[int, int, str]]:
    # Convert input map to 2D grid and find guard starting position
    grid = [list(line) for line in input_map.strip().splitlines()]
    if not grid:
        raise ValueError("Input map cannot be empty.")
    if len(grid) != 10 or any(len(row) != 10 for row in grid):
        raise ValueError("Input map must be 10x10.")

    start_pos = None
    start_pos_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                if start_pos_count >= 1:
                    raise ValueError("Input map cannot have multiple guard starting positions.")
                start_pos = (i, j, '^')
                start_pos_count += 1
    if not start_pos:
        raise ValueError("Input map must have one guard starting position.")
    return grid, start_pos

def get_next_direction(current: str, turn_right: bool = True) -> str:
    directions = ['^', '>', 'v', '<']
    current_idx = directions.index(current)
    if turn_right:
        return directions[(current_idx + 1) % 4]
    return directions[(current_idx - 1) % 4]

def get_next_position(pos: Tuple[int, int], direction: str) -> Tuple[int, int]:
    row, col = pos
    if direction == '^':
        return (row - 1, col)
    elif direction == '>':
        return (row, col + 1)
    elif direction == 'v':
        return (row + 1, col)
    else:  # direction == '<'
        return (row, col - 1)

def is_valid_position(grid: List[List[str]], pos: Tuple[int, int]) -> bool:
    rows, cols = len(grid), len(grid[0])
    row, col = pos
    return 0 <= row < rows and 0 <= col < cols

def count_guard_visited_positions(input_map: str) -> int:
    # Parse the input map
    grid, start_pos = parse_guard_map(input_map)

    # Initialize visited positions set
    visited: Set[Tuple[int, int]] = set()
    current_pos = (start_pos[0], start_pos[1])
    current_direction = start_pos[2]
    visited.add(current_pos)

    while True:
        # Get next forward position
        next_pos = get_next_position(current_pos, current_direction)

        # Check if guard would leave the map
        if not is_valid_position(grid, next_pos):
            break

        # Check if there's an obstacle ahead
        next_row, next_col = next_pos
        if grid[next_row][next_col] == '#':
            # Turn right if obstacle ahead
            current_direction = get_next_direction(current_direction)
        else:
            # Move forward if no obstacle
            current_pos = next_pos
            visited.add(current_pos)

    return len(visited)

def solution() -> int:
    # Read input from stdin
    input_data = sys.stdin.read()
    return count_guard_visited_positions(input_data)