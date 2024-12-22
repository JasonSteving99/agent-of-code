from typing import List, Dict, Set, Tuple
from collections import deque

def get_shortest_button_sequence(target_code: str) -> str:
    """
    Find shortest sequence of directional keypad presses to type target code on numeric keypad.
    Args:
        target_code: String containing the target numeric code (e.g. "029A")
    Returns:
        Shortest sequence of directional button presses (<,>,^,v,A)
    """
    numeric_keypad = {
        '7': (0, 0), '8': (0, 1), '9': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '1': (2, 0), '2': (2, 1), '3': (2, 2),
        '0': (3, 1), 'A': (3, 2)
    }

    def get_neighbors(pos: Tuple[int, int]) -> List[Tuple[Tuple[int,int], str]]:
        neighbors:List[Tuple[Tuple[int, int], str]] = []
        row, col = pos
        moves = [("<", (0,-1)), (">", (0,1)), ("^", (-1,0)), ("v", (1,0))]
        for direction, (dr, dc) in moves:
             new_row, new_col = row + dr, col + dc
             if (new_row, new_col) in numeric_keypad.values():
                 neighbors.append(((new_row, new_col), direction))
        return neighbors
    
    def bfs(start:Tuple[int,int], end: Tuple[int, int]) -> str:
        queue = deque([(start, "")]
        visited = {start}
        while queue:
            current_pos, path = queue.popleft()
            if current_pos == end:
                return path
            for neighbor, direction in get_neighbors(current_pos):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path+direction))
        return "" # Should never happen with valid inputs.
    
    current_pos = numeric_keypad['A']
    result = ""
    for digit in target_code:
        target_pos = numeric_keypad[digit]
        path = bfs(current_pos, target_pos)
        result += path + "A"
        current_pos = target_pos
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
