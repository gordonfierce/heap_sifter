import click
from click.testing import CliRunner
import heapsifter

from heapsifter import is_heap

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

def test_add_arg():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(heapsifter.add, ["-i", "Pass todo directly."])
        assert result.exit_code == 0
        with open('todo.txt') as todos:
            assert todos.read() == "Pass todo directly.\n"

def test_is_heap():
    heap = [1, 2, 3, 4]
    assert is_heap(heap)
    not_heap = [34, 2, 3, 4, 10]
    assert not is_heap(not_heap)
