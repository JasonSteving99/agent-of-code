"""Solves the keypad control sequence challenge."""
from dataclasses import dataclass
from collections import deque
from typing import Dict, List, Set, Tuple

@dataclass
class State:
    """Represents a state in the keypad traversal."""
    current_pos: Tuple[int, int]
    sequence: str
    target_code: str
    current_code_idx: int

def solve_keypad(numeric_code: str) -> str:
    """
    Find the shortest sequence of directional button presses to type the given numeric code.
    
    Args:
        numeric_code: The code to be typed on the numeric keypad (e.g., "029A")
    
    Returns:
        The shortest sequence of directional button presses required
    """
    # Define keypad layouts and valid positions
    numeric_keypad: Dict[Tuple[int, int], str] = {
        (0, 0): '7', (0, 1): '8', (0, 2): '9',
        (1, 0): '4', (1, 1): '5', (1, 2): '6',
        (2, 0): '1', (2, 1): '2', (2, 2): '3',
        (3, 0): ' ', (3, 1): '0', (3, 2): 'A'
    }
    
    valid_positions: Set[Tuple[int, int]] = set(numeric_keypad.keys())
    valid_positions.remove((3,0))
    # Directional mappings
    directions = {
        '^': (-1, 0),  # up
        'v': (1, 0),   # down
        '<': (0, -1),  # left
        '>': (0, 1)    # right
    }
    
    def get_valid_moves(pos: Tuple[int, int]) -> List[Tuple[str, Tuple[int, int]]]:
        """Get all valid moves from current position."""
        moves = []
        for dir_symbol, (dy, dx) in directions.items():
            new_pos = (pos[0] + dy, pos[1] + dx)
            if new_pos in valid_positions:
                moves.append((dir_symbol, new_pos))
        return moves
    
    def bfs() -> str:
        """Perform BFS to find shortest path to type the code."""
        start_pos = (3, 2)  # Starting at 'A'
        queue = deque([State(start_pos, "", numeric_code, 0)])
        seen = set()
        
        while queue:
            state = queue.popleft()
            
            # Skip if this state has been seen
            state_key = (state.current_pos, state.current_code_idx)
            if state_key in seen:
                continue
            seen.add(state_key)
            
            # Check if we're at a position where we need to press 'A'
            current_target = state.target_code[state.current_code_idx]
            if numeric_keypad[state.current_pos] == current_target:
                new_sequence = state.sequence + 'A'
                new_code_idx = state.current_code_idx + 1
                
                # If we've completed the code, return the sequence
                if new_code_idx == len(state.target_code):
                    return new_sequence
                
                queue.append(State(
                    state.current_pos,
                    new_sequence,
                    state.target_code,
                    new_code_idx
                ))
            
            # Try all valid moves from current position
            for dir_symbol, new_pos in get_valid_moves(state.current_pos):
                queue.append(State(
                    new_pos,
                    state.sequence + dir_symbol,
                    state.target_code,
                    state.current_code_idx
                ))
        
        return ""  # Should never reach here given valid input
    
    return bfs()

def solution() -> int:
    """
    Read input codes from stdin and return the sum of their complexities.
    """
    codes = [line.strip() for line in input().split('\n') if line.strip()]
    total_complexity = 0
    
    for code in codes:
        # Get shortest sequence for this code
        sequence = solve_keypad(code)
        # Calculate numeric part of code (ignoring leading zeros)
        numeric_part = int(''.join(c for c in code if c.isdigit()))
        # Add complexity (sequence length * numeric part) to total
        total_complexity += len(sequence) * numeric_part
        
    return total_complexity