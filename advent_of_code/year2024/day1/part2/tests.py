"""Unit tests for the calculate_similarity_score function.

The function takes a string input representing two lists of integers formatted as pairs
separated by newlines, where each pair has two numbers separated by whitespace.
It calculates a similarity score based on counting matches between the first number
of each pair with the second numbers.

Example input format:
3   4
4   3
2   5
...

Each line contains two integers separated by whitespace. The first number in each pair
represents an ID from the first list, and the second number represents an ID from the
second list.

The function should calculate how many times each first number appears as a second number
in other pairs, accumulating these matches into a total similarity score.
"""

from solution import calculate_similarity_score

def test_basic_similarity_score():
    # Given a string with multiple number pairs where some numbers match across columns
    input_data = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    
    # When calculating the similarity score
    result = calculate_similarity_score(input_data)
    
    # Then it should return 31 based on the matching patterns
    # The explanation for score 31:
    # - First column numbers [3,4,2,1,3,3] matching against
    # - Second column numbers [4,3,5,3,9,3]
    assert result == 31, (
        f"Expected similarity score of 31 for input:\n{input_data}\n"
        f"but got {result}"
    )

def test_empty_input():
    # Given an empty string input
    input_data = ""
    
    # When calculating the similarity score
    result = calculate_similarity_score(input_data)
    
    # Then it should return 0 as there are no pairs to compare
    assert result == 0, (
        f"Expected similarity score of 0 for empty input, but got {result}"
    )

def test_single_pair():
    # Given a string with just one pair of numbers
    input_data = "1   2"
    
    # When calculating the similarity score
    result = calculate_similarity_score(input_data)
    
    # Then it should return 0 as there is only one pair with no matches
    assert result == 0, (
        f"Expected similarity score of 0 for single pair input:\n{input_data}\n"
        f"but got {result}"
    )

def test_all_matching_pairs():
    # Given a string where all pairs have matching numbers
    input_data = "1   1\n1   1\n1   1"
    
    # When calculating the similarity score
    result = calculate_similarity_score(input_data)
    
    # Then it should return a score reflecting all matches
    assert result == 9, (
        f"Expected similarity score of 9 for all matching pairs:\n{input_data}\n"
        f"but got {result}"
    )