from typing import List, Set, Tuple
import sys


def calculate_final_box_gps_sum(input_str: str) -> int:
    """Calculate the sum of GPS coordinates of all boxes after robot movement."""
    # Parse the input
    lines = input_str.strip().split('\n')
    
    # Find the empty line separating map from moves
    separator_idx = lines.index('')
    map_lines = lines[:separator_idx]
    moves = ''.join(lines[separator_idx + 1:]).strip()
    
    # Initialize game state
    height = len(map_lines)
    width = len(map_lines[0])
    boxes: Set[Tuple[int, int]] = set()
    robot_pos = None

    # Parse initial state
    for i, line in enumerate(map_lines):
        for j, char in enumerate(line):
            if char == 'O':
                boxes.add((i, j))
            elif char == '@':
                robot_pos = [i, j]

    # Movement directions
    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    # Process each move
    for move in moves:
        if move not in directions:
            continue
            
        dy, dx = directions[move]
        new_pos = [robot_pos[0] + dy, robot_pos[1] + dx]
        
        # Check if new position is within bounds and not a wall
        if (0 <= new_pos[0] < height and 
            0 <= new_pos[1] < width and 
            map_lines[new_pos[0]][new_pos[1]] != '#'):
            
            # Check if there's a box in the way
            if (new_pos[0], new_pos[1]) in boxes:
                box_new_pos = (new_pos[0] + dy, new_pos[1] + dx)
                
                # Check if box can be pushed
                if (0 <= box_new_pos[0] < height and 
                    0 <= box_new_pos[1] < width and 
                    map_lines[box_new_pos[0]][box_new_pos[1]] != '#' and
                     box_new_pos not in boxes):
                    
                    # Move the box
                    boxes.remove((new_pos[0], new_pos[1]))
                    boxes.add(box_new_pos)
                    
                    # Move the robot
                    robot_pos = new_pos

            else:
                # Move the robot
                robot_pos = new_pos

    # Calculate GPS sum
    total = 0
    for box in boxes:
        gps = box[0] * 100 + box[1]
        total += gps

    return total


def solution() -> int:
    """Read from stdin and return solution."""
    input_data = sys.stdin.read()
    return calculate_final_box_gps_sum(input_data)


if __name__ == "__main__":
    print(solution())
