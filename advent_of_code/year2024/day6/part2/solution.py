"""Day 6, Part 2: Find possible trap positions for a guard following strict patrol protocol."""
from typing import List, Set, Tuple
import copy


def parse_grid(grid_str: str) -> List[List[str]]:
    return [list(line) for line in grid_str.strip().split('\n')]


def find_guard_start(grid: List[List[str]]) -> Tuple[int, int, str]:
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in ('^', '>', 'v', '<'):
                return r, c, cell
    raise ValueError("Guard not found in grid")


def get_next_direction(current: str) -> str:
    return {'^': '>', '>': 'v', 'v': '<', '<': '^'}[current]


def get_next_position(row: int, col: int, direction: str) -> Tuple[int, int]:
    moves = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    dr, dc = moves[direction]
    return row + dr, col + dc


def is_valid_position(row: int, col: int, grid: List[List[str]]) -> bool:
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def has_loop(grid: List[List[str]], start_row: int, start_col: int, start_dir: str) -> bool:
    visited: Set[Tuple[int, int, str]] = set()
    row, col, direction = start_row, start_col, start_dir

    while (row, col, direction) not in visited and is_valid_position(row, col, grid):
        visited.add((row, col, direction))
        next_row, next_col = get_next_position(row, col, direction)

        if not is_valid_position(next_row, next_col, grid) or grid[next_row][next_col] in '#O':
            direction = get_next_direction(direction)
        else:
            row, col = next_row, next_col

    return (row, col, direction) in visited


def count_trap_positions(grid_str: str) -> int:
    grid = parse_grid(grid_str)
    start_row, start_col, start_dir = find_guard_start(grid)
    original_grid = copy.deepcopy(grid)
    count = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '.' and (r, c) != (start_row, start_col):
                grid[r][c] = 'O'
                if has_loop(grid, start_row, start_col, start_dir):
                    count += 1
                grid[r][c] = original_grid[r][c]

    return count


def solution() -> int:
    grid_str = ""
    while True:
        try:
            line = input()
            grid_str += line + "\n"
        except EOFError:
            break
    return count_trap_positions(grid_str.rstrip())


if __name__ == "__main__":
    print(solution())