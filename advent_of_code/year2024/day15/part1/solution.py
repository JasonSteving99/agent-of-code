from typing import List, Tuple, Set

def calculate_final_gps_sum(warehouse_input: str) -> int:
    """
    Calculate the sum of GPS coordinates for all boxes after robot movement.
    
    Args:
    warehouse_input (str): String containing warehouse layout and movement sequence
    
    Returns:
    int: Sum of GPS coordinates of all boxes after movement
    """
    # Parse input
    lines = warehouse_input.strip().split('\n')
    
    # Find empty line separating map from moves
    separator_idx = 0
    for i, line in enumerate(lines):
        if not line.strip():
            separator_idx = i
            break
    
    # Split input into map and moves
    warehouse_map = [list(line) for line in lines[:separator_idx] if line.strip()]
    moves = ''.join(line.strip() for line in lines[separator_idx+1:] if line.strip())
    
    # Find initial robot position
    robot_pos = None
    for i in range(len(warehouse_map)):
        for j in range(len(warehouse_map[0])):
            if warehouse_map[i][j] == '@':
                robot_pos = (i, j)
                break
        if robot_pos:
            break
    
    # Process each move
    for move in moves:
        new_robot_pos = robot_pos
        
        # Calculate direction
        if move == '^':
            delta = (-1, 0)
        elif move == 'v':
            delta = (1, 0)
        elif move == '<':
            delta = (0, -1)
        elif move == '>':
            delta = (0, 1)
        else:
            continue
            
        new_robot_pos = (robot_pos[0] + delta[0], robot_pos[1] + delta[1])
        
        # Check if movement is valid
        if warehouse_map[new_robot_pos[0]][new_robot_pos[1]] == '#':
            continue
            
        if warehouse_map[new_robot_pos[0]][new_robot_pos[1]] == 'O':
            # Try to push box
            box_new_pos = (new_robot_pos[0] + delta[0], new_robot_pos[1] + delta[1])
            
            # Check if box can be pushed
            if (warehouse_map[box_new_pos[0]][box_new_pos[1]] == '#' or 
                warehouse_map[box_new_pos[0]][box_new_pos[1]] == 'O'):
                continue
            
            # Move box and robot
            warehouse_map[box_new_pos[0]][box_new_pos[1]] = 'O'
            warehouse_map[robot_pos[0]][robot_pos[1]] = '.'
            warehouse_map[new_robot_pos[0]][new_robot_pos[1]] = '@'
            robot_pos = new_robot_pos

        else:
            # Move robot
            warehouse_map[robot_pos[0]][robot_pos[1]] = '.'
            warehouse_map[new_robot_pos[0]][new_robot_pos[1]] = '@'
            robot_pos = new_robot_pos
    
    # Calculate GPS sum
    gps_sum = 0
    for i in range(len(warehouse_map)):
        for j in range(len(warehouse_map[0])):
            if warehouse_map[i][j] == 'O':
                gps_sum += (i * 100 + j)
                
    return gps_sum

def solution() -> int:
    """
    Read input from stdin and return solution.
    
    Returns:
        int: Solution to the problem
    """
    import sys
    return calculate_final_gps_sum(sys.stdin.read())