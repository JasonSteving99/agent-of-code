"""
This test suite validates the `generate_secret_number` function that generates the 2000th
pseudorandom secret number in a sequence starting from a given initial secret number.

Key test coverage:
- Verifies correct generation of the 2000th secret number for small input values (1, 10)
- Verifies correct generation for larger input values (100, 2024)
- Each test validates a specific input-output pair from the provided examples
"""

from solution import generate_secret_number


def test_generate_secret_from_one():
    """Test generation of 2000th secret number starting from initial value 1."""
    initial_secret = 1
    expected_2000th_secret = 8685429
    result = generate_secret_number(initial_secret)
    assert result == expected_2000th_secret, \
        f"For initial secret {initial_secret}, expected 2000th number to be {expected_2000th_secret}, but got {result}"


def test_generate_secret_from_ten():
    """Test generation of 2000th secret number starting from initial value 10."""
    initial_secret = 10
    expected_2000th_secret = 4700978
    result = generate_secret_number(initial_secret)
    assert result == expected_2000th_secret, \
        f"For initial secret {initial_secret}, expected 2000th number to be {expected_2000th_secret}, but got {result}"


def test_generate_secret_from_hundred():
    """Test generation of 2000th secret number starting from initial value 100."""
    initial_secret = 100
    expected_2000th_secret = 15273692
    result = generate_secret_number(initial_secret)
    assert result == expected_2000th_secret, \
        f"For initial secret {initial_secret}, expected 2000th number to be {expected_2000th_secret}, but got {result}"


def test_generate_secret_from_2024():
    """Test generation of 2000th secret number starting from initial value 2024."""
    initial_secret = 2024
    expected_2000th_secret = 8667524
    result = generate_secret_number(initial_secret)
    assert result == expected_2000th_secret, \
        f"For initial secret {initial_secret}, expected 2000th number to be {expected_2000th_secret}, but got {result}"