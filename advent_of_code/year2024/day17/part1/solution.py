from typing import List, Optional
import sys


def run_chronospatial_computer(program_str: str, init_a: int, init_b: int, init_c: int) -> str:
    # Parse program string into list of integers
    program = [int(x) for x in program_str.split(',')]
    
    # Initialize registers and instruction pointer
    registers = {'A': init_a, 'B': init_b, 'C': init_c}
    ip = 0
    output_values: List[int] = []
    
    def get_combo_operand(operand: int) -> int:
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return registers['A']
        elif operand == 5:
            return registers['B']
        elif operand == 6:
            return registers['C']
        else:  # operand == 7
            raise ValueError("Invalid combo operand 7")
    
    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1] if ip + 1 < len(program) else 0
        
        if opcode == 0:  # adv
            divisor = 1 << get_combo_operand(operand)  # 2^operand
            registers['A'] = registers['A'] // divisor
            ip += 2
        elif opcode == 1:  # bxl
            registers['B'] ^= operand  # XOR with literal operand
            ip += 2
        elif opcode == 2:  # bst
            registers['B'] = get_combo_operand(operand) % 8
            ip += 2
        elif opcode == 3:  # jnz
            if registers['A'] != 0:
                ip = operand
            else:
                ip += 2
        elif opcode == 4:  # bxc
            registers['B'] ^= registers['C']  # Ignore operand
            ip += 2
        elif opcode == 5:  # out
            output_value = get_combo_operand(operand) % 8
            output_values.append(output_value)
            ip += 2
        elif opcode == 6:  # bdv
            divisor = 1 << get_combo_operand(operand)
            registers['B'] = registers['A'] // divisor
            ip += 2
        elif opcode == 7:  # cdv
            divisor = 1 << get_combo_operand(operand)
            registers['C'] = registers['A'] // divisor
            ip += 2
        else:
            raise ValueError(f"Invalid opcode: {opcode}")
    
    if output_values:
        return ','.join(map(str,output_values))
    else:
        return str(registers['B'])


def solution() -> str:
    # Read input from stdin
    lines = sys.stdin.readlines()
    
    # Parse register values
    init_a = int(lines[0].strip().split(': ')[1])
    init_b = int(lines[1].strip().split(': ')[1])
    init_c = int(lines[2].strip().split(': ')[1])
    
    # Parse program
    program = lines[4].strip()
    
    return run_chronospatial_computer(program, init_a, init_b, init_c)