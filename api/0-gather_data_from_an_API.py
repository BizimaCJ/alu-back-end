#!/usr/bin/python3
"""
This module provides a script to fetch and display an employee's TODO list
progress from a REST API based on a given employee ID.
"""
import requests
import sys


def gather_data():
    """
    Fetches user and todo data from JSONPlaceholder API and prints
    the progress in a specific format.
    """
    if len(sys.argv) < 2:
        return

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        return

    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user_res = requests.get("{}users/{}".format(url, user_id))
    user_data = user_res.json()
    # Use .get() as required to avoid exceptions
    employee_name = user_data.get("name")

    # Fetch TODO list
    todos_res = requests.get("{}todos?userId={}".format(url, user_id))
    todos_data = todos_res.json()

    # Calculate tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # First line output
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))

    # Task titles with 1 tab and 1 space
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    gather_data()

