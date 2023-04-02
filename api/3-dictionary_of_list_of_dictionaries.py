#!/usr/bin/python3
"""Commenting"""
import json
import requests


def gather_data_json():
    """Comments"""
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    task_list = []
    task_dict = {}
    user_data = 0
    for u in users:
        user_data += 1
        todos = requests.get("https://jsonplaceholder."
                             "typicode.com/todos?userId={}"
                             .format(user_data)).json()
        for t in todos:
            task_list.append({'username': u['username'],
                              'task': t['title'],
                              'completed': t['completed']})
        task_dict[user_data] = task_list
        task_list = []
    with open('todo_all_employees.json'.format(user_data),
              'w+', encoding='UTF8') as f:
        f.write(json.dumps(task_dict))


if __name__ == '__main__':
    gather_data_json()
