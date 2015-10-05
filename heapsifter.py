from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from builtins import input
from builtins import open
from builtins import range
from builtins import int
from builtins import object
from future import standard_library
standard_library.install_aliases()
# coding: utf-8
import random 
import heapq
import functools

import click

def is_heap(passed_list):
    assert True


def insert_todo(todos, text):
    heapq.heappush(todos, TODO(text))


def review(todos):
    item = random.choice(todos)
    click.echo(item.text)
    review = input()
    item.text = review


def write_todos(todo_list, file_name):
    with open(file_name, mode='w') as my_file:
        for item in todo_list:
            print(item.text, file=my_file)


def read_todos(todo_file):
    try:
        with open(todo_file) as my_file:
            todos = [TODO(todo.strip()) for todo in  my_file if todo != '\n']
        return todos
    except FileNotFoundError:
        return []


def alt_read_todos(todo_file):
    return [TODO(todo.strip()) for todo in todo_file if todo != '\n']

    
def alt_write_todos(todo_file, todo_list):
    [print(item.text, file=todo_file) for item in todo_list]


@functools.lru_cache(maxsize=None)
def prioritize_or_equal(item_a, item_b):
    click.echo("a: {}".format(item_a))
    click.echo("b: {}".format(item_b))
    choice = click.prompt("More important? a/b/(e)qual")
    if choice == 'b':
        return 'less'
    elif choice == 'a':
        return 'greater'
    else:
        return 'equal'


@functools.total_ordering
class TODO(object):
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return "TODO({})".format(self.text)

    def __str__(self):
        return self.text

    def __eq__(self, other):
        if self.text < other.text:
            return prioritize_or_equal(self.text, other.text) == 'equal'
        else:
            return prioritize_or_equal(other.text, self.text) == 'equal'

    def __lt__(self, other):
        if self.text < other.text:
            return prioritize_or_equal(self.text, other.text) == 'greater'
        else:
            return prioritize_or_equal(other.text, self.text) == 'less'


@click.group()
def cli():
    pass


@cli.command()
@click.option('-i', '--insertion', prompt='Your todo',
              help='The string you want to add.')
@click.option('--todo_file', default='todo.txt',
              help='The text file destination.',
              type=click.Path())
def add(todo_file, insertion):
    todos = read_todos(todo_file)
    insert_todo(todos, insertion)
    write_todos(todos, todo_file)


@cli.command()
@click.option('--todo_file', default='todo.txt',
              help='The file to heap.',
              type=click.Path())
def heap_it(todo_file):
    todos = read_todos(todo_file)
    heapq.heapify(todos)
    write_todos(todos, todo_file)  

@cli.command()
@click.option('--todo_file', default='todo.txt',
              help='The todo file to review.',
              type=click.Path())
def pop(todo_file):
    todos = read_todos(todo_file)
    if len(todos) == 0:
        click.echo("No todos!")
        return 0
    click.echo(todos[0])
    choice = click.prompt("Mark [d]one, [r]epush, or [C]urrent?")
    if choice == 'd':
        heapq.heappop(todos)
    elif choice == 'r':
        heapq.heapreplace(todos, todos[0])
        # item = heapq.heappop(todos)
        # heapq.heappush(todos, item)
    write_todos(todos, todo_file)



def multi_delete(todo_list, indexes):
    """Remove the items specified by the indexes in a heap-preserving way."""
    indexes = list(reversed(sorted(indexes)))
    for index in indexes:
        todo_list[index] = todo_list[-1]
        todo_list.pop()
    list_len = len(todo_list)
    for index in indexes:
        if index < list_len:
            heapq._siftup(todo_list, index)
    return todo_list


@cli.command()
@click.option('--todo_file', default='todo.txt',
              help='The todo file to review.',
              type=click.Path())
def batch_remove(todo_file):
    todos = read_todos(todo_file)
    click.echo("Todos:")
    for item_tuple in enumerate(todos):
        click.echo("{}) {}".format(*item_tuple))
    target_list = []
    while True:
        resp = click.prompt("(q)uit or #")
        if resp == 'q':
            break
        else:
            try:
                target = int(resp)
                target_list.append(target)
            except TypeError:
                pass
    new_list = multi_delete(todos, target_list)
    write_todos(new_list, todo_file)


@cli.command()
@click.option('--todo_file', default='todo.txt',
              help='The todo file to review.',
              type=click.Path())
@click.option('-n', '--number', default=5,
              help='Number of todos to show.',
              type=click.INT)
def head(todo_file, number):
    todos = read_todos(todo_file)
    [click.echo(todos[n]) for n in range(number)]

if __name__ == '__main__':
    cli()
