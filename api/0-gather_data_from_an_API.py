#!/usr/bin/python3
"""comments"""

import requests

def get_employee_todo_progress(employee_id):
    """Comments"""
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    data = response.json()
    total_tasks = len(data)
    completed_tasks = sum(1 for task in data if task["completed"])
    employee_name = data[0]["name"].split(":")[0]
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for task in data:
        if task["completed"]:
            print(f"\t- {task['title']}")
get_employee_todo_progress(1)
