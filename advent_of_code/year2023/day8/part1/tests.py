# These tests cover examples of navigating a network of nodes based on a sequence of left/right instructions to arrive at the destination node `ZZZ` starting at the `AAA` node. The solution involves repeatedly cycling through the given instructions.

from solution import steps_to_reach_zzz
import pytest


@pytest.mark.parametrize("input_str, expected_output", [("RL\n\nAAA = (BBB, CCC)\nBBB = (DDD, EEE)\nCCC = (ZZZ, GGG)\nDDD = (DDD, DDD)\nEEE = (EEE, EEE)\nGGG = (GGG, GGG)\nZZZ = (ZZZ, ZZZ)", 2), ("LLR\n\nAAA = (BBB, BBB)\nBBB = (AAA, ZZZ)\nZZZ = (ZZZ, ZZZ)", 6)])
def test_steps_to_reach_zzz(input_str, expected_output):
    actual_output = steps_to_reach_zzz(input_str)
    assert actual_output == expected_output, f"For input {input_str!r}, expected output {expected_output!r}, but got {actual_output!r}"
