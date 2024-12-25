"""Solution module to simulate logic gates."""
from typing import Dict, Set, List
import re
import sys


def apply_gate(op: str, a: int, b: int) -> int:
    """Apply logic gate operation on two inputs."""
    if op == "AND":
        return a & b
    elif op == "OR":
        return a | b
    else:  # XOR
        return a ^ b


def simulate_logic_gates(input_data: str) -> int:
    """
    Simulate a system of logic gates and wires to produce a decimal number.
    
    Args:
        input_data: String containing initial wire values and gate connections
    
    Returns:
        int: Decimal number produced by combining bits on z-wires
    """
    # Parse input
    lines = input_data.strip().split('\n')
    
    # Find where gate definitions start (after initial values)
    gate_start = 0
    for i, line in enumerate(lines):
        if not ':' in line and line.strip():
            gate_start = i
            break
    
    # Parse initial wire values
    wires: Dict[str, int] = {}
    for line in lines[:gate_start]:
        if line.strip():
            wire, value = line.split(':')
            wires[wire.strip()] = int(value.strip())
    
    # Parse and store gate definitions
    gates = []
    for line in lines[gate_start:]:
        if not line.strip():
            continue
        # Parse gate definition line
        match = re.match(r'(\w+)\s+(AND|OR|XOR)\s+(\w+)\s+->\s+(\w+)', line.strip())
        if match:
            in1, op, in2, out = match.groups()
            gates.append((in1, op, in2, out))
    
    # Track which wires have values
    evaluated_wires = set(wires.keys())
    
    # Keep evaluating gates until all z-wires have values
    while True:
        progress = False
        for in1, op, in2, out in gates:
            if out not in evaluated_wires and in1 in evaluated_wires and in2 in evaluated_wires:
                wires[out] = apply_gate(op, wires[in1], wires[in2])
                evaluated_wires.add(out)
                progress = True
        
        if all(wire in evaluated_wires for wire in wires if wire.startswith('z')):
            break
        if not progress:
           break

    
    # Collect all z-wires and their values
    z_wires: List[tuple[str, int]] = []
    for wire in wires.keys():
        if wire.startswith('z'):
            z_wires.append((wire, wires[wire]))
    
    # Convert binary to decimal
    result = 0
    z_wires.sort(key=lambda x: int(x[0][1:]))  # Ensure z-wires are in order
    for wire, value in z_wires:
        result = (result << 1) | value
    
    return result


def solution() -> int:
    """Read from stdin and solve the problem."""
    input_data = sys.stdin.read()
    return simulate_logic_gates(input_data)


if __name__ == "__main__":
    print(solution())
