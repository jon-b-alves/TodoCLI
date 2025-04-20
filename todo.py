import argparse
import json

'''
main.py
todo.json
completed_task.json
'''

#todo add "task"
#todo delete {ID#}
#todo list
#todo clear
#todo help
#todo complete

# read/load -> modify -> write/save

TODO_FILE = 'data/todo.json'

def read_tasks(todo_file) -> list:  
    with open(todo_file, 'r') as file:
        tasks = json.load(file)
  
        try:
            return tasks
        except json.JSONDecodeError:
            return []

def write_tasks(tasks: list, todo_file):
    with open(todo_file, 'w') as file:
        json.dump(tasks, file, indent=4)

def generate_id(tasks: list) -> int:
    if tasks == None:
        return 1
    
    max_id = 0
    for task in tasks:
        if task['id'] > max_id:
            max_id = task['id']
    return max_id + 1
        

def create_task(tasks: list, task_text: str) -> list[dict]:
    task_data = {
        'id': generate_id(tasks),
        'task': task_text,
        'completed': False
    }
    tasks.append(task_data)
    return tasks

def store_task(task_text: str):
    tasks = read_tasks(TODO_FILE)
    updated_tasks = create_task(tasks, task_text)
    write_tasks(updated_tasks, TODO_FILE)
    print('task stored')

def delete_task(task_id: int):
    tasks = read_tasks(TODO_FILE)
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            write_tasks(tasks, TODO_FILE)
            print('task deleted')
            return
    print('no matching id')

def show_tasks():
    tasks = read_tasks(TODO_FILE)
    for task in tasks:
         print(f"({task['id']}) {task['task']}")

def parse_arguments():
    parser = argparse.ArgumentParser(prog='Todo List', description='CLI Todo List')
    subparsers = parser.add_subparsers(dest='command', help='commands')

    #add
    add_task_parser = subparsers.add_parser('add', help='add task')
    add_task_parser.add_argument('task', type=str, help='task itself')

    #delete
    delete_task_parser = subparsers.add_parser('delete', help='delete task')
    delete_task_parser.add_argument('task_id', type=int, help='task id')

    #list
    list_task_parser = subparsers.add_parser('list', help='list tasks')

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()

    if args.command == 'add':
        store_task(args.task)
    if args.command == 'delete':
        delete_task(args.task_id)
    if args.command == 'list':
        show_tasks()
    

