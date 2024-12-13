"""
This test suite validates the calculate_min_tokens function which determines the minimum number
of tokens needed to win a prize in a claw machine game. The tests verify:
1. The function correctly calculates token costs when using combinations of Button A (3 tokens)
   and Button B (1 token) to reach specific prize coordinates
2. Works with different starting positions and target coordinates
3. Handles the coordinate string parsing correctly
"""

from solution import calculate_min_tokens


def test_prize_configuration_with_larger_coordinates():
    machine_config = (
        "Button A: X+94, Y+34\n"
        "Button B: X+22, Y+67\n"
        "Prize: X=8400, Y=5400"
    )
    result = calculate_min_tokens(machine_config)
    assert result == 280, (
        f"Expected 280 tokens for configuration:\n{machine_config}\n"
        f"but got {result} tokens instead"
    )


def test_prize_configuration_with_smaller_movements():
    machine_config = (
        "Button A: X+17, Y+86\n"
        "Button B: X+84, Y+37\n"
        "Prize: X=7870, Y=6450"
    )
    result = calculate_min_tokens(machine_config)
    assert result == 200, (
        f"Expected 200 tokens for configuration:\n{machine_config}\n"
        f"but got {result} tokens instead"
    )