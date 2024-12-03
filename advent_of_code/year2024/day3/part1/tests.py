"""
Purpose of these tests:
1. Verify that only syntactically valid mul(x,y) expressions are processed
2. Confirm that invalid/malformed mul expressions are correctly ignored
3. Ensure proper handling of input strings with mixed valid/invalid mul operations
4. Test that valid mul operations with 1-3 digit numbers are correctly summed
"""

from solution import sum_valid_mul_operations

def test_complex_string_with_mixed_valid_invalid_operations():
    test_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    expected = 161  # 8 (from mul(2,4)) + 88 (from mul(11,8)) + 65 (from mul(8,5)) = 161
    result = sum_valid_mul_operations(test_input)
    assert result == expected, (
        f"Failed to correctly process mixed valid/invalid mul operations.\n"
        f"Input: {test_input}\n"
        f"Expected sum: {expected}\n"
        f"Got: {result}"
    )

def test_single_valid_mul_operation():
    test_input = "mul(10,20)"
    expected = 200  # Just 10 * 20
    result = sum_valid_mul_operations(test_input)
    assert result == expected, (
        f"Failed to process single valid mul operation.\n"
        f"Input: {test_input}\n"
        f"Expected: {expected}\n"
        f"Got: {result}"
    )

def test_empty_string():
    test_input = ""
    expected = 0  # No valid mul operations should return 0
    result = sum_valid_mul_operations(test_input)
    assert result == expected, (
        f"Failed to handle empty string input.\n"
        f"Input: {test_input}\n"
        f"Expected: {expected}\n"
        f"Got: {result}"
    )

def test_no_valid_mul_operations():
    test_input = "mul[5,6]mul{7,8}mul(a,b)mul(1,)mul(,2)mul(1.2,3)"
    expected = 0  # No valid mul operations should return 0
    result = sum_valid_mul_operations(test_input)
    assert result == expected, (
        f"Failed to handle string with only invalid mul operations.\n"
        f"Input: {test_input}\n"
        f"Expected: {expected}\n"
        f"Got: {result}"
    )

def test_multiple_valid_mul_operations():
    test_input = "mul(2,3)mul(4,5)mul(6,7)"
    expected = 62  # (2*3) + (4*5) + (6*7) = 6 + 20 + 42 = 62
    result = sum_valid_mul_operations(test_input)
    assert result == expected, (
        f"Failed to sum multiple valid mul operations.\n"
        f"Input: {test_input}\n"
        f"Expected: {expected}\n"
        f"Got: {result}"
    )

def test_valid_three_digit_numbers():
    test_input = "mul(123,456)mul(789,100)"
    expected = 135108  # (123*456) + (789*100) = 56088 + 78900 = 135108
    result = sum_valid_mul_operations(test_input)
    assert result == expected, (
        f"Failed to handle valid three-digit numbers.\n"
        f"Input: {test_input}\n"
        f"Expected: {expected}\n"
        f"Got: {result}"
    )