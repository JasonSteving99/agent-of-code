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

class Keypad:
    """Represents a directional keypad.
    The numeric keypad has coordinates, but a mapping to characters.
    The directional keypads use coordinates that map to direction symbols.
    """

    def __init__(self, keypad_type: str):
        self.keypad_type = keypad_type
        if keypad_type == "numeric":
            self.layout: Dict[Tuple[int, int], str] = {
                (0, 0): '7', (0, 1): '8', (0, 2): '9',
                (1, 0): '4', (1, 1): '5', (1, 2): '6',
                (2, 0): '1', (2, 1): '2', (2, 2): '3',
                (3, 0): ' ', (3, 1): '0', (3, 2): 'A'
            }
            self.valid_positions = set(self.layout.keys())
            self.valid_positions.remove((3,0))

        elif keypad_type == "directional":
            self.layout: Dict[Tuple[int, int], str] = {
                 (0, 1): '^', (0, 2): 'A',
                 (1, 0): '<', (1, 1): 'v', (1, 2): '>'
             }
            self.valid_positions = set(self.layout.keys())
        else:
            raise ValueError(f"Invalid keypad type: {keypad_type}")

        self.directions = {
            '^': (-1, 0),  # up
            'v': (1, 0),   # down
            '<': (0, -1),  # left
            '>': (0, 1)    # right
        }
    def get_valid_moves(self, pos: Tuple[int, int]) -> List[Tuple[str, Tuple[int, int]]]:
        """Get all valid moves from current position."""
        moves = []
        for dir_symbol, (dy, dx) in self.directions.items():
            new_pos = (pos[0] + dy, pos[1] + dx)
            if new_pos in self.valid_positions:
                moves.append((dir_symbol, new_pos))
        return moves

    def solve_code(self, target_code: str) -> str:
        """Perform BFS to find shortest path to type the code."""
        if self.keypad_type == "numeric":
            start_pos = (3, 2)  # Starting at 'A'
        else:
            start_pos = (0,2)

        queue = deque([State(start_pos, "", target_code, 0)])
        seen = set()

        while queue:
            state = queue.popleft()
            # Skip if this state has been seen
            state_key = (state.current_pos, state.current_code_idx)
            if state_key in seen:
                continue
            seen.add(state_key)

            current_target = state.target_code[state.current_code_idx]
            if self.layout.get(state.current_pos) == current_target:
                new_sequence = state.sequence + 'A'
                new_code_idx = state.current_code_idx + 1
                if new_code_idx == len(state.target_code):
                    return new_sequence

                queue.append(State(
                    state.current_pos,
                    new_sequence,
                    state.target_code,
                    new_code_idx
                ))

            for dir_symbol, new_pos in self.get_valid_moves(state.current_pos):
                queue.append(State(
                    new_pos,
                    state.sequence + dir_symbol,
                    state.target_code,
                    state.current_code_idx
                ))
        return ""

def solution() -> int:
    """
    Read input codes from stdin and return the sum of their complexities.
    """
    codes = [line.strip() for line in input().split('\n') if line.strip()]
    total_complexity = 0
    
    numeric_keypad = Keypad("numeric")
    second_directional_keypad = Keypad("directional")
    first_directional_keypad = Keypad("directional")
    
    for code in codes:
       
        second_level_code = second_directional_keypad.solve_code(code)
        first_level_code = first_directional_keypad.solve_code(second_level_code)
        sequence = first_level_code

        numeric_part = int(''.join(c for c in code if c.isdigit()))
        total_complexity += len(sequence) * numeric_part
        
    return total_complexity