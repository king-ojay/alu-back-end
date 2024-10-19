#!/usr/bin/python3
import requests
import sys
"""
    python script that returns TODO list progress for a given employee ID
"""

def get_employee_todo_progress(employee_id):
    # API base URL
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get employee information
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data['name']
    
    # Get TODO list for the employee
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todos_data = todos_response.json()
    
    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])
    
    # Print progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    
    # Print completed tasks
    for todo in todos_data:
        if todo['completed']:
            print(f"\t {todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
    except requests.RequestException as e:
        print(f"Error: Unable to fetch data from the API. {e}")
        sys.exit(1)