"""
This test suite covers the similarity score calculation between two lists of numbers represented as a string.
The score is calculated by taking each number from the left list and multiplying it by its frequency
in the right list, then summing all these products.

For the example input "3   4\n4   3\n2   5\n1   3\n3   9\n3   3":
- Left list: [3,4,2,1,3,3]
- Right list: [4,3,5,3,9,3]
- 3 appears in left 3 times and matches 3 in right 3 times: 3 * 3 = 9
- 4 appears in left once and matches nothing in right: 4 * 0 = 0
- 2 appears in left once and matches nothing in right: 2 * 0 = 0
- 1 appears in left once and matches nothing in right: 1 * 0 = 0
Total score = 31
"""

from solution import calculate_similarity_score
import pytest


def test_example_similarity_score():
    input_str = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    expected_score = 31
    
    result = calculate_similarity_score(input_str)
    
    assert result == expected_score, (
        f"Failed to calculate correct similarity score.\n"
        f"Input: {input_str}\n"
        f"Expected: {expected_score}\n"
        f"Got: {result}"
    )


def test_empty_input():
    """Test handling of empty input string"""
    input_str = ""
    expected_score = 0
    
    result = calculate_similarity_score(input_str)
    
    assert result == expected_score, (
        f"Failed to handle empty input string.\n"
        f"Expected: {expected_score}\n"
        f"Got: {result}"
    )


def test_single_line_input():
    """Test with just one pair of numbers"""
    input_str = "3   3"
    expected_score = 3
    
    result = calculate_similarity_score(input_str)
    
    assert result == expected_score, (
        f"Failed to calculate score for single line input.\n"
        f"Input: {input_str}\n"
        f"Expected: {expected_score}\n"
        f"Got: {result}"
    )


def test_no_matches():
    """Test when there are no matching numbers between lists"""
    input_str = "1   2\n3   4"
    expected_score = 0
    
    result = calculate_similarity_score(input_str)
    
    assert result == expected_score, (
        f"Failed to calculate score when no matches exist.\n"
        f"Input: {input_str}\n"
        f"Expected: {expected_score}\n"
        f"Got: {result}"
    )