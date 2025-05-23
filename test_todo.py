import json
import todo

TODO_FILE = "data/todo.json"


def test_todo_file_exists():
    assert TODO_FILE is not None


def test_todo_file_not_empty():
    assert todo.read_tasks(TODO_FILE) is not None


def test_generate_id_empty_list():
    assert todo.generate_id([]) == 1


def test_generate_id_with_tasks():
    tasks = [
        {"id": 1, "task": "A", "completed": False},
        {"id": 3, "task": "B", "completed": True},
        {"id": 5, "task": "C", "completed": False},
    ]
    assert todo.generate_id(tasks) == 6


def test_create_new_task():
    tasks = [
        {"id": 1, "task": "A", "completed": False},
        {"id": 3, "task": "B", "completed": True},
        {"id": 5, "task": "C", "completed": False},
    ]

    updated_tasks = todo.create_task(tasks, "test")
    assert len(updated_tasks) == 4
    assert updated_tasks[-1]["id"] == 6
    assert updated_tasks[-1]["task"] == "test"


def test_read_tasks(tmp_path):
    file = tmp_path / "test.json"
    tasks = [
        {"id": 1, "task": "A", "completed": False},
        {"id": 3, "task": "B", "completed": True},
        {"id": 5, "task": "C", "completed": False},
    ]

    with file.open("w") as f:
        json.dump(tasks, f, indent=4)
    content = todo.read_tasks(file)
    assert content == tasks


def test_write_tasks(tmp_path):
    file = tmp_path / "test.json"
    tasks = [
        {"id": 1, "task": "A", "completed": False},
        {"id": 3, "task": "B", "completed": True},
        {"id": 5, "task": "C", "completed": False},
    ]

    todo.write_tasks(tasks, file)
    with open(file, "r") as f:
        content = json.load(f)

    assert content == tasks


def test_delete_task(tmp_path):
    file = tmp_path / "test.json"
    tasks = [
        {"id": 1, "task": "A", "completed": False},
        {"id": 3, "task": "B", "completed": True},
        {"id": 5, "task": "C", "completed": False},
    ]

    with file.open("w") as f:
        json.dump(tasks, f, indent=4)

    assert todo.delete_task(3, file) is True


def test_store_task(tmp_path):
    file = tmp_path / "test.json"
    tasks = [
        {"id": 1, "task": "A", "completed": False},
        {"id": 3, "task": "B", "completed": True},
        {"id": 5, "task": "C", "completed": False},
    ]
    with file.open("w") as f:
        json.dump(tasks, f, indent=4)

    updated_tasks = todo.store_task("D", file)
    assert len(updated_tasks) == 4
    assert updated_tasks[3]["task"] == "D"


def test_clear_tasks(tmp_path):
    file = tmp_path / "test.json"
    tasks = [
        {"id": 1, "task": "A", "completed": False},
        {"id": 3, "task": "B", "completed": True},
        {"id": 5, "task": "C", "completed": False},
    ]
    with file.open("w") as f:
        json.dump(tasks, f, indent=4)

    boolean = todo.clear_tasks(file)

    with open(file, "r") as f:
        tasks = json.load(f)

    assert boolean is True
    assert tasks == []


def test_complete_task(tmp_path):
    file = tmp_path / "test.json"
    tasks = [
        {"id": 1, "task": "A", "completed": False},
        {"id": 3, "task": "B", "completed": True},
        {"id": 5, "task": "C", "completed": False},
    ]
    with file.open("w") as f:
        json.dump(tasks, f, indent=4)

    boolean = todo.complete_task(5, file)
    assert boolean is True


def test_uncomplete_task(tmp_path):
    file = tmp_path / "test.json"
    tasks = [
        {"id": 1, "task": "A", "completed": False},
        {"id": 3, "task": "B", "completed": True},
        {"id": 5, "task": "C", "completed": False},
    ]
    with file.open("w") as f:
        json.dump(tasks, f, indent=4)

    boolean = todo.uncomplete_task(3, file)
    assert boolean is True
