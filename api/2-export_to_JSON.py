#!/usr/bin/python3
"""We consume APIs to extract fictitious information."""
from sys import argv
import json
import requests


def api_data():
    """We query the name and tasks of an employee."""
    if len(argv) > 1 and argv[1].isdigit():
        USER_ID = int(argv[1])

    else:
        return

    """Build the API URL to get user tasks."""
    api_url = f"https://jsonplaceholder.typicode.com/todos?userId={USER_ID}"
    response = requests.get(api_url)

    """Build the API URL to get user information"""
    user_url = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
    users = requests.get(user_url)
    """Check if the user's information request was successful."""
    if users.status_code == 200:
        user = users.json()
        # Get the user's name
        EMPLOYEE_NAME = user["username"]
    else:
        print("Please enter an existing user ID")
        return

    """Check if the task request was successful."""
    if response.status_code == 200:
        todos = response.json()
    else:
        print("Error: Unable to get tasks. Please enter an existing user ID.")
        return

    """Collect information from all user tasks."""
    user_task = []
    for todo in todos:

        task_info = {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": EMPLOYEE_NAME
            }
        user_task.append(task_info)

    """Export data in the JSON format."""
    file_json = f"{USER_ID}.json"
    with open(file_json, "w") as archivo:
        json.dump({f"{USER_ID}": user_task}, archivo)


if __name__ == "__main__":
    api_data()
