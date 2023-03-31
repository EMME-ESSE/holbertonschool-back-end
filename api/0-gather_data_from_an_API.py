#!/usr/bin/python3
"""comments"""
import requests

if __name__ == '__main__':
    """Commented"""
    def get_employee_todo_progress(employee_id):
        rs1 = "https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        rs2 = "https://jsonplaceholder.typicode.com/users/{employee_id}"
        response = requests.get(rs1.format())
        data = response.json(rs2)
        total = len(data)
        completed = sum(1 for task in data if task["completed"])
        response = requests.get(f)
        name = response.json()["name"]
        print(f"Employee {name} is done with tasks ({completed}/{total}):")
        for task in data:
            if task["completed"]:
                print(f"\t- {task['title']}")
    get_employee_todo_progress(1)

