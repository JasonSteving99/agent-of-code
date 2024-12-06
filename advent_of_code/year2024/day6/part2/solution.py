from typing import List, Set, Tuple
import sys

def get_next_position_direction(
    pos: Tuple[int, int],
    direction: Tuple[int, int],
    grid: List[List[str]]
) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    curr_dir_idx = directions.index(direction)
    curr_row, curr_col = pos

    next_row = curr_row + direction[1]
    next_col = curr_col + direction[0]

    if (
        next_row < 0
        or next_row >= len(grid)
        or next_col < 0
        or next_col >= len(grid[0])
        or grid[next_row][next_col] == '#'
        or grid[next_row][next_col] == 'O'
    ):
        next_dir_idx = (curr_dir_idx + 1) % 4
        return pos, directions[next_dir_idx]
    else:
        return (next_col, next_row), direction


def explore_reachable(grid: List[List[str]], pos: Tuple[int, int], reachable: Set[Tuple[int, int]]):
    if (
        not (0 <= pos[0] < len(grid[0]) and 0 <= pos[1] < len(grid))
        or pos in reachable
        or grid[pos[1]][pos[0]] != '.'
    ):
        return

    reachable.add(pos)
    explore_reachable(grid, (pos[0] + 1, pos[1]), reachable)
    explore_reachable(grid, (pos[0] - 1, pos[1]), reachable)
    explore_reachable(grid, (pos[0], pos[1] + 1), reachable)
    explore_reachable(grid, (pos[0], pos[1] - 1), reachable)


def simulate_guard_path(
    grid: List[List[str]],
    start_pos: Tuple[int, int],
    start_direction: Tuple[int, int],
    max_steps: int = 10000,
) -> Set[Tuple[int, int]]:
    visited = set()
    pos = start_pos
    direction = start_direction
    steps = 0

    while True:
        if not (0 <= pos[1] < len(grid) and 0 <= pos[0] < len(grid[0])):
            return None  # Guard left the grid

        if (pos, direction) in visited:
            reachable = set()
            explore_reachable(grid, start_pos, reachable)            
            visited_reachable = {p for p, d in visited if grid[p[1]][p[0]] == '.'}
            if reachable == visited_reachable:
                return visited
            else:
                return None

        visited.add((pos, direction))
        next_pos, next_direction = get_next_position_direction(pos, direction, grid)

        if steps > max_steps:
            return None  # Prevent infinite loops in unexpected cases

        pos = next_pos
        direction = next_direction
        steps += 1

def count_obstruction_locations(grid_str: str) -> int:
    if not isinstance(grid_str, str):
        raise TypeError("Input must be a string")

    if not grid_str:
        raise ValueError("Map cannot be empty")

    grid = [list(row) for row in grid_str.strip().splitlines()]
    if not grid or not grid[0]:
        raise ValueError("Map cannot be empty")

    height = len(grid)
    width = len(grid[0])

    start_pos = None
    for row in range(height):
        for col in range(width):
            if grid[row][col] == '^':
                start_pos = (col, row)
                start_direction = (0, -1)  # Up
                grid[row][col] = '.'  # Clear start position
                break
        if start_pos:
            break

    valid_positions = 0

    for row in range(height):
        for col in range(width):
            if grid[row][col] == '.' and (col, row) != start_pos:
                grid[row][col] = 'O'

                path = simulate_guard_path(grid, start_pos, start_direction)

                if path is not None:
                    valid_positions += 1

                grid[row][col] = '.'

    return valid_positions

def solution() -> int:
    input_str = sys.stdin.read()
    return count_obstruction_locations(input_str)

if __name__ == "__main__":
    print(solution())
