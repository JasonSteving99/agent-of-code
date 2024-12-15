"""Calculates the sum of the GPS coordinates of all boxes after robot movements."""
from typing import List, Set, Tuple


def calculate_final_box_gps_sum(input_str: str) -> int:
    # Parse input
    lines = input_str.strip().split('\n')

    # Find where grid ends and movements begin
    grid: List[str] = []
    moves = ""
    parsing_grid = True
    for line in lines:
        if parsing_grid:
            if line and all(c in "#.O@" for c in line):
                grid.append(line)
            elif not line:
                parsing_grid = False
        else:
            moves += line.strip()

    # Convert grid to list for easier manipulation
    grid = [list(row) for row in grid]
    rows, cols = len(grid), len(grid[0])

    # Find robot position
    robot_pos = None
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@':
                robot_pos = (i, j)
                break
        if robot_pos:
            break

    # Helper function to check if movement is valid
    def can_move(pos: Tuple[int, int], delta: Tuple[int, int], curr_grid: List[List[str]]) -> bool:
        next_pos = (pos[0] + delta[0], pos[1] + delta[1])
        
        if 0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols:
            if curr_grid[next_pos[0]][next_pos[1]] == 'O':
                box_next = (next_pos[0] + delta[0], next_pos[1] + delta[1])
                if not (0 <= box_next[0] < rows and 0 <= box_next[1] < cols):
                    return False
                if curr_grid[box_next[0]][box_next[1]] in ['#', 'O']:
                    return False
            elif curr_grid[next_pos[0]][next_pos[1]] == '#':
                return False
        else:
            return False
        return True

    # Process movements
    curr_pos = robot_pos
    direction_map = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    for move in moves:
        delta = direction_map[move]
        if can_move(curr_pos, delta, grid):
            next_pos = (curr_pos[0] + delta[0], curr_pos[1] + delta[1])
            
            # If moving into a box, push it
            if grid[next_pos[0]][next_pos[1]] == 'O':
                box_next = (next_pos[0] + delta[0], next_pos[1] + delta[1])
                grid[box_next[0]][box_next[1]] = 'O'
                grid[next_pos[0]][next_pos[1]] = '@'
                curr_pos = next_pos
            else:
                grid[next_pos[0]][next_pos[1]] = '@'
                curr_pos = next_pos

            grid[curr_pos[0]][curr_pos[1]] = '.'

    # Calculate GPS coordinates sum
    gps_sum = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'O':
                gps_sum += (100 * i + j)

    return gps_sum

def solution() -> int:
    input_lines = []
    while True:
        try:
            line = input()
            input_lines.append(line)
        except EOFError:
            break
    input_str = "\n".join(input_lines)
    result = calculate_final_box_gps_sum(input_str)
    return result