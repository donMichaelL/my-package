import logging

from .exceptions import InvalidInputError

# This creates a logger specifically named "my_package.services"
logger = logging.getLogger(__name__)


def process_large_data(data: list) -> int:
    """Processes a large dataset."""
    logger.debug("Starting to process %d items", len(data))

    try:
        result = len(data) * 2
    except Exception as e:
        logger.error("Failed to process data: %s", e)
        raise InvalidInputError("Data processing failed") from e

    logger.debug("Finished processing data successfully.")

    return result
