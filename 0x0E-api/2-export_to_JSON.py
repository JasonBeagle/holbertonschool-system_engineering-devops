#!/usr/bin/python3

"""
This script uses a REST API to obtain information about
an employee's progress on their TODO list based on the employee ID,
and exports the data in JSON format.
"""

import json
import requests
from sys import argv

# Check if this module is being executed as the main program
if __name__ == "__main__":

    # Retrieve the user ID passed in as an argument
    user_id = argv[1]

    # Make a request to TODO list API for tasks associated with given user ID
    todos = requests.get(
        "http://jsonplaceholder.typicode.com/todos?userId={}".format(user_id))

    # Make a request to user API to retrieve info about the given user ID
    user = requests.get(
        "http://jsonplaceholder.typicode.com/users/{}".format(user_id))

    # Initialize a dictionary with user ID as key and a empty list as the value
    out = {user.json().get('id'): []}

    # Open new JSON file with user ID as name and write retrieved data to it
    with open('{}.json'.format(user_id), "w") as output:
        # Iterate through the TODO list data and append to output dictionary
        for tarea in todos.json():
            data = {
                'task': tarea.get('title'),
                'completed': tarea.get('completed'),
                'username': user.json().get('username')
            }
            out.get(user.json().get('id')).append(data)

        # Write the output dictionary to the JSON file
        json.dump(out, output)
