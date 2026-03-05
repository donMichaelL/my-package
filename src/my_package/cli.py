import logging
from importlib.metadata import PackageNotFoundError, version

import click

logger = logging.getLogger(__name__)


def get_version() -> str:
    try:
        return version("my-package")
    except PackageNotFoundError:
        return "unknown"


@click.group()
@click.version_option(version=get_version(), prog_name="my-package")
@click.option("-v", "--verbose", is_flag=True, help="Enable verbose debug logging.")
def main(verbose: bool) -> None:
    log_level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s", force=True)
    logger.debug("Logging system initialized in CLI.")


@main.command(name="coffee", hidden=True)
def coffee() -> None:
    """This docstring won't show up in the help menu!"""
    logger.info("☕ I am a teapot. Just kidding, here is your virtual coffee!")
    logger.debug("Checking virtual water temperature... perfect.")


if __name__ == "__main__":
    main()
