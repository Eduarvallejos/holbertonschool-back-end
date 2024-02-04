#!/usr/bin/python3
"""We consume APIs to extract fictitious information."""
from sys import argv
import csv
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
        print("Error:username not found.")

    """Check if the task request was successful."""
    if response.status_code == 200:
        todos = response.json()
        
    else:
        print("Error: Unable to get tasks. Please enter an existing user ID.")

    """CSV file creation"""
    csv_file_name = f"{USER_ID}.csv"
    with open(csv_file_name, mode='w', newline='') as csv_file:
        # Define the field names (column headers) for the CSV
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]

        # Create a CSV writer object
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        # Write task data to the CSV file
        for todo in todos:
            writer.writerow({
                "USER_ID": USER_ID,
                "USERNAME": EMPLOYEE_NAME,
                "TASK_COMPLETED_STATUS": todo["completed"],
                "TASK_TITLE": todo["title"]
            })


if __name__ == "__main__":
    api_data()
