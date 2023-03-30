#!/usr/bin/python3
import csv
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ./2-export_to_CSV.py employee_id")
        sys.exit(1)

    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    try:
        user_data = user_response.json()
        todos_data = todos_response.json()
    except ValueError:
        print("Error: Not a valid JSON")

    employee_name = user_data.get("name")
    filename = "{}.csv".format(employee_id)

    with open(filename, mode='w') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for task in todos_data:
            task_completed = task.get("completed")
            task_title = task
