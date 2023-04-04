#!/usr/bin/python3
"""Using a REST API, for a given employee ID, returns information about
his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":
    """Your code should not be executed when imported"""

    # Get the employee ID from the command line argument
    user_id = argv[1]

    # Send a GET request to the API to retrieve the todos and user information
    todos = requests.get(
        "http://jsonplaceholder.typicode.com/todos?userId={}".format(user_id))
    user = requests.get(
        "http://jsonplaceholder.typicode.com/users/{}".format(user_id))

    # Check if the user information was successfully retrieved
    if len(user.json()):
        # Initialize counters for total tasks and completed tasks
        total = 0
        completed = 0
        # Create a list to store completed tasks
        tasks_list = []
        # Iterate through each task in the todos
        for tarea in todos.json():
            total += 1  # Increment total tasks
            # Check if the task is completed
            if tarea.get("completed") is True:
                completed += 1  # Increment completed tasks counter
                # Add task title to completed tasks list
                tasks_list.append(tarea.get("title"))

        # Print employee's name and task completion information
        print("Employee {} is done with tasks({}/{}):".format(
            user.json().get("name"), completed, total))
        # Iterate through each completed task and print it
        for task in tasks_list:
            print("\t {}".format(task))
