#!/usr/bin/python3
"""
Export employee TODO list to CSV file
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]

    # Fetch employee data
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)

    user_resp = requests.get(user_url)
    todos_resp = requests.get(todos_url)

    if user_resp.status_code != 200 or todos_resp.status_code != 200:
        print("Error fetching data")
        sys.exit(1)

    user_data = user_resp.json()
    todos_data = todos_resp.json()

    username = user_data.get("username")

    # Prepare CSV file
    csv_filename = "{}.csv".format(user_id)
    with open(csv_filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])

