"""Unit tests for a 3-bit virtual machine implementation.

These tests verify the behavior of a virtual machine with 3 registers (A, B, C)
and 8 instructions by checking program execution outputs against expected values.
Tests cover different initial register states and various instruction sequences.

The tested function takes a comma-separated string of instruction opcodes/operands 
and returns a comma-separated string of values output during program execution.
"""

from solution import run_virtual_machine
import pytest

def test_simple_two_instruction_program():
    """Test a simple program with two instructions starting with A=10, B=29, C=9."""
    program = "2,6"
    expected_output = "1"
    actual_output = run_virtual_machine(program)
    assert actual_output == expected_output, \
        f"Program '{program}' with initial registers A=10,B=29,C=9 should output '{expected_output}' but got '{actual_output}'"

def test_program_outputs_three_values():
    """Test a program that outputs three values with initial A=10, B=29, C=9."""
    program = "5,0,5,1,5,4"
    expected_output = "0,1,2"
    actual_output = run_virtual_machine(program)
    assert actual_output == expected_output, \
        f"Program '{program}' with initial registers A=10,B=29,C=9 should output '{expected_output}' but got '{actual_output}'"

def test_program_outputs_eleven_values():
    """Test a program that outputs eleven values with initial A=10, B=29, C=9."""
    program = "0,1,5,4,3,0"
    expected_output = "4,2,5,6,7,7,7,7,3,1,0"
    actual_output = run_virtual_machine(program)
    assert actual_output == expected_output, \
        f"Program '{program}' with initial registers A=10,B=29,C=9 should output '{expected_output}' but got '{actual_output}'"

def test_two_instruction_program_computes_26():
    """Test a program that outputs the value 26 with initial A=10, B=29, C=9."""
    program = "1,7"
    expected_output = "26"
    actual_output = run_virtual_machine(program)
    assert actual_output == expected_output, \
        f"Program '{program}' with initial registers A=10,B=29,C=9 should output '{expected_output}' but got '{actual_output}'"

def test_two_instruction_program_computes_44354():
    """Test a program that outputs the value 44354 with initial A=10, B=29, C=9."""
    program = "4,0"
    expected_output = "44354"
    actual_output = run_virtual_machine(program)
    assert actual_output == expected_output, \
        f"Program '{program}' with initial registers A=10,B=29,C=9 should output '{expected_output}' but got '{actual_output}'"

def test_program_with_different_initial_registers():
    """Test a program with initial register values A=729, B=0, C=0."""
    program = "0,1,5,4,3,0"
    expected_output = "4,6,3,5,6,3,5,2,1,0"
    actual_output = run_virtual_machine(program)
    assert actual_output == expected_output, \
        f"Program '{program}' with initial registers A=729,B=0,C=0 should output '{expected_output}' but got '{actual_output}'"