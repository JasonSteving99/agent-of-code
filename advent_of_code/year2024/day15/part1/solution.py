from typing import List, Set, Tuple
import sys

def parse_input(input_str: str) -> Tuple[List[List[str]], str]:
    parts = input_str.strip().split('\n\n')
    warehouse_map = [list(line) for line in parts[0].splitlines()]
    moves = ''.join(parts[1].strip().split('\n'))
    return warehouse_map, moves

def get_robot_position(warehouse: List[List[str]]) -> Tuple[int, int]:
    for i, row in enumerate(warehouse):
        for j, cell in enumerate(row):
            if cell == '@':
                return i, j
    return -1, -1  # Should never happen given valid input

def try_move(warehouse: List[List[str]], robot_pos: Tuple[int, int], 
             direction: str) -> Tuple[bool, Tuple[int, int]]:
    ri, rj = robot_pos
    di = -1 if direction == '^' else 1 if direction == 'v' else 0
    dj = -1 if direction == '<' else 1 if direction == '>' else 0
    new_ri, new_rj = ri + di, rj + dj
    
    # Check if move would hit wall
    if warehouse[new_ri][new_rj] == '#':
        return False, robot_pos
    
    # If empty space, robot can move
    if warehouse[new_ri][new_rj] == '.':
        warehouse[ri][rj] = '.'
        warehouse[new_ri][new_rj] = '@'
        return True, (new_ri, new_rj)
    
    # If box, check if box can be pushed
    if warehouse[new_ri][new_rj] == 'O':
        box_new_ri, box_new_rj = new_ri + di, new_rj + dj
        if (warehouse[box_new_ri][box_new_rj] == '.'):
            warehouse[ri][rj] = '.'
            warehouse[new_ri][new_rj] = '@'
            warehouse[box_new_ri][box_new_rj] = 'O'
            return True, (new_ri, new_rj)
    
    return False, robot_pos

def calculate_gps_coordinates(warehouse: List[List[str]]) -> int:
    total = 0
    for i, row in enumerate(warehouse):
        for j, cell in enumerate(row):
            if cell == 'O':
                total += (100 * i + j)
    return total

def calculate_final_box_gps_sum(input_data: str) -> int:
    # Parse input
    warehouse, moves = parse_input(input_data)
    
    # Get initial robot position
    robot_pos = get_robot_position(warehouse)
    
    # Execute all moves
    for move in moves:
        robot_pos = try_move(warehouse, robot_pos, move)[1]
    
    # Calculate final GPS sum
    return calculate_gps_coordinates(warehouse)

def solution() -> int:
    return calculate_final_box_gps_sum(sys.stdin.read())