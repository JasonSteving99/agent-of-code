"""
This test suite validates the simulate_logic_gates function which processes a circuit description consisting of:
1. Initial wire values section (format: wire_name: value)
2. Logic gate connections section (format: input1 GATE input2 -> output)
- Supported gates: AND, OR, XOR
- Output wires start with 'z' and their combined binary value represents the decimal result
"""

from solution import simulate_logic_gates


def test_simple_three_gate_circuit():
    # Simple circuit with 3 gates (AND, XOR, OR) and 6 input wires
    circuit = """x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02"""
    
    result = simulate_logic_gates(circuit)
    assert result == 4, (
        f"Circuit with inputs x00=1,x01=1,x02=1,y00=0,y01=1,y02=0 "
        f"expected to produce 4 (binary 100 from z02=1,z01=0,z00=0), but got {result}"
    )


def test_complex_circuit_with_multiple_gates():
    # Complex circuit with multiple interconnected gates and intermediate wires
    circuit = """x00: 1
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
kwq OR kpj -> z05
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
    
    result = simulate_logic_gates(circuit)
    assert result == 2024, (
        f"Complex circuit with multiple gates and intermediate wires "
        f"expected to produce 2024, but got {result}"
    )