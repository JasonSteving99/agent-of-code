"""Day 6, Part 2: Find possible trap positions for a guard following strict patrol protocol."""
from typing import List, Set, Tuple
import copy


def parse_grid(grid_str: str) -> List[List[str]]:
    """Parse the input string into a 2D grid."""
    return [list(line) for line in grid_str.strip().split('\n')]


def find_guard_start(grid: List[List[str]]) -> Tuple[int, int, str]:
    """Find guard's starting position and direction."""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                return i, j, '^'
            elif grid[i][j] == '>':
                return i, j, '>'
            elif grid[i][j] == 'v':
                return i, j, 'v'
            elif grid[i][j] == '<':
                return i, j, '<'
    raise ValueError("Guard not found in grid")


def get_next_direction(current: str) -> str:
    """Get next direction after a right turn."""
    return {'^': '>', '>': 'v', 'v': '<', '<': '^'}[current]


def get_next_position(row: int, col: int, direction: str) -> Tuple[int, int]:
    """Get next position based on direction."""
    moves = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    dr, dc = moves[direction]
    return row + dr, col + dc


def is_valid_position(row: int, col: int, grid: List[List[str]]) -> bool:
    """Check if position is within grid bounds."""
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def simulate_path(grid: List[List[str]], start_row: int, start_col: int, start_dir: str) -> Set[Tuple[int, int, str]]:
    """Simulate guard's path until it loops or leaves the grid, returning visited positions."""
    visited = set()
    current_pos = (start_row, start_col, start_dir)

    while current_pos not in visited and is_valid_position(current_pos[0], current_pos[1], grid):
        visited.add(current_pos)
        row, col, direction = current_pos
        next_row, next_col = get_next_position(row, col, direction)
        if not is_valid_position(next_row, next_col, grid) or grid[next_row][next_col] in '#O':
            direction = get_next_direction(direction)
            current_pos = (row, col, direction)
        else:
            current_pos = (next_row, next_col, direction)
    return visited


def has_loop(grid: List[List[str]], guard_pos: Tuple[int, int, str]) -> bool:
    """Check if guard gets stuck in a loop."""
    visited = simulate_path(grid, guard_pos[0], guard_pos[1], guard_pos[2])
    last_pos = list(visited)[-1]
    return last_pos in visited and is_valid_position(last_pos[0], last_pos[1], grid)


def count_trap_positions(grid_str: str) -> int:
    """Count number of positions where placing an obstacle creates a loop."""
    grid = parse_grid(grid_str)
    guard_start = find_guard_start(grid)
    original_grid = copy.deepcopy(grid)
    trap_positions = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.' and (i, j) != (guard_start[0], guard_start[1]):
                grid[i][j] = 'O'
                if has_loop(grid, guard_start):
                    trap_positions += 1
                grid[i][j] = original_grid[i][j]  # Correctly revert to the initial character

    return trap_positions


def solution() -> int:
    """Read input from stdin and solve the problem."""
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
