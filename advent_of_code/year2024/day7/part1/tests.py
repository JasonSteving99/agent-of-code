"""Unit tests for check_calibration_equation function focusing on determining if an equation string can be made true by inserting '+' or '*' operators between numbers.

These tests verify:
1. Basic case with two numbers where solution exists
2. Medium case with three numbers where solution exists
3. Complex case with four numbers where solution exists

The solution to be implemented should:
- Parse input strings in format "result: num1 num2 ..." to extract expected result and operand numbers
- Try different combinations of '+' and '*' operators between numbers
- Return the test value (before ':') if any operator combination makes equation true, 0 otherwise
"""

from solution import check_calibration_equation

def test_two_numbers_equation():
    test_input = "190: 10 19"
    result = check_calibration_equation(test_input)
    assert result == 190, f"Input '{test_input}' should return 190 as 10*19=190, but got {result}"

def test_three_numbers_equation():
    test_input = "3267: 81 40 27"
    result = check_calibration_equation(test_input)
    assert result == 3267, f"Input '{test_input}' should return 3267 as there exists a valid operator combination, but got {result}"

def test_four_numbers_equation():
    test_input = "292: 11 6 16 20"
    result = check_calibration_equation(test_input)
    assert result == 292, f"Input '{test_input}' should return 292 as there exists a valid operator combination, but got {result}"