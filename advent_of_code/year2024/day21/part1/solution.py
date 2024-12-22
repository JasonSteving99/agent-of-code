from typing import List, Dict, Set, Tuple
from queue import Queue

def get_shortest_button_sequence(target_code: str) -> str:
    """
    Find shortest sequence of directional keypad presses to type target code on numeric keypad.
    Args:
        target_code: String containing the target numeric code (e.g. "029A")
    Returns:
        Shortest sequence of directional button presses (<,>,^,v,A)
    """
    # Define keypad layouts
    numeric_keypad = {
        '7': (0,0), '8': (0,1), '9': (0,2),
        '4': (1,0), '5': (1,1), '6': (1,2), 
        '1': (2,0), '2': (2,1), '3': (2,2),
        '0': (3,1), 'A': (3,2)
    }
    
    # Helper function to get valid moves from current position
    def get_valid_moves(pos: Tuple[int, int]) -> List[Tuple[str, Tuple[int, int]]]:
        row, col = pos
        moves = []
        # Check all possible moves (up, down, left, right)
        for direction, (dr, dc) in {'<':(0,-1), '>':(0,1), '^':(-1,0), 'v':(1,0)}.items():
            new_row, new_col = row + dr, col + dc
            # Verify new position exists on numeric keypad
            for digit, coords in numeric_keypad.items():
                if coords == (new_row, new_col):
                    moves.append((direction, (new_row, new_col)))
                    break
        return moves

    def bfs(target_digit: str, start_pos: Tuple[int, int]) -> Tuple[str, Tuple[int, int]]:
        queue = Queue()
        queue.put((start_pos, ""))
        visited = {start_pos}
        target_pos = numeric_keypad[target_digit]
        
        while not queue.empty():
            current_pos, path = queue.get()
            if current_pos == target_pos:
                return path + "A", current_pos
            
            for direction, next_pos in get_valid_moves(current_pos):
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.put((next_pos, path + direction))
                    
        return "", start_pos  # Should never happen with valid input

    # Start at 'A' position
    current_pos = numeric_keypad['A']
    result = ""
    
    # Process each digit in target code
    for digit in target_code:
        sequence, current_pos = bfs(digit, current_pos)
        result += sequence
        
    return result

def solution() -> int:
    """
    Read codes from stdin and return sum of complexities.
    Returns:
        Sum of the complexities of all codes
    """
    total_complexity = 0
    
    # Read the five codes
    for _ in range(5):
        code = input().strip()
        # Get shortest sequence for this code
        sequence = get_shortest_button_sequence(code)
        # Calculate numeric part (ignoring leading zeros)
        numeric_part = int(''.join(c for c in code if c.isdigit()))
        # Add complexity for this code
        total_complexity += len(sequence) * numeric_part
        
    return total_complexity
