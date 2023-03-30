#!/usr/bin/python3
"""comments"""

import requests
import sys

if __name__ == "__main__":
    """comment"""
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    response = requests.get("https://jsonplaceholder.typicode.com/todos", params={"userId": employee_id})
    response.raise_for_status()
    todos = response.json()
    num_completed = sum(1 for todo in todos if todo["completed"])
    total = len(todos)
    employee_name = todos[0]["name"]

    print("Employee {} is done with tasks({}/{}):".format(employee_name, num_completed, total))

    for todo in todos:
        if todo["completed"]:
            print("\t {}".format(todo["title"]))
