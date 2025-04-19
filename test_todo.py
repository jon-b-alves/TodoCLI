import pytest
from todo import load_tasks

TODO_FILE = 'data/todo.json'

def test_todo_file_exists():
    assert TODO_FILE != None

def test_load_tasks():
    assert load_tasks() != None

