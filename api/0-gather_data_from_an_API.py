#!/usr/bin/python3
"""comments"""

import requests
import sys

if __name__ == '__main__':
    try:
        employee_id = int(sys.argv[1])
    except Exception:
        print("Please insert an integer as a parameter")
        exit()

    total_tasks = 0
    done_tasks = 0
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        employee_id)
    url = 'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(
        employee_id)

    user_response = requests.get(user_url).json().get('name')
    response = requests.get(url).json()

    for task in response:
        total_tasks += 1
        if task['completed'] is True:
            done_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(user_response,
          done_tasks, total_tasks))

    for task in response:
        if task['completed'] is True:
            print("\t {}".format(task['title']))
