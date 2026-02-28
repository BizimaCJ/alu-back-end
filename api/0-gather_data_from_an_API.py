#!/usr/bin/python3
"""
Gather data from an API for a given employee ID
and display TODO list progress.
"""

import requests
import sys


def fetch_employee(user_id):
    """Fetch employee data from the API."""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to fetch employee data")
        sys.exit(1)
    return response.json()


def fetch_todos(user_id):
    """Fetch TODO list for the employee from the API."""
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to fetch TODO list")
        sys.exit(1)
    return response.json()


def display_progress(user_id):
    """Display TODO list progress in the required format."""
    employee = fetch_employee(user_id)
    todos = fetch_todos(user_id)

    employee_name = employee.get("name")
    total_tasks = len(todos)
    done_tasks = sum(1 for task in todos if task.get("completed"))

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done_tasks, total_tasks))

    for task in todos:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: EMPLOYEE_ID must be an integer")
        sys.exit(1)

    display_progress(employee_id)

