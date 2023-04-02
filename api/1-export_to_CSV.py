#!/usr/bin/python3
"""Commenting"""
import csv
import requests
from sys import argv


def gather_data_csv():
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
        task_list.append([user_data, par_user['username'], t['completed'],
                         t['title']])
    with open('{}.csv'.format(user_data), 'w+', encoding='UTF8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(task_list)


if __name__ == '__main__':
    gather_data_csv()
