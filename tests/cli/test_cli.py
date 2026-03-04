from click.testing import CliRunner

from my_package.cli import main


def test_version_flag_outputs_correct_string() -> None:
    """Test that the --version flag outputs the correct version string."""
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert "my-package, version " in result.output


def test_main_execution_without_args() -> None:
    """Test that running the main function without any arguments executes successfully."""
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0
