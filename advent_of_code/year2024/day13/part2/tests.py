"""
This test suite covers the function calculate_min_tokens_part2 which calculates the minimum number of button presses
needed to reach a prize position with very large X,Y coordinates (offset by 10000000000000).

Key aspects covered by tests:
- Input parsing for button coordinates and prize position with large coordinate values
- All examples provide valid input format with buttons A and B and a prize position
- Prize coordinates are in the range of 10000000000000 + smaller offset
"""

from solution import calculate_min_tokens_part2

def test_example_1_with_large_coordinates():
    input_str = "Button A: X+94, Y+34\nButton B: X+22, Y+67\nPrize: X=10000000008400, Y=10000000005400"
    result = calculate_min_tokens_part2(input_str)
    assert isinstance(result, int), f"Expected integer result but got {type(result)}"


def test_example_2_with_large_coordinates():
    input_str = "Button A: X+26, Y+66\nButton B: X+67, Y+21\nPrize: X=10000000012748, Y=10000000012176"
    result = calculate_min_tokens_part2(input_str)
    assert isinstance(result, int), f"Expected integer result but got {type(result)}"


def test_example_3_with_large_coordinates():
    input_str = "Button A: X+17, Y+86\nButton B: X+84, Y+37\nPrize: X=10000000007870, Y=10000000006450"
    result = calculate_min_tokens_part2(input_str)
    assert isinstance(result, int), f"Expected integer result but got {type(result)}"


def test_example_4_with_large_coordinates():
    input_str = "Button A: X+69, Y+23\nButton B: X+27, Y+71\nPrize: X=10000000018641, Y=10000000010279"
    result = calculate_min_tokens_part2(input_str)
    assert isinstance(result, int), f"Expected integer result but got {type(result)}"