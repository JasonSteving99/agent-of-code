"""
Test module for the calculate_similarity_score function.

The function takes a string input containing two space-separated integers per line,
where the first column represents the first list and the second column represents 
the second list. The function calculates a similarity score by:
1. Taking each unique number from the first list
2. Counting how many times it appears in the second list
3. Multiplying these counts by the original number
4. Summing all these products

For example, given the input "3 4\n4 3\n2 5\n1 3\n3 9\n3 3":
- 3 appears 3 times in second list (3 × 3 = 9), and it appears 3 times in first list so total = 27
- 4 appears 1 time in second list (4 × 1 = 4)
- 2 appears 0 times in second list (2 × 0 = 0)
- 1 appears 0 times in second list (1 × 0 = 0)
Total score = 27 + 4 + 0 + 0 = 31
"""

import pytest
from solution import calculate_similarity_score

def test_calculate_similarity_score_with_mixed_numbers():
    input_str = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    expected_score = 31
    
    result = calculate_similarity_score(input_str)
    
    assert result == expected_score, (
        f"Expected similarity score of {expected_score} for input:\n{input_str}\n"
        f"but got {result} instead"
    )

def test_calculate_similarity_score_with_empty_string():
    """Test edge case with empty input string"""
    input_str = ""
    expected_score = 0
    
    result = calculate_similarity_score(input_str)
    
    assert result == expected_score, (
        f"Expected similarity score of {expected_score} for empty input "
        f"but got {result} instead"
    )

def test_calculate_similarity_score_with_single_line():
    """Test case with just one pair of numbers"""
    input_str = "5   3"
    expected_score = 0  # 5 doesn't appear in second list
    
    result = calculate_similarity_score(input_str)
    
    assert result == expected_score, (
        f"Expected similarity score of {expected_score} for input:\n{input_str}\n"
        f"but got {result} instead"
    )

def test_calculate_similarity_score_with_perfect_match():
    """Test case where numbers in first list all appear in second list"""
    input_str = "1   1\n2   2\n3   3"
    expected_score = 6  # (1×1) + (2×1) + (3×1) = 6
    
    result = calculate_similarity_score(input_str)
    
    assert result == expected_score, (
        f"Expected similarity score of {expected_score} for input:\n{input_str}\n"
        f"but got {result} instead"
    )