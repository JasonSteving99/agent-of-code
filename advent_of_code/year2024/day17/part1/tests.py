"""
Test suite for the Chronospatial Computer implementation.

These tests verify that the Chronospatial Computer correctly executes programs given as 
comma-separated strings of integers and produces expected outputs based on initial register values.
The computer appears to have three registers (A, B, C) with default values, and the output
is either the sequence of outputs during program execution or the final B register value.
"""

from solution import run_chronospatial_computer
import pytest

def test_simple_program_with_default_registers():
    program = "2,6"
    expected_output = "1"
    result = run_chronospatial_computer(program, 10, 29, 9)
    assert result == expected_output, \
        f"Program '{program}' with A=10,B=29,C=9 should output '{expected_output}' but got '{result}'"

def test_multiple_output_program_with_default_registers():
    program = "5,0,5,1,5,4"
    expected_output = "0,1,2"
    result = run_chronospatial_computer(program, 10, 29, 9)
    assert result == expected_output, \
        f"Program '{program}' with A=10,B=29,C=9 should output '{expected_output}' but got '{result}'"

def test_longer_output_sequence_with_default_registers_1():
    program = "0,1,5,4,3,0"
    expected_output = "4,2,5,6,7,7,7,7,3,1,0"
    result = run_chronospatial_computer(program, 10, 29, 9)
    assert result == expected_output, \
        f"Program '{program}' with A=10,B=29,C=9 should output '{expected_output}' but got '{result}'"

def test_single_output_program_with_default_registers():
    program = "1,7"
    expected_output = "26"
    result = run_chronospatial_computer(program, 10, 29, 9)
    assert result == expected_output, \
        f"Program '{program}' with A=10,B=29,C=9 should output '{expected_output}' but got '{result}'"

def test_larger_output_with_default_registers():
    program = "4,0"
    expected_output = "44354"
    result = run_chronospatial_computer(program, 10, 29, 9)
    assert result == expected_output, \
        f"Program '{program}' with A=10,B=29,C=9 should output '{expected_output}' but got '{result}'"

def test_with_custom_register_values():
    program = "0,1,5,4,3,0"
    expected_output = "4,6,3,5,6,3,5,2,1,0"
    result = run_chronospatial_computer(program, 729, 0, 0)
    assert result == expected_output, \
        f"Program '{program}' with A=729,B=0,C=0 should output '{expected_output}' but got '{result}'"