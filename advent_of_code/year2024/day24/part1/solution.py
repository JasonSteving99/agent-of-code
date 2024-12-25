"""Solution module for boolean logic gate simulator."""
from typing import Dict, Set, Tuple, List
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
    dependencies: Dict[str, Set[str]] = {}
    for line in lines[split_idx:]:
        if not line.strip():
            continue
        # Extract gate type and wire names
        match = re.match(r'^(\w+)\s+(AND|OR|XOR)\s+(\w+)\s+->\s+(\w+)$', line)
        if not match:
            continue
        in1, gate_type, in2, out = match.groups()
        gates.append((in1, gate_type, in2, out))
        dependencies[out] = {in1, in2}

    # Topological Sort
    def topological_sort(deps: Dict[str, Set[str]]) -> List[str]:
        in_degree: Dict[str, int] = {node: 0 for node in deps.keys()}
        for node_deps in deps.values():
            for dep in node_deps:
                if dep in in_degree:
                    in_degree[dep] += 1

        queue: List[str] = [node for node in in_degree if in_degree[node] == 0]
        sorted_nodes: List[str] = []
        while queue:
            node = queue.pop(0)
            sorted_nodes.append(node)
            for dependent, node_deps in deps.items():
                if node in node_deps:
                    in_degree[dependent] -= 1
                    if in_degree[dependent] == 0:
                        queue.append(dependent)
        return sorted_nodes

    sorted_gates_output_wires = topological_sort(dependencies)

    # Process gates in topological order
    for out in sorted_gates_output_wires:
        for in1, gate_type, in2, gate_out in gates:
            if gate_out == out:
                val1 = wires.get(in1)
                val2 = wires.get(in2)
                if val1 is not None and val2 is not None:
                     if gate_type == 'AND':
                        wires[out] = 1 if val1 and val2 else 0
                     elif gate_type == 'OR':
                        wires[out] = 1 if val1 or val2 else 0
                     else:  # XOR
                        wires[out] = 1 if val1 != val2 else 0


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
