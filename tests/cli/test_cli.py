from click.testing import CliRunner

from my_package.cli import main


def test_version_flag_outputs_correct_string() -> None:
    """Test that the --version flag outputs the correct version string."""
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert "my-package, version " in result.output


def test_main_execution_without_args() -> None:
    """Test that running the CLI without a subcommand correctly throws a usage error."""
    runner = CliRunner()
    result = runner.invoke(main)

    assert result.exit_code == 2


def test_coffee_command_standard_logs():
    """Test that the coffee command prints INFO logs, but hides DEBUG logs by default."""
    runner = CliRunner()
    result = runner.invoke(main, ["coffee"])

    assert result.exit_code == 0
    assert "☕ I am a teapot. Just kidding, here is your virtual coffee!" in result.output
    assert "Checking virtual water temperature... perfect." not in result.output


def test_coffee_command_verbose_logs():
    """Test that the -v flag successfully reveals the DEBUG logs."""
    runner = CliRunner()
    result = runner.invoke(main, ["-v", "coffee"])

    assert result.exit_code == 0
    assert "☕ I am a teapot. Just kidding, here is your virtual coffee!" in result.output
    assert "Checking virtual water temperature... perfect." in result.output
