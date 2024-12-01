"""Solution for the pipe maze problem."""
from collections import deque
from typing import List, Set, Tuple, Dict


def get_possible_directions(pipe: str) -> List[Tuple[int, int]]:
    """Return possible movement directions for a given pipe type."""
    directions = {
        '|': [(-1, 0), (1, 0)],  # North and South
        '-': [(0, -1), (0, 1)],  # West and East
        'L': [(-1, 0), (0, 1)],  # North and East
        'J': [(-1, 0), (0, -1)],  # North and West
        '7': [(1, 0), (0, -1)],  # South and West
        'F': [(1, 0), (0, 1)],   # South and East
    }
    return directions.get(pipe, [])


def get_connected_neighbors(maze: List[str], row: int, col: int) -> List[Tuple[int, int]]:
    """Return valid connected neighbors for a given position."""
    rows, cols = len(maze), len(maze[0])
    neighbors = []

    # If current position is 'S', check all adjacent pipes that connect back to S
    if maze[row][col] == 'S':
        # Check all adjacent positions
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < rows and 0 <= new_col < cols:
                pipe = maze[new_row][new_col]
                if pipe != '.':
                    # For each adjacent pipe, check if it connects back to S
                    directions = get_possible_directions(pipe)
                    for dir_x, dir_y in directions:
                        if new_row + dir_x == row and new_col + dir_y == col:
                            neighbors.append((new_row, new_col))
        return neighbors

    # For regular pipes, use their defined directions
    current_pipe = maze[row][col]
    for dx, dy in get_possible_directions(current_pipe):
        new_row, new_col = row + dx, col + dy
        if 0 <= new_row < rows and 0 <= new_col < cols:
            neighbors.append((new_row, new_col))
    return neighbors


def find_start(maze: List[str]) -> Tuple[int, int]:
    """Find the starting position 'S' in the maze."""
    for i, row in enumerate(maze):
        if 'S' in row:
            return i, row.index('S')
    return -1, -1


def calculate_max_loop_distance(maze_str: str) -> int:
    """Calculate the maximum distance in the loop from the starting position.

    Args:
        maze_str: The maze representation as a string with newlines.

    Returns:
        The maximum distance from the starting position in the loop.
    """
    # Convert input string to list of strings
    maze = maze_str.strip().split('\n')

    # Find starting position
    start_row, start_col = find_start(maze)

    # BFS to find distances
    distances: Dict[Tuple[int, int], int] = {(start_row, start_col): 0}
    queue = deque([(start_row, start_col)])
    visited: Set[Tuple[int, int]] = {(start_row, start_col)}

    while queue:
        current_row, current_col = queue.popleft()
        current_dist = distances[(current_row, current_col)]

        for next_row, next_col in get_connected_neighbors(maze, current_row, current_col):
            if (next_row, next_col) not in visited:
                visited.add((next_row, next_col))
                distances[(next_row, next_col)] = current_dist + 1
                queue.append((next_row, next_col))

    # Return maximum distance if any points were found
    return max(distances.values()) if distances else 0


def solution() -> int:
    """Read from stdin and solve the problem."""
    import sys
    input_data = sys.stdin.read()
    return calculate_max_loop_distance(input_data)