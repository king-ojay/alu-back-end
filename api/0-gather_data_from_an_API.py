#!/usr/bin/python3
"""
Fetch and display employee TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    
    # Fetch employee data
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    employee_response = requests.get(employee_url).json()
    todos_response = requests.get(todos_url).json()

    employee_name = employee_response.get('name')
    total_tasks = len(todos_response)
    done_tasks = len([task for task in todos_response if task.get('completed')])

    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    
    for task in todos_response:
        if task.get('completed'):
            print("\t", task.get('title'))
