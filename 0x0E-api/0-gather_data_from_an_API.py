#!/usr/bin/python3

"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

USERS_API = "https://jsonplaceholder.typicode.com/users/"
TODOS_API = "https://jsonplaceholder.typicode.com/todos"


def get_employee_todos(employee_id):
    """
    Given an employee ID, returns information about their TODO list progress.
    """

    # Fetch the employee's details from the API.
    employee_api_url = USERS_API + str(employee_id)
    employee_response = requests.get(employee_api_url)
    employee = employee_response.json()

    # Fetch the employee's TODO list from the API.
    todos_api_url = TODOS_API + "?userId=" + str(employee_id)
    todos_response = requests.get(todos_api_url)
    todos = todos_response.json()

    # Count the number of completed and total tasks.
    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos)

    # Construct the output string.
    output = "Employee {} is done with tasks({}/{}):\n".format(
        employee['name'], num_completed_tasks, total_tasks)

    # Add the title of completed tasks to the output string.
    for task in completed_tasks[:-1]:
        output += "\t" + task['title'] + '\n'

    output += "\t" + completed_tasks[-1]['title']

    return output


def main():
    # Check if the employee ID was provided as a command-line argument.
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    # Parse the employee ID.
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Invalid employee ID.")
        sys.exit(1)

    # Get the employee's TODO list progress.
    try:
        output = get_employee_todos(employee_id)
    except requests.exceptions.RequestException as e:
        print("Error: Could not fetch employee data from API.")
        sys.exit(1)

    # Print the output.
    print(output)


if __name__ == "__main__":
    main()
