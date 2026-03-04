import logging
from importlib.metadata import PackageNotFoundError, version

import click

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def get_version() -> str:
    try:
        return version("my-package")
    except PackageNotFoundError:
        return "unknown"


@click.command()
@click.version_option(version=get_version(), prog_name="my-package")
def main() -> None:
    pass


if __name__ == "__main__":
    main()
