#!/usr/bin/python3
"""Commented"""
import requests
from sys import argv


def gather_data():
    """Commenting"""
    user_data = int(argv[1])
    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(user_data))
    par_user = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(user_data))
    todos_json = todos.json()
    completed_tasks, tasks, task_list = 0, 0, []
    for t in todos_json:
        if t['completed'] is True:
            completed_tasks += 1
            task_list.append("\t {}".format(t['title']))
        tasks += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(par_user['name'], completed_tasks, tasks))
    print(*task_list, sep='\n')


if __name__ == '__main__':
    gather_data()
