import pytest
import json
from todo import read_tasks
from todo import generate_id
from todo import create_task
from todo import write_tasks

TODO_FILE = 'data/todo.json'

def test_todo_file_exists():
    assert TODO_FILE is not None

def test_todo_file_not_empty():
    assert read_tasks(TODO_FILE) is not None

def test_generate_id_empty_list():
    assert generate_id([]) == 1

def test_generate_id_with_tasks():
    tasks = [
        {'id': 1, 'task': 'A', 'completed': False},
        {'id': 3, 'task': 'B', 'completed': True},
        {'id': 5, 'task': 'C', 'completed': False}
    ]
    assert generate_id(tasks) == 6

def test_create_new_task():
    tasks = [
        {'id': 1, 'task': 'A', 'completed': False},
        {'id': 3, 'task': 'B', 'completed': True},
        {'id': 5, 'task': 'C', 'completed': False}
    ]

    updated_tasks = create_task(tasks, 'test')
    assert len(updated_tasks) == 4
    assert updated_tasks[-1]['id'] == 6
    assert updated_tasks[-1]['task'] == 'test'


def test_read_tasks(tmp_path):
    file = tmp_path / 'test.json'
    tasks = [
        {'id': 1, 'task': 'A', 'completed': False},
        {'id': 3, 'task': 'B', 'completed': True},
        {'id': 5, 'task': 'C', 'completed': False}
    ]
    
    with file.open('w') as f:
        json.dump(tasks, f, indent=4)
    content = read_tasks(file)
    assert content == tasks

def test_write_tasks(tmp_path):
    file = tmp_path / 'test.json'

    tasks = [
        {'id': 1, 'task': 'A', 'completed': False},
        {'id': 3, 'task': 'B', 'completed': True},
        {'id': 5, 'task': 'C', 'completed': False}
    ]

    write_tasks(tasks, file)
    with open(file, 'r') as f:
        content = json.load(f)
    
    assert content == tasks
