"""Unit tests for the 3-bit computer emulator function.

These tests validate the behavior of a function that emulates a 3-bit computer.
The function takes a string of comma-separated 3-bit numbers representing the program,
along with initial values for three registers (A, B, C).

The tests cover different program inputs and expected outputs based on 
various initial register states and program instructions.
"""

from solution import run_3bit_computer
import pytest

def test_simple_two_instruction_program():
    """Test a simple program with two instructions (2,6)."""
    program = "2,6"
    # Assuming default register values of 0
    result = run_3bit_computer(program, 0, 0, 0)
    assert result == "1", f"Program '{program}' with registers A=0,B=0,C=0 should output '1', got '{result}'"

def test_six_instruction_program():
    """Test a program with six instructions (5,0,5,1,5,4)."""
    program = "5,0,5,1,5,4"
    result = run_3bit_computer(program, 0, 0, 0)
    assert result == "0,1,2", f"Program '{program}' with registers A=0,B=0,C=0 should output '0,1,2', got '{result}'"

def test_six_instruction_program_first_variation():
    """Test first variation of six instruction program (0,1,5,4,3,0)."""
    program = "0,1,5,4,3,0"
    result = run_3bit_computer(program, 0, 0, 0)
    assert result == "4,2,5,6,7,7,7,7,3,1,0", (
        f"Program '{program}' with registers A=0,B=0,C=0 should output "
        f"'4,2,5,6,7,7,7,7,3,1,0', got '{result}'"
    )

def test_two_instruction_program_different_values():
    """Test another two instruction program (1,7)."""
    program = "1,7"
    result = run_3bit_computer(program, 0, 0, 0)
    assert result == "26", f"Program '{program}' with registers A=0,B=0,C=0 should output '26', got '{result}'"

def test_two_instruction_different_sequence():
    """Test two instruction sequence (4,0)."""
    program = "4,0"
    result = run_3bit_computer(program, 0, 0, 0)
    assert result == "44354", f"Program '{program}' with registers A=0,B=0,C=0 should output '44354', got '{result}'"

def test_six_instruction_program_second_variation():
    """Test second variation of six instruction program (0,1,5,4,3,0)."""
    program = "0,1,5,4,3,0"
    result = run_3bit_computer(program, 0, 0, 0)
    assert result == "4,6,3,5,6,3,5,2,1,0", (
        f"Program '{program}' with registers A=0,B=0,C=0 should output "
        f"'4,6,3,5,6,3,5,2,1,0', got '{result}'"
    )