#!/usr/bin/python3
"""We consume APIs to extract fictitious information."""
from sys import argv
import json
import requests


def api_data():
    """We query the name and tasks of an employee."""

    # Dictionary to store tasks for all users
    employee_todos = {}

    for USERID in range(1, 11):
        """Build the API URL to get user tasks."""
        api_url = f"https://jsonplaceholder.typicode.com/todos?userId={USERID}"
        response = requests.get(api_url)

        """Build the API URL to get user information"""
        user_url = f"https://jsonplaceholder.typicode.com/users/{USERID}"
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
            print("Error: Please enter an existing user ID.")
            return

        """Collect information from all user tasks."""
        user_task = []

        for todo in todos:
            task_info = {
                "username": EMPLOYEE_NAME,
                "task": todo["title"],
                "completed": todo["completed"]
                }
            user_task.append(task_info)

        employee_todos[str(USERID)] = user_task

        """Export data in the JSON format."""
        file_json = "todo_all_employees.json"
        with open(file_json, "w") as archivo:
            json.dump(employee_todos, archivo)


if __name__ == "__main__":
    api_data()
