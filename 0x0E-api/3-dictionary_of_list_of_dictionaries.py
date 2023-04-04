#!/usr/bin/python3

"""
This script extends the previous version to export data in
JSON format for all employees' progress on their TODO lists,
based on data from the JSONPlaceholder API.
"""

import json
import requests
from sys import argv

# Check if this module is being executed as the main program
if __name__ == "__main__":

    # Make requests to the user and TODO list APIs to retrieve data
    users = requests.get('{}/users'.format(
        'https://jsonplaceholder.typicode.com')).json()
    tasks = requests.get(
        '{}/todos'.format('https://jsonplaceholder.typicode.com')).json()

    # Initialize an empty dictionary to store the output data
    out = dict()

    # Iterate through users, create a k/v pair in the dictionary for user ID
    for user in users:
        out.update({user.get('id'): []})

        # Iterate through tasks and add task to dictionary matching user IDs
        for tarea in tasks:
            if tarea.get('userId') == user.get('id'):
                data = {
                        'task': tarea.get('title'),
                        'completed': tarea.get('completed'),
                        'username': user.get('username')
                }
                out.get(user.get('id')).append(data)

    # Write the output dictionary to a JSON file
    with open('todo_all_employees.json', "w") as file:
        json.dump(out, file)
