"""Solution to run a 3-bit virtual machine."""

import sys
from typing import List, Optional


class VirtualMachine:
    """A 3-bit virtual machine with registers A, B, C."""

    def __init__(self, register_a: int = 0, register_b: int = 0, register_c: int = 0):
        self.registers = {'A': register_a, 'B': register_b, 'C': register_c}
        self.instruction_pointer = 0
        self.outputs: List[int] = []

    def get_combo_value(self, operand: int) -> int:
        """Get value based on combo operand rules."""
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return self.registers['A']
        if operand == 5:
            return self.registers['B']
        if operand == 6:
            return self.registers['C']
        return 0  # operand 7 is reserved

    def execute_instruction(self, opcode: int, operand: int) -> None:
        """Execute a single instruction."""
        if opcode == 0:  # adv
            self.registers['A'] //= 1 << self.get_combo_value(operand)
        elif opcode == 1:  # bxl
            self.registers['B'] ^= operand
        elif opcode == 2:  # bst
            self.registers['B'] = self.get_combo_value(operand) % 8
        elif opcode == 3:  # jnz
            if self.registers['A'] != 0:
                self.instruction_pointer = operand
                return
        elif opcode == 4:  # bxc
            self.registers['B'] ^= self.registers['C']
        elif opcode == 5:  # out
            self.outputs.append(self.get_combo_value(operand) % 8)
        elif opcode == 6:  # bdv
            self.registers['B'] = self.registers['A'] // (1 << self.get_combo_value(operand))
        elif opcode == 7:  # cdv
            self.registers['C'] = self.registers['A'] // (1 << self.get_combo_value(operand))

        self.instruction_pointer += 2

    def run_program(self, program: List[int]) -> None:
        """Run the program until it halts."""
        while self.instruction_pointer < len(program):
            self.execute_instruction(program[self.instruction_pointer], 
                                  program[self.instruction_pointer + 1])


def parse_input() -> tuple[list[int], dict[str, int]]:
    """Parse the input from stdin."""
    registers = {'A': 0, 'B': 0, 'C': 0}
    # Read register values
    for _ in range(3):
        line = sys.stdin.readline().strip()
        if line:
            reg, val = line.split(': ')
            reg = reg.split()[-1]  # Get just the register letter
            registers[reg] = int(val)
    
    # Skip empty line
    sys.stdin.readline()
    
    # Read program
    program_line = sys.stdin.readline().strip()
    if program_line.startswith('Program: '):
        program_line = program_line[9:]  # Remove "Program: " prefix
    
    program = [int(x) for x in program_line.split(',')]
    return program, registers


def run_virtual_machine(input_str: Optional[str] = None) -> str:
    """Run the virtual machine program and return comma-separated output."""
    if input_str is not None:
        # For testing, use the provided input string
        import io
        sys.stdin = io.StringIO(input_str)
    
    program, registers = parse_input()
    
    # Initialize and run the virtual machine
    vm = VirtualMachine(registers['A'], registers['B'], registers['C'])
    vm.run_program(program)
    
    # Return the output as a comma-separated string
    return ','.join(str(x) for x in vm.outputs)


if __name__ == '__main__':
    print(run_virtual_machine())