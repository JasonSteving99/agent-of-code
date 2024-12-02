"""
Unit tests for the sum_calibration_values function that processes calibration values in two modes:
Part 1: Extracts first and last numerical digits from each line to form two-digit numbers
Part 2: Same as Part 1 but also considers spelled out numbers (e.g., 'one', 'two', etc.)
"""

from solution import sum_calibration_values
import pytest

def test_sum_calibration_with_numeric_digits_only():
    """Test processing input with only numeric digits (Part 1)."""
    puzzle_input = "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet"
    expected_output = "142"
    
    result = sum_calibration_values(puzzle_input)
    
    assert result == expected_output, (
        f"Failed to sum calibration values correctly for input with numeric digits only.\n"
        f"Input:\n{puzzle_input}\n"
        f"Expected sum: {expected_output}\n"
        f"Got: {result}"
    )

def test_sum_calibration_with_spelled_out_numbers():
    """Test processing input that includes spelled out numbers (Part 2)."""
    puzzle_input = ("two1nine\neightwothree\nabcone2threexyz\n"
                   "xtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen")
    expected_output = "281"
    
    result = sum_calibration_values(puzzle_input)
    
    assert result == expected_output, (
        f"Failed to sum calibration values correctly for input including spelled out numbers.\n"
        f"Input:\n{puzzle_input}\n"
        f"Expected sum: {expected_output}\n"
        f"Got: {result}"
    )

def test_empty_input():
    """Test handling of empty input."""
    result = sum_calibration_values("")
    assert result == "0", (
        f"Failed to handle empty input correctly.\n"
        f"Expected: '0'\n"
        f"Got: {result}"
    )

def test_single_line_input():
    """Test processing of a single line input."""
    puzzle_input = "1abc2"
    expected_output = "12"
    
    result = sum_calibration_values(puzzle_input)
    
    assert result == expected_output, (
        f"Failed to process single line input correctly.\n"
        f"Input: {puzzle_input}\n"
        f"Expected: {expected_output}\n"
        f"Got: {result}"
    )