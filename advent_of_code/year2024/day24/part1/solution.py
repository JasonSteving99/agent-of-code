"""Solution module for boolean logic gate simulator."""
from typing import Dict, Set, Tuple
import re


def simulate_logic_gates(input_data: str) -> int:
    """
    Simulate a system of logic gates and return the decimal number from z wires.
    
    Args:
        input_data: String containing initial wire values and gate connections
        
    Returns:
        int: Decimal number produced by combining bits on z wires
    """
    # Parse input into initial values and gate connections
    lines = input_data.strip().split('\n')
    
    # Find split between initial values and gate connections
    split_idx = 0
    for i, line in enumerate(lines):
        if not line.strip():
            split_idx = i
            break
    else:
        split_idx = len(lines)
    
    # Parse initial values
    wires: Dict[str, int] = {}
    for line in lines[:split_idx]:
        if not line.strip():
            continue
        wire, value = line.split(': ')
        wires[wire] = int(value)
    
    # Parse gate connections
    gates: list[tuple[str, str, str, str]] = []
    for line in lines[split_idx:]:
        if not line.strip():
            continue
        # Extract gate type and wire names
        match = re.match(r'^(\w+)\s+(AND|OR|XOR)\s+(\w+)\s+->\s+(\w+)$', line)
        if not match:
            continue
        in1, gate_type, in2, out = match.groups()
        gates.append((in1, gate_type, in2, out))

    # Process gates until all z wires have values
    while any(wire.startswith('z') and wire not in wires for wire in [out for _, _, _, out in gates]):
        for in1, gate_type, in2, out in gates:
            if in1 in wires and in2 in wires and out not in wires:
                # Compute gate output
                if gate_type == 'AND':
                    wires[out] = 1 if wires[in1] and wires[in2] else 0
                elif gate_type == 'OR':
                    wires[out] = 1 if wires[in1] or wires[in2] else 0
                else:  # XOR
                    wires[out] = 1 if wires[in1] != wires[in2] else 0

    # Collect z-wire values in order
    z_wires = sorted(wire for wire in wires if wire.startswith('z'))
    
    # Convert binary to decimal
    result = 0
    for z_wire in z_wires:
        result = (result << 1) | wires[z_wire]
        
    return result


def solution() -> int:
    """Read from stdin and return result."""
    import sys
    return simulate_logic_gates(sys.stdin.read())


if __name__ == "__main__":
    print(solution())
