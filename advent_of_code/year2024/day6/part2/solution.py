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

    def is_valid(pos: Tuple[int, int]) -> bool:
        return 0 <= pos[0] < rows and 0 <= pos[1] < cols

    def get_path(grid: List[str], start: Tuple[int, int], start_dir: int) -> Tuple[Set[Tuple[int, int]], Set[Tuple[Tuple[int, int], int]]]:
        pos = start
        direction = start_dir
        path = set()
        visited_states = set()

        # Continue until we leave the map or enter a loop
        while True:
            path.add(pos)
            state = (pos, direction)
            if state in visited_states:
                return path, visited_states

            visited_states.add(state)
            next_pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])

            # Check if next position is blocked or out of bounds
            if not is_valid(next_pos) or grid[next_pos[0]][next_pos[1]] == '#':
                direction = (direction + 1) % 4  # Turn right
            else:
                pos = next_pos

            # If we've left the map
            if not is_valid(pos):
                return path, visited_states

    def try_obstruction(pos: Tuple[int, int], grid: List[str]) -> bool:
        if pos == start_pos or grid[pos[0]][pos[1]] == '#' or grid[pos[0]][pos[1]] == '^':
            return False

        # Create a new grid with the obstruction
        new_grid = copy.deepcopy(grid)
        new_grid[pos[0]] = new_grid[pos[0]][:pos[1]] + '#' + new_grid[pos[0]][pos[1] + 1:]

        # Get the path with the new obstruction
        path, visited_states = get_path(new_grid, start_pos, initial_dir)

        # Check if the path creates a loop (path is finite and doesn't leave the map)
        return len(visited_states) != len(path) 


    # Try placing an obstruction at each empty position
    count = 0
    for i in range(rows):
        for j in range(cols):
            if try_obstruction((i, j), grid):
                count += 1

    return count


def solution() -> int:
    # Read input from stdin
    input_data = sys.stdin.read()
    return count_obstruction_locations(input_data)


if __name__ == "__main__":
    print(solution())