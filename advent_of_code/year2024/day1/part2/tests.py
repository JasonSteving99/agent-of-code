"""
Tests for the calculate_similarity_score function that computes a similarity score
between two columns of numbers.

The tests verify that:
1. The function correctly parses input string containing space-separated number pairs
2. The function properly counts matches between numbers in the first and second column
3. The function handles multiple occurrences of the same number correctly
4. The function returns the expected integer score based on the matches found

Function signature:
calculate_similarity_score(input_str: str) -> int
"""

from solution import calculate_similarity_score


def test_calculate_similarity_score_with_mixed_matches():
    # Test case with a mix of matching and non-matching numbers
    input_str = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    expected_score = 31
    
    result = calculate_similarity_score(input_str)
    
    # Detailed assertion message showing input and expected vs actual output
    assert result == expected_score, (
        f"Failed for input:\n{input_str}\n"
        f"Expected score: {expected_score}, but got: {result}"
    )
    
    # The test verifies that for the input where:
    # First column:  [3, 4, 2, 1, 3, 3]
    # Second column: [4, 3, 5, 3, 9, 3]
    # The function calculates the correct similarity score of 31