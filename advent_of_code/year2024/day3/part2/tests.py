"""Test suite for the calculate_enabled_multiplications function.

This test suite verifies functionality of the calculate_enabled_multiplications function 
which processes a string containing multiplication instructions and do/don't control commands.
Key test aspects:
- Multiplication (mul) operations are enabled by default
- 'don't()' disables subsequent multiplications until a 'do()'
- Only the most recent do/don't command affects future instructions
- The function returns an integer sum of all enabled multiplications
"""

from solution import calculate_enabled_multiplications


def test_multiplication_with_control_instructions():
    """Test example with mix of enabled/disabled multiplications."""
    # Complex input string with multiple multiplications and control instructions
    input_str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    expected_output = 8  # Sum of enabled multiplications: mul(2,4)=8
    
    result = calculate_enabled_multiplications(input_str)
    
    assert result == expected_output, (
        f"Failed with input '{input_str}'\n"
        f"Expected sum of enabled multiplications: {expected_output}\n"
        f"Got: {result}\n"
    )


def test_empty_string():
    """Test with empty input string should return 0."""
    input_str = ""
    expected_output = 0
    
    result = calculate_enabled_multiplications(input_str)
    
    assert result == expected_output, (
        f"Failed with empty input string\n"
        f"Expected: {expected_output}\n"
        f"Got: {result}"
    )


def test_no_valid_multiplications():
    """Test with string containing no valid multiplications."""
    input_str = "no_multiplications_here"
    expected_output = 0
    
    result = calculate_enabled_multiplications(input_str)
    
    assert result == expected_output, (
        f"Failed with input containing no multiplications: '{input_str}'\n"
        f"Expected: {expected_output}\n"
        f"Got: {result}"
    )