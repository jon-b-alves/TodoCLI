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

def load_tasks() -> list:  
    with open(TODO_FILE, 'r') as file:
        tasks = json.load(file)
        return tasks

def save_tasks(tasks: list) -> list:
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def generate_id(tasks: list) -> int:
    if tasks == None:
        return 1
    
    max_id = 0
    for task in tasks:
        if task['id'] > max_id:
            max_id = task['id']
    return max_id + 1
        

def add_task(task_text: str):
    tasks = load_tasks()
    task_data = {
        'id': generate_id(tasks),
        'task': task_text,
        'completed': False
    }
    
    tasks.append(task_data)
    save_tasks(tasks)

def delete_task(task_id: int):
    tasks = load_tasks()
    #search for task with equal id
    #

def parse_arguments():
    parser = argparse.ArgumentParser(prog='Todo List', description='CLI Todo List')
    subparsers = parser.add_subparsers(dest='command', help='commands')

    #add
    add_task_parser = subparsers.add_parser('add', help='add task')
    add_task_parser.add_argument('task', type=str, help='task itself')

    #delete
    delete_task_parser = subparsers.add_parser('delete', help='delete task')
    delete_task_parser.add_argument('task_id', type=int, help='task id')

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()

    if args.command == 'add':
        add_task(args.task)
    if args.command == 'delete':
        print(args.task_id) #delete_task(args.task_id)

