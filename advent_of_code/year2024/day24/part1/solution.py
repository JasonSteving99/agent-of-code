from typing import Dict, List, Tuple
import sys

def extract_wire_parts(gate_line: str) -> Tuple[str, str, str, str]:
    """Extract wire input and output parts from a gate line."""
    inputs, output = gate_line.split(" -> ")
    parts = inputs.split()
    if len(parts) == 3:  # Binary operation
        wire1, op, wire2 = parts
        return wire1, op, wire2, output.strip()
    else:
        raise ValueError(f"Invalid gate line format: {gate_line}")

def evaluate_gate(wire1_val: int, op: str, wire2_val: int) -> int:
    """Evaluate a logic gate operation."""
    if op == "AND":
        return wire1_val & wire2_val
    elif op == "OR":
        return wire1_val | wire2_val
    elif op == "XOR":
        return wire1_val ^ wire2_val
    else:
        raise ValueError(f"Unknown operation: {op}")

def simulate_logic_gates(input_data: str) -> int:
    # Parse input into initial values and gates
    lines = input_data.strip().split('\n')
    
    # Initialize dictionaries for wire values and gate definitions
    wire_values: Dict[str, int] = {}
    gates: Dict[str, Tuple[str, str, str]] = {}
    
    # Parse input
    reading_initial_values = True
    for line in lines:
        if not line:
            reading_initial_values = False
            continue
            
        if reading_initial_values:
            if ":" not in line:
                reading_initial_values = False
            else:
                wire, value = line.split(": ")
                wire_values[wire] = int(value)
                continue
                
        if not reading_initial_values:
            try:
                wire1, op, wire2, output = extract_wire_parts(line)
                if output not in gates:
                    gates[output] = (wire1, op, wire2)
            except ValueError:
                continue

    # Evaluate gates until all z-wires have values
    while True:
        changes = False
        for output, (wire1, op, wire2) in gates.items():
            if output not in wire_values:
                if wire1 in wire_values and wire2 in wire_values:
                    wire_values[output] = evaluate_gate(wire_values[wire1], op, wire_values[wire2])
                    changes = True
        
        if not changes:
            break
    
    # Collect z-wire values and convert to decimal
    z_wires = sorted([wire for wire in wire_values if wire.startswith('z')], key=lambda x: int(x[1:]))
    binary = ''.join('1' if wire_values[wire] else '0' for wire in reversed(z_wires))
    return int(binary, 2)

def solution() -> int:
    """Read from stdin and return the result."""
    return simulate_logic_gates(sys.stdin.read())

if __name__ == "__main__":
    print(solution())