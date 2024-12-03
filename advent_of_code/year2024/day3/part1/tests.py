"""
This test suite covers the function sum_of_multiplications which:
1. Takes a string input containing potentially multiple 'mul(X,Y)' expressions
2. Identifies valid mul() expressions while ignoring malformed ones and other text
3. Calculates the product for each valid mul() expression
4. Returns the sum of all valid multiplication products

The test validates handling of:
- Valid mul() expressions mixed with invalid text
- Multiple consecutive valid mul() expressions
- Malformed multiplication expressions that should be ignored
- Various delimiter characters between expressions
"""

from solution import sum_of_multiplications

def test_mixed_valid_and_invalid_expressions():
    # Complex input with valid mul() calls mixed with invalid syntax and extra characters
    input_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    result = sum_of_multiplications(input_str)
    
    # Expected calculation:
    # mul(2,4) = 8
    # mul(3,7) = 21
    # mul(32,64) = 2048 (Invalid: closing bracket)
    # mul(11,8) = 88
    # mul(8,5) = 40

    assert result == 161, (
        f"Failed to correctly sum valid multiplication products.\n"
        f"Input: {input_str}\n"
        f"Expected: 161\n"
        f"Got: {result}\n"
        f"Should find and sum products from: mul(2,4)=8, mul(3,7)=21, mul(11,8)=88, mul(8,5)=40"
    )

def test_empty_string():
    # Test handling empty input
    input_str = ""
    result = sum_of_multiplications(input_str)
    assert result == 0, (
        f"Failed to handle empty string input.\n"
        f"Input: {input_str}\n"
        f"Expected: 0\n"
        f"Got: {result}\n"
        f"Should return 0 when no valid mul() expressions are found"
    )

def test_no_valid_multiplications():
    # Test string with no valid mul() expressions
    input_str = "mul[2,3] mul{4,5} mul(2,3 mul2,4) mul(a,b)"
    result = sum_of_multiplications(input_str)
    assert result == 0, (
        f"Failed to handle input with no valid mul() expressions.\n"
        f"Input: {input_str}\n"
        f"Expected: 0\n"
        f"Got: {result}\n"
        f"Should return 0 when no valid mul() expressions are found"
    )

def test_single_valid_multiplication():
    # Test single valid mul() expression
    input_str = "mul(10,20)"
    result = sum_of_multiplications(input_str)
    assert result == 200, (
        f"Failed to handle single valid mul() expression.\n"
        f"Input: {input_str}\n"
        f"Expected: 200\n"
        f"Got: {result}\n"
        f"Should correctly calculate mul(10,20)=200"
    )