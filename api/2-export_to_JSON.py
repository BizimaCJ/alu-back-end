#!/usr/bin/python3
"""
Export employee TODO list to JSON file.
"""

import json
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


def export_to_json(user_id):
    """Export all tasks of an employee to a JSON file."""
    employee = fetch_employee(user_id)
    todos = fetch_todos(user_id)

    username = employee.get("username")

    # Build JSON structure
    data = {
        str(user_id): [
            {"task": task.get("title"),
             "completed": task.get("completed"),
             "username": username} for task in todos
        ]
    }

    # Write JSON to file
    filename = "{}.json".format(user_id)
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: EMPLOYEE_ID must be an integer")
        sys.exit(1)

    export_to_json(employee_id)

