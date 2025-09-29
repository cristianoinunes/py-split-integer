import pytest
from app.split_integer import split_integer


def test_returns_correct_number_of_parts() -> None:
    assert len(split_integer(100, 7)) == 7


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(53, 5)) == 53


def test_array_is_sorted() -> None:
    assert split_integer(101, 7) == sorted(split_integer(101, 7))


def test_difference_between_max_and_min_is_at_most_one() -> None:
    result = split_integer(101, 7)
    assert max(result) - min(result) <= 1


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(42, 1) == [42]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert result == sorted(result)


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
    assert split_integer(value, parts) == expected


@pytest.mark.parametrize(
    "value, parts",
    [
        (1, 1),
        (5, 5),
        (10, 3),
        (1000, 999),
        (999, 1000),
        (123456, 789),
        # Removed (0, 1) — not valid as per "positive integers" constraint
    ],
)
def test_general_properties(value: int, parts: int) -> None:
    result = split_integer(value, parts)
    assert len(result) == parts
    assert sum(result) == value
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
