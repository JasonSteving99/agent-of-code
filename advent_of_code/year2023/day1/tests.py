from advent_of_code.year2023.day1.solution import (
    sum_calibration_values,
)  # Assuming the code above is in your_module.py


def test_sum_calibration_values_case1():
    assert sum_calibration_values(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]) == 142


def test_sum_calibration_values_case2():
    assert (
        sum_calibration_values(
            [
                "two1nine",
                "eightwothree",
                "abcone2threexyz",
                "xtwone3four",
                "4nineeightseven2",
                "zoneight234",
                "7pqrstsixteen",
            ]
        )
        == 281
    )
