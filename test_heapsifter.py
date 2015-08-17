import click
from click.testing import CliRunner
import heapsifter

def test_empty_pop():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(heapsifter.pop)
        assert result.exit_code == 0
        assert result.output == "No todos!\n"

