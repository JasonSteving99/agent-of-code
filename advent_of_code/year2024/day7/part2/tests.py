"""
This test suite verifies the evaluate_expression function that determines if a set of numbers can 
evaluate to a target number using concatenation (||), addition (+), and multiplication (*) operators.
The operators are evaluated from left to right and numbers cannot be rearranged.

Input format: "target: num1 num2 num3 ..." where target and nums are positive integers
Output: Returns the target number if the numbers can evaluate to it using the allowed operations
"""

from solution import evaluate_expression


def test_two_numbers_evaluation():
    """Test evaluating expression with two numbers."""
    input_str = "156: 15 6"
    result = evaluate_expression(input_str)
    assert result == 156, f"For input '{input_str}', expected 156 but got {result}"


def test_four_numbers_evaluation():
    """Test evaluating expression with four numbers."""
    input_str = "7290: 6 8 6 15"
    result = evaluate_expression(input_str)
    assert result == 7290, f"For input '{input_str}', expected 7290 but got {result}"


def test_three_numbers_small_target():
    """Test evaluating expression with three numbers and a small target."""
    input_str = "192: 17 8 14"
    result = evaluate_expression(input_str)
    assert result == 192, f"For input '{input_str}', expected 192 but got {result}"


def test_two_numbers_medium_target():
    """Test evaluating expression with two numbers and a medium target."""
    input_str = "190: 10 19"
    result = evaluate_expression(input_str)
    assert result == 190, f"For input '{input_str}', expected 190 but got {result}"


def test_three_numbers_large_target():
    """Test evaluating expression with three numbers and a large target."""
    input_str = "3267: 81 40 27"
    result = evaluate_expression(input_str)
    assert result == 3267, f"For input '{input_str}', expected 3267 but got {result}"


def test_four_numbers_small_target():
    """Test evaluating expression with four numbers and a small target."""
    input_str = "292: 11 6 16 20"
    result = evaluate_expression(input_str)
    assert result == 292, f"For input '{input_str}', expected 292 but got {result}"