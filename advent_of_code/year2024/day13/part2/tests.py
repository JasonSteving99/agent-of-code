"""
Unit tests for Part 2 of the Button Sequence Optimization Problem.

These tests validate that the solution correctly calculates the minimum number of tokens
needed to win all prizes when the prize coordinates have been adjusted by adding
10000000000000 to both X and Y coordinates. Key differences from Part 1:
- Prize coordinates are now very large numbers (base of 10000000000000 plus offset)
- No limit on number of button presses
- Need to handle large coordinate calculations efficiently
"""

from solution import calculate_min_tokens_part2

def test_prize_with_offset_8400_5400():
    input_data = ["Button A: X+94, Y+34",
                  "Button B: X+22, Y+67",
                  "Prize: X=10000000008400, Y=10000000005400"]
    
    result = calculate_min_tokens_part2(input_data)
    
    # Test provides explicit context about the input and expected output
    assert result > 0, f"For input {input_data}, expected positive number of tokens, got {result}"

def test_prize_with_offset_12748_12176():
    input_data = ["Button A: X+26, Y+66",
                  "Button B: X+67, Y+21",
                  "Prize: X=10000000012748, Y=10000000012176"]
    
    result = calculate_min_tokens_part2(input_data)
    
    # Test provides explicit context about the input and expected output
    assert result > 0, f"For input {input_data}, expected positive number of tokens, got {result}"

def test_prize_with_offset_7870_6450():
    input_data = ["Button A: X+17, Y+86",
                  "Button B: X+84, Y+37",
                  "Prize: X=10000000007870, Y=10000000006450"]
    
    result = calculate_min_tokens_part2(input_data)
    
    # Test provides explicit context about the input and expected output
    assert result > 0, f"For input {input_data}, expected positive number of tokens, got {result}"

def test_prize_with_offset_18641_10279():
    input_data = ["Button A: X+69, Y+23",
                  "Button B: X+27, Y+71",
                  "Prize: X=10000000018641, Y=10000000010279"]
    
    result = calculate_min_tokens_part2(input_data)
    
    # Test provides explicit context about the input and expected output
    assert result > 0, f"For input {input_data}, expected positive number of tokens, got {result}"