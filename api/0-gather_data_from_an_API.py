#!/usr/bin/python3
"""Module that retrieves TODO list progress for a given employee ID."""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Get and print TODO list progress for a given employee ID."""
    base_url = "https://jsonplaceholder.typicode.com"
    
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data['name']
    
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todos_data = todos_response.json()
    
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])
    
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    
    for todo in todos_data:
        if todo['completed']:
            print(f"\t {todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        em