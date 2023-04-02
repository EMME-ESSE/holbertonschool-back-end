#!/usr/bin/python3
"""Commenting"""
import json
import requests
from sys import argv


def gather_data_json():
    """Comments"""
    user_data = int(argv[1])
    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(user_data))
    par_user = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(user_data))
    todos_json = todos.json()
    task_list = []
    for t in todos_json:
        task_list.append({'task': t['title'],
                          'completed': t['completed'],
                          'username': par_user['username']})
    task_dict = {}
    task_dict[user_data] = task_list
    with open('{}.json'.format(user_data), 'w+', encoding='UTF8') as f:
        f.write(json.dumps(task_dict))


if __name__ == '__main__':
    gather_data_json()
