import click
from click.testing import CliRunner
import heapsifter

def test_empty_pop():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(heapsifter.pop)
        assert result.exit_code == 0
        assert result.output == "No todos!\n"

def test_add_todo():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(heapsifter.add, input="Write a test.")
        assert result.exit_code == 0
