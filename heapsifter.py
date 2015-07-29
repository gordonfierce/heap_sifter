# coding: utf-8
import random, heapq, functools

import click

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
class TODO:
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


@click.command()
@click.option('--insertion', prompt='Your todo',
              help='The string you want to add.')
@click.option('--todo_file', default='todo.txt',
              help='The text file destination.')
def add_todo(todo_file, insertion):
    todos = read_todos(todo_file)
    insert_todo(todos, insertion)
    write_todos(todos, todo_file)

@click.command()
@click.option('--file', default='todo.txt',
              help='The file to heap.')
def heap_it(todo_file):
    todos = read_todos(todo_file)
    heapq.heapify(todos)
    write_todos(todos, todo_file)

if __name__ == '__main__':
    add_todo()
