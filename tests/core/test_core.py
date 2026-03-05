import pytest

from my_package import InvalidInputError, add_numbers


def test_add_numbers_success():
    """Test that the add_numbers function correctly sums two positive integers."""
    assert add_numbers(2, 3) == 5


def test_add_numbers_with_invalid_string():
    """Test that passing non-numbers raises our custom InvalidInputError."""
    with pytest.raises(InvalidInputError) as exc_info:
        add_numbers("apple", 5)

    assert str(exc_info.value) == "Both arguments must be valid numbers."
