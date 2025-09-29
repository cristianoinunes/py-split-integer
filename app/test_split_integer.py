import pytest
from app.split_integer import split_integer


def test_returns_correct_number_of_parts() -> None:
    result = split_integer(100, 7)
    assert len(result) == 7, (
        "Should return exactly 'number_of_parts' elements"
    )


def test_sum_of_parts_equals_value() -> None:
    value = 53
    parts = 5
    result = split_integer(value, parts)
    assert sum(result) == value, (
        "Parts should sum up to the original value"
    )


def test_array_is_sorted() -> None:
    result = split_integer(101, 7)
    assert result == sorted(result), (
        "Result should be sorted in ascending order"
    )


def test_difference_between_max_and_min_is_at_most_one() -> None:
    result = split_integer(101, 7)
    assert max(result) - min(result) <= 1, (
        "Difference between max and min must be ≤ 1"
    )


@pytest.mark.parametrize(
    "value, parts, expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
    ],
)
def test_example_cases(
    value: int, parts: int, expected: list[int]
) -> None:
    result = split_integer(value, parts)
    assert result == expected, f"Expected {expected}, got {result}"


@pytest.mark.parametrize(
    "value, parts",
    [
        (1, 1),
        (5, 5),
        (10, 3),
        (1000, 999),
        (999, 1000),
        (123456, 789),
        (0, 1),
    ],
)
def test_general_properties(value: int, parts: int) -> None:
    result = split_integer(value, parts)
    assert len(result) == parts, "Incorrect number of parts"
    assert sum(result) == value, "Incorrect total sum"
    assert result == sorted(result), "Array is not sorted"
    assert max(result) - min(result) <= 1, (
        "Max-min difference is greater than 1"
    )
