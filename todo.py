import argparse
import json

# todo help
# read/load -> modify -> write/save
TODO_FILE = "data/todo.json"


def read_tasks(todo_file) -> list:
    try:
        with open(todo_file, "r") as file:
            tasks = json.load(file)
            return tasks
    except json.JSONDecodeError:
        return []


def write_tasks(tasks: list, todo_file) -> None:
    with open(todo_file, "w") as file:
        json.dump(tasks, file, indent=4)


def generate_id(tasks: list) -> int:
    if tasks is None:
        return 1

    max_id = 0
    for task in tasks:
        if task["id"] > max_id:
            max_id = task["id"]
    return max_id + 1


def create_task(tasks: list, task_text: str) -> list:
    task_data = {
        "id": generate_id(tasks),
        "task": task_text,
        "completed": False
    }
    tasks.append(task_data)
    return tasks


def store_task(task_text: str, file_path: str) -> list[dict]:
    tasks = read_tasks(file_path)
    updated_tasks = create_task(tasks, task_text)
    write_tasks(updated_tasks, file_path)
    print("Task stored")
    return updated_tasks


def delete_task(task_id: int, file_path: str) -> bool:
    tasks = read_tasks(file_path)
    task = find_task_by_id(tasks, task_id)
    if task:
        tasks.remove(task)
        write_tasks(tasks, file_path)
        print("Task deleted")
        return True
    print("No matching id")
    return False


def show_tasks(file_path: str) -> None:
    tasks = read_tasks(file_path)
    if tasks:
        for task in tasks:
            print(f"({task['id']}) {task['task']}")
    else:
        print("No tasks available")


def clear_tasks(file_path: str) -> bool:
    try:
        tasks = read_tasks(file_path)
        tasks.clear()
        write_tasks(tasks, file_path)
        print("Tasks cleared")
        return True
    except Exception:
        return False


def find_task_by_id(tasks: list[dict], task_id) -> dict | None:
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def complete_task(task_id: int, file_path: str) -> bool:
    tasks = read_tasks(file_path)
    task = find_task_by_id(tasks, task_id)
    if task:
        task["completed"] = True
        write_tasks(tasks, file_path)
        print("Task completed")
        return True
    print("No matching id")
    return False


def uncomplete_task(task_id: int, file_path: str) -> bool:
    tasks = read_tasks(file_path)
    task = find_task_by_id(tasks, task_id)
    if task:
        task["completed"] = False
        write_tasks(tasks, file_path)
        print("Task uncompleted")
        return True
    print("No matching id")
    return False


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="Todo List", description="CLI Todo List"
        )
    subparsers = parser.add_subparsers(dest="command", help="commands")

    # add
    add_task_parser = subparsers.add_parser("add", help="add task")
    add_task_parser.add_argument("task", type=str, help="task itself")

    # delete
    delete_task_parser = subparsers.add_parser(
        "delete", aliases=["del"], help="delete task"
    )
    delete_task_parser.add_argument("task_id", type=int, help="task id")

    # list
    subparsers.add_parser("list", aliases=["ls"], help="list tasks")

    # clear
    subparsers.add_parser("clear", aliases=["cl"], help="clear all tasks")

    # complete
    complete_task_parser = subparsers.add_parser(
        "complete", aliases=["cmp"], help="mark task as complete"
    )
    complete_task_parser.add_argument("task_id", type=int, help="task id")

    # uncomplete
    uncomplete_task_parser = subparsers.add_parser(
        "uncomplete", aliases=["uncmp"], help="mark task as uncomplete"
    )
    uncomplete_task_parser.add_argument("task_id", type=int, help="task id")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    if args.command in ["add"]:
        store_task(args.task, TODO_FILE)
    if args.command in ["delete", "del"]:
        delete_task(args.task_id, TODO_FILE)
    if args.command in ["list", "ls"]:
        show_tasks(TODO_FILE)
    if args.command in ["clear", "cl"]:
        clear_tasks(TODO_FILE)
    if args.command in ["complete", "cmp"]:
        complete_task(args.task_id, TODO_FILE)
    if args.command in ["uncomplete", "uncmp"]:
        uncomplete_task(args.task_id, TODO_FILE)
