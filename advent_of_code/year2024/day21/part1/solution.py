"""
Solution for the Keypad Conundrum problem.

This module contains functionality to generate the shortest sequence of directional
keypad presses needed to enter various numeric codes.
"""
from typing import Dict, List, Set, Tuple
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    """Represents a position on a keypad."""
    row: int
    col: int


class Keypad:
    """Represents a keypad with buttons and movement controls."""
    def __init__(self, layout: List[List[str]]):
        self.layout = layout
        self.height = len(layout)
        self.width = len(layout[0]) if layout else 0
        self.button_positions: Dict[str, Position] = {}
        
        for i, row in enumerate(layout):
            for j, button in enumerate(row):
                if button != ' ':
                    self.button_positions[button] = Position(i, j)
    
    def get_button(self, pos: Position) -> str:
        """Get the button at a given position."""
        if (0 <= pos.row < self.height and 
            0 <= pos.col < self.width and 
            self.layout[pos.row][pos.col] != ' '):
            return self.layout[pos.row][pos.col]
        return ' '


def generate_keypad_sequence(target: str) -> str:
    """
    Generate the shortest sequence of directional keypad presses to type the target code.
    
    Args:
        target: The numeric code to be typed.
        
    Returns:
        The shortest sequence of directional keypad button presses.
    """
    # Define the keypads
    numeric_keypad = Keypad([
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        [' ', '0', 'A']
    ])
    
    directional_keypad = Keypad([
        [' ', '^', 'A'],
        ['<', 'v', '>']
    ])
    
    moves = {
        '^': Position(-1, 0),
        'v': Position(1, 0),
        '<': Position(0, -1),
        '>': Position(0, 1)
    }

    def find_path(start: Position, target_button: str, keypad: Keypad) -> List[str]:
        """Find shortest path from start position to target button."""
        visited: Set[Tuple[int, int]] = set()
        queue: List[Tuple[Position, List[str]]] = [(start, [])]
        visited.add((start.row, start.col))
        
        while queue:
            pos, path = queue.pop(0)
            if keypad.get_button(pos) == target_button:
                return path + ['A']  # Add press action
                
            for direction, move in moves.items():
                new_pos = Position(pos.row + move.row, pos.col + move.col)
                pos_tuple = (new_pos.row, new_pos.col)
                
                if (pos_tuple not in visited and 
                    keypad.get_button(new_pos) != ' '):
                    queue.append((new_pos, path + [direction]))
                    visited.add(pos_tuple)
        
        return []  # No path found

    def generate_robot_sequence(code: str) -> str:
        """Generate sequence for robot to type the numeric code."""
        start_pos = numeric_keypad.button_positions['A']
        sequence = []
        
        for digit in code:
            path = find_path(start_pos, digit, numeric_keypad)
            sequence.extend(path)
            start_pos = numeric_keypad.button_positions[digit]
            
        return ''.join(sequence)

    # Start with directional keypad 'A' position
    robot_sequence = generate_robot_sequence(target)
    second_robot_start = directional_keypad.button_positions['A']
    final_sequence = []

    # Generate sequence for second robot
    for action in robot_sequence:
        path = find_path(second_robot_start, action, directional_keypad)
        final_sequence.extend(path)
        if action in directional_keypad.button_positions:
            second_robot_start = directional_keypad.button_positions[action]

    return ''.join(final_sequence)


def solution() -> int:
    """
    Read input codes and return sum of their complexities.
    
    Returns:
        The sum of complexities for all input codes.
    """
    total_complexity = 0
    
    for line in sys.stdin:
        code = line.strip()
        if not code:
            continue
            
        sequence = generate_keypad_sequence(code)
        numeric_part = int(''.join(c for c in code if c.isdigit()))
        complexity = len(sequence) * numeric_part
        total_complexity += complexity
    
    return total_complexity