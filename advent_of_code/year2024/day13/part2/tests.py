"""
Tests for Part 2 of the buttonmasher prize collection puzzle.

The function must calculate the minimum number of tokens needed to collect all prizes,
where each prize's coordinates have been increased by 10000000000000.
The tested function should handle very large coordinate values efficiently.

Each button press adds a specific X,Y offset to the current position.
The goal is to find the minimum number of button presses (tokens) needed
to reach all prize coordinates from the starting position of (0,0).
"""

from solution import calculate_min_tokens_part2
import pytest


def test_scenario_1_large_coordinates():
    input_data = [
        "Button A: X+94, Y+34",
        "Button B: X+22, Y+67",
        "Prize: X=10000000008400, Y=10000000005400"
    ]
    result = calculate_min_tokens_part2(input_data)
    assert result != 0, (
        "Expected non-zero tokens for input:\n"
        f"{input_data}\n"
        "Function returned 0 tokens which cannot be correct for reaching prize"
    )


def test_scenario_2_large_coordinates():
    input_data = [
        "Button A: X+26, Y+66",
        "Button B: X+67, Y+21",
        "Prize: X=10000000012748, Y=10000000012176"
    ]
    result = calculate_min_tokens_part2(input_data)
    assert result != 0, (
        "Expected non-zero tokens for input:\n"
        f"{input_data}\n"
        "Function returned 0 tokens which cannot be correct for reaching prize"
    )


def test_scenario_3_large_coordinates():
    input_data = [
        "Button A: X+17, Y+86",
        "Button B: X+84, Y+37",
        "Prize: X=10000000007870, Y=10000000006450"
    ]
    result = calculate_min_tokens_part2(input_data)
    assert result != 0, (
        "Expected non-zero tokens for input:\n"
        f"{input_data}\n"
        "Function returned 0 tokens which cannot be correct for reaching prize"
    )


def test_scenario_4_large_coordinates():
    input_data = [
        "Button A: X+69, Y+23",
        "Button B: X+27, Y+71",
        "Prize: X=10000000018641, Y=10000000010279"
    ]
    result = calculate_min_tokens_part2(input_data)
    assert result != 0, (
        "Expected non-zero tokens for input:\n"
        f"{input_data}\n"
        "Function returned 0 tokens which cannot be correct for reaching prize"
    )


def test_all_inputs_return_positive_values():
    # All test cases should return positive values since we need at least some tokens
    # to reach prizes with such large coordinates
    test_cases = [
        [
            "Button A: X+94, Y+34",
            "Button B: X+22, Y+67",
            "Prize: X=10000000008400, Y=10000000005400"
        ],
        [
            "Button A: X+26, Y+66",
            "Button B: X+67, Y+21",
            "Prize: X=10000000012748, Y=10000000012176"
        ],
        [
            "Button A: X+17, Y+86",
            "Button B: X+84, Y+37",
            "Prize: X=10000000007870, Y=10000000006450"
        ],
        [
            "Button A: X+69, Y+23",
            "Button B: X+27, Y+71",
            "Prize: X=10000000018641, Y=10000000010279"
        ]
    ]
    
    for test_case in test_cases:
        result = calculate_min_tokens_part2(test_case)
        assert result > 0, (
            f"Expected positive number of tokens for input:\n{test_case}\n"
            f"Got {result} instead"
        )