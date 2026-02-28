#!/usr/bin/python3
"""
Export all employees' TODO lists to a single JSON file
in a dictionary of list of dictionaries format.
"""

import json
import requests
import sys


def fetch_users():
    """Fetch all employees from the API."""
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to fetch users")
        sys.exit(1)
    return response.json()


def fetch_todos(user_id):
    """Fetch TODO list for a specific employee from the API."""
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to fetch TODOs for user {}".format(user_id))
        sys.exit(1)
    return response.json()


def export_all_todos():
    """Export all employees' TODOs to todo_all_employees.json."""
    users = fetch_users()
    all_data = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        todos = fetch_todos(user_id)

        # Build the list of dictionaries for this user
        all_data[str(user_id)] = [
            {"username": username,
             "task": task.get("title"),
             "completed": task.get("completed")}
            for task in todos
        ]

    # Write to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_data, json_file, indent=4)


if __name__ == "__main__":
    export_all_todos()
	
