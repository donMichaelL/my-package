class MyPackageError(Exception):
    """Base exception for all errors in my-package."""

    pass


class InvalidInputError(MyPackageError):
    """Raised when the provided input cannot be processed as a number."""

    pass
