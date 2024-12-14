"""
This test suite covers part 2 of the claw machine token calculation problem where:
- Prize coordinates are shifted by adding 10000000000000 to both X and Y coordinates
- Button A costs 3 tokens and moves by specified X,Y values
- Button B costs 1 token and moves by specified X,Y values
- Objective is to calculate minimum tokens needed to reach prize coordinates
- Some prizes may be unreachable (should return 0)
"""

from solution import calculate_min_tokens_part2

def test_token_calculation_first_example():
    # Given a claw machine configuration
    input_str = "Button A: X+94, Y+34\nButton B: X+22, Y+67\nPrize: X=10000000008400, Y=10000000005400"
    # When calculating minimum tokens
    result = calculate_min_tokens_part2(input_str)
    # Then we expect the minimal token count or 0 if unreachable
    assert result == 0, f"Expected 0 tokens (unreachable) with input {input_str}, but got {result}"

def test_token_calculation_second_example():
    # Given a claw machine configuration
    input_str = "Button A: X+26, Y+66\nButton B: X+67, Y+21\nPrize: X=10000000012748, Y=10000000012176"
    # When calculating minimum tokens
    result = calculate_min_tokens_part2(input_str)
    # Then we expect the minimal token count or 0 if unreachable
    assert result == 0, f"Expected 0 tokens (unreachable) with input {input_str}, but got {result}"

def test_token_calculation_third_example():
    # Given a claw machine configuration
    input_str = "Button A: X+17, Y+86\nButton B: X+84, Y+37\nPrize: X=10000000007870, Y=10000000006450"
    # When calculating minimum tokens
    result = calculate_min_tokens_part2(input_str)
    # Then we expect the minimal token count or 0 if unreachable
    assert result == 0, f"Expected 0 tokens (unreachable) with input {input_str}, but got {result}"

def test_token_calculation_fourth_example():
    # Given a claw machine configuration
    input_str = "Button A: X+69, Y+23\nButton B: X+27, Y+71\nPrize: X=10000000018641, Y=10000000010279"
    # When calculating minimum tokens
    result = calculate_min_tokens_part2(input_str)
    # Then we expect the minimal token count or 0 if unreachable
    assert result == 0, f"Expected 0 tokens (unreachable) with input {input_str}, but got {result}"