#!/usr/bin/python3
"""We consume APIs to extract fictitious information."""
import requests
from sys import argv


def api_data():
    """We query the name and tasks of an employee."""
    if len(argv) > 1 and argv[1].isdigit():
        user_ID = int(argv[1])

    else:
        return

    """Build the API URL to get user tasks."""
    api_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_ID}"
    response = requests.get(api_url)

    """Build the API URL to get user information"""
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_ID}"
    users = requests.get(user_url)

    """Check if the user's information request was successful."""
    if users.status_code == 200:
        user = users.json()
        # Get the user's name
        EMPLOYEE_NAME = user["name"]
    else:
        print("Error:username not found.")

    """Check if the task request was successful."""
    if response.status_code == 200:
        todos = response.json()
        # Count the number of completed tasks and total tasks
        NUMBER_OF_DONE_TASKS = sum(1 for todo in todos if todo['completed'])
        TOTAL_NUMBER_OF_TASKS = len(todos)
    else:
        print("Error: Unable to get tasks. Please enter an existing user ID.")

    print(f"Employee {EMPLOYEE_NAME} is done with tasks"
          f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

    # Print titles of completed tasks
    for todo in todos:
        if todo["completed"]:
            print("\t {}".format(todo["title"]))


if __name__ == "__main__":
    api_data()
