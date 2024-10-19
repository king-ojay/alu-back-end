#!/usr/bin/python3
"""
This Python script fetches and displays TODO list progress for a given employee ID.
"""

import requests
import sys

if __name__ == "__main__":
    # Ensure the user provides an integer ID
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Fetch employee data from API
    url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(url_user).json()

    # Fetch todo list data from API
    url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(url_todos).json()

    # Get employee name
    employee_name = user_response.get("name")

    # Get completed tasks and total tasks
    completed_tasks = [todo for todo in todos_response if todo.get("completed")]
    total_tasks = len(todos_response)

    # Print employee's TODO list progress
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
