"""Solves puzzle of finding steps to reach ZZZ from AAA following left/right instructions."""
import sys
from typing import Dict, Tuple

def parse_input(raw_input: str) -> Tuple[str, Dict[str, Tuple[str, str]]]:
    """Parse the input into instructions and node mapping."""
    lines = raw_input.strip().split('\n')
    
    # First line contains the instructions
    instructions = lines[0].strip()
    
    # Skip empty line and process node mappings
    node_map = {}
    for line in lines[2:]:
        node, paths = line.split(' = ')
        left, right = paths.strip('()').split(', ')
        node_map[node] = (left, right)
        
    return instructions, node_map

def steps_to_reach_zzz(input_str: str) -> int:
    """
    Calculate steps required to reach ZZZ from AAA following the given instructions.
    
    Args:
        input_str: Input string containing instructions and node mappings
        
    Returns:
        Number of steps required to reach ZZZ
    """
    instructions, node_map = parse_input(input_str)
    
    current_node = 'AAA'
    steps = 0
    instr_len = len(instructions)
    
    while current_node != 'ZZZ':
        # Get current instruction (L or R) by using modulo for cycling
        direction = instructions[steps % instr_len]
        
        # Get next node based on direction
        if direction == 'L':
            current_node = node_map[current_node][0]
        else:  # direction == 'R'
            current_node = node_map[current_node][1]
            
        steps += 1
        
    return steps

def solution() -> int:
    """Read input from stdin and return the solution."""
    return steps_to_reach_zzz(sys.stdin.read())

if __name__ == '__main__':
    print(solution())