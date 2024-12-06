from typing import List, Set, Tuple
import sys
import copy


def count_obstruction_locations(input_map: str) -> int:
    # Convert input map to 2D grid
    grid = input_map.strip().split('\n')
    rows = len(grid)
    cols = len(grid[0])

    # Find starting position and direction of guard
    start_pos = None
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '^':
                start_pos = (i, j)
                break
        if start_pos:
            break

    # Directions: UP, RIGHT, DOWN, LEFT
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    initial_dir = 0  # UP

    def is_valid(pos: Tuple[int, int], grid: List[str]) -> bool:
        return 0 <= pos[0] < rows and 0 <= pos[1] < cols and grid[pos[0]][pos[1]] != '#'

    def get_path(grid: List[str], start: Tuple[int, int], start_dir: int) -> Tuple[Set[Tuple[int, int]], int]:
        pos = start
        direction = start_dir
        path = set()
        path.add(pos)

        while True:
            next_pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])

            if not is_valid(next_pos, grid):
                direction = (direction + 1) % 4  # Turn right
                next_pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
            
            if not is_valid(next_pos, grid):
                return path, direction


            if next_pos in path:
                return path, direction

            pos = next_pos
            path.add(pos)

    def try_obstruction(pos: Tuple[int, int], grid: List[str], start_pos: Tuple[int, int], initial_dir: int) -> bool:
        if pos == start_pos or grid[pos[0]][pos[1]] == '#' or grid[pos[0]][pos[1]] == '^':
            return False

        new_grid = copy.deepcopy(grid)
        new_grid[pos[0]] = new_grid[pos[0]][:pos[1]] + '#' + new_grid[pos[0]][pos[1] + 1:]
        path, direction = get_path(new_grid, start_pos, initial_dir)
        return start_pos in path and initial_dir == direction

    count = 0
    for i in range(rows):
        for j in range(cols):
            if try_obstruction((i, j), grid, start_pos, initial_dir):
                count += 1
    return count

def solution() -> int:
    input_data = sys.stdin.read()
    return count_obstruction_locations(input_data)

if __name__ == "__main__":
    print(solution())
