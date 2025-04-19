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

def generate_id():
    return

def add_task(task_text: str):
    task_data = {
        'id': 123,
        'task': task_text,
        'completed': False
    }

def delete_task(task_id: int):
    return

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
        print(args.task) #add_task(args.task)
    if args.command == 'delete':
        print(args.task_id) #delete_task(args.task_id)

