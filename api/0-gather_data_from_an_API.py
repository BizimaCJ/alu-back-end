#!/usr/bin/python3
"""
Gather employee TODO progress from API.
"""

import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user = user_response.json()
    todos = todos_response.json()

    employee_name = user.get("name")

    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed") is True]
    done_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done_tasks, total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))

