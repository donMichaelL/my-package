from .exceptions import InvalidInputError


def add_numbers(a, b) -> int:
    """
    Adds two numbers together.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        int: The total sum.

    Raises:
        InvalidInputError: If either argument cannot be converted to an integer.
    """
    try:
        val_a = int(a)
        val_b = int(b)
    except ValueError as e:
        raise InvalidInputError("Both arguments must be valid numbers.") from e

    return val_a + val_b
