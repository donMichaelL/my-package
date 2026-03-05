from my_package import add_numbers


def test_add_numbers():
    """Test that the add_numbers function correctly sums two integers."""
    result = add_numbers(2, 3)
    assert result == 5

    # Let's test negative numbers too!
    assert add_numbers(-1, 1) == 0
