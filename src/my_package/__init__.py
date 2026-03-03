import logging
from importlib.metadata import PackageNotFoundError, version

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def main() -> None:
    try:
        pkg_version = version("my-package")
    except PackageNotFoundError:
        pkg_version = "unknown (not installed)"

    logger.info(f"Starting my-package v{pkg_version}")
