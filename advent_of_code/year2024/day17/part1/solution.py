"""Solution for running a 3-bit computer simulator."""
from typing import List

def run_3bit_computer(program_str: str, init_a: int, init_b: int, init_c: int) -> str:
    """Run the 3-bit computer program with given initial register values.
    
    Args:
        program_str: Comma-separated string of 3-bit numbers representing program instructions
        init_a: Initial value for register A
        init_b: Initial value for register B
        init_c: Initial value for register C
    
    Returns:
        A string of comma-separated values output by the program
    """
    # Convert program string to list of integers
    program = [int(x) for x in program_str.strip().split(',')]
    
    # Initialize registers
    registers = {'A': init_a, 'B': init_b, 'C': init_c}
    
    # Initialize instruction pointer and output list
    ip = 0
    outputs: List[int] = []
    
    def get_combo_value(operand: int) -> int:
        """Get value for combo operand based on rules."""
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
            power = get_combo_value(operand)
            registers['A'] = registers['A'] // (2 ** power)
            ip += 2
        elif opcode == 1:  # bxl
            registers['B'] ^= operand
            ip += 2
        elif opcode == 2:  # bst
            registers['B'] = get_combo_value(operand) % 8
            ip += 2
        elif opcode == 3:  # jnz
            if registers['A'] != 0:
                ip = operand
            else:
                ip += 2
        elif opcode == 4:  # bxc
            registers['B'] ^= registers['C']
            ip += 2
        elif opcode == 5:  # out
            outputs.append(get_combo_value(operand) % 8)
            ip += 2
        elif opcode == 6:  # bdv
            power = get_combo_value(operand)
            registers['B'] = registers['A'] // (2 ** power)
            ip += 2
        elif opcode == 7:  # cdv
            power = get_combo_value(operand)
            registers['C'] = registers['A'] // (2 ** power)
            ip += 2
        else:
            raise ValueError(f"Invalid opcode: {opcode}")
    
    return ','.join(str(x) for x in outputs)

def solution() -> str:
    """Read input from stdin and return the result as a string."""
    # Read and parse input
    lines = []
    while True:
        try:
            line = input().strip()
            if line:
                lines.append(line)
        except EOFError:
            break
    
    # Parse initial register values
    a = int(lines[0].split(': ')[1])
    b = int(lines[1].split(': ')[1])
    c = int(lines[2].split(': ')[1])
    
    # Get program string
    program = lines[4]
    
    # Run program and return output
    return run_3bit_computer(program, a, b, c)