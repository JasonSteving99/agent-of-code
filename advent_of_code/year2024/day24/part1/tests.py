"""Unit tests for a logic gate simulator that processes wire definitions and gate connections.

The tests cover:
1. Basic gate operations (AND, OR, XOR) with simple circuits
2. Complex circuits with multiple gates and wire dependencies 
3. Edge cases with duplicate gate definitions and same output wire definitions
4. Circuits where the decimal output is formed from multiple z-wires in order (z00 being LSB)
"""

from solution import simulate_logic_gates
import pytest


def test_simple_circuit_with_three_gates():
    """Test a simple circuit with one each of AND, XOR, and OR gates."""
    input_circuit = """x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02"""
    
    result = simulate_logic_gates(input_circuit)
    # Expected output calculation:
    # z00 = 1 AND 0 = 0
    # z01 = 1 XOR 1 = 0
    # z02 = 1 OR 0 = 1
    # Binary: 100 = Decimal: 4
    assert result == 4, f"Expected 4 for input:\n{input_circuit}\nGot {result} instead"


def test_complex_circuit_with_duplicate_and_overwritten_definitions():
    """Test a complex circuit with duplicate gate definitions and overwritten wire definitions."""
    input_circuit = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kpq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""

    result = simulate_logic_gates(input_circuit)
    # Expected decimal value: 2024
    assert result == 2024, f"Expected 2024 for complex circuit with duplicate definitions. Got {result} instead"