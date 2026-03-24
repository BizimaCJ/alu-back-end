#!/usr/bin/python3
"""
Accesses a REST API for a given employee ID and returns
information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Define API base URL
        url = "https://jsonplaceholder.typicode.com/"
        user_id = sys.argv[1]

        # Fetch user data
        user_response = requests.get("{}users/{}".format(url, user_id))
        user_data = user_response.json()
        employee_name = user_data.get("name")

        # Fetch todo data
        todos_response = requests.get("{}todos?userId={}".format(url, user_id))
        todos = todos_response.json()

        # Filter completed tasks
        done_tasks = []
        for task in todos:
            if task.get("completed") is True:
                done_tasks.append(task.get("title"))

        total_tasks = len(todos)
        done_count = len(done_tasks)

        # Exact formatting for the summary line
        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, done_count, total_tasks))

        # Exact formatting for task titles (1 tab + 1 space)
        for title in done_tasks:
            print("\t {}".format(title))

