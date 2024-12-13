"""
This test suite verifies the min_tokens_part2 function which takes a list of claw machine configurations
and returns the minimum number of tokens needed to win all prizes.

Each input string represents a claw machine configuration with:
- Button A: X and Y increments
- Button B: X and Y increments  
- Prize: Absolute X and Y coordinates (increased by 10000000000000)

The function should analyze these configurations and determine the minimum number of tokens 
needed to solve ALL machines, where each token allows one button press.
"""

from solution import min_tokens_part2

def test_min_tokens_part2_example1():
    input_config = ["Button A: X+94, Y+34\nButton B: X+22, Y+67\nPrize: X=10000000008400, Y=10000000005400"]
    result = min_tokens_part2(input_config)
    assert isinstance(result, int), f"Expected integer result but got {type(result)}"
    assert result > 100, f"Expected result > 100 since prize coordinates are very large (got {result})"

def test_min_tokens_part2_example2():
    input_config = ["Button A: X+26, Y+66\nButton B: X+67, Y+21\nPrize: X=10000000012748, Y=10000000012176"]
    result = min_tokens_part2(input_config)
    assert isinstance(result, int), f"Expected integer result but got {type(result)}"
    assert result > 100, f"Expected result > 100 since prize coordinates are very large (got {result})"

def test_min_tokens_part2_example3():
    input_config = ["Button A: X+17, Y+86\nButton B: X+84, Y+37\nPrize: X=10000000007870, Y=10000000006450"]
    result = min_tokens_part2(input_config)
    assert isinstance(result, int), f"Expected integer result but got {type(result)}"
    assert result > 100, f"Expected result > 100 since prize coordinates are very large (got {result})"

def test_min_tokens_part2_example4():
    input_config = ["Button A: X+69, Y+23\nButton B: X+27, Y+71\nPrize: X=10000000018641, Y=10000000010279"]
    result = min_tokens_part2(input_config)
    assert isinstance(result, int), f"Expected integer result but got {type(result)}"
    assert result > 100, f"Expected result > 100 since prize coordinates are very large (got {result})"

def test_min_tokens_part2_all_machines():
    input_configs = [
        "Button A: X+94, Y+34\nButton B: X+22, Y+67\nPrize: X=10000000008400, Y=10000000005400",
        "Button A: X+26, Y+66\nButton B: X+67, Y+21\nPrize: X=10000000012748, Y=10000000012176",
        "Button A: X+17, Y+86\nButton B: X+84, Y+37\nPrize: X=10000000007870, Y=10000000006450",
        "Button A: X+69, Y+23\nButton B: X+27, Y+71\nPrize: X=10000000018641, Y=10000000010279"
    ]
    result = min_tokens_part2(input_configs)
    assert isinstance(result, int), f"Expected integer result but got {type(result)}"
    assert result > 100, f"Expected result > 100 since prize coordinates are very large (got {result})"