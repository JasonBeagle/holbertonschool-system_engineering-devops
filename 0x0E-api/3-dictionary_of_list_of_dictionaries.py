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
    # Set verify to False to ignore SSL certificate verification
    users = requests.get('https://jsonplaceholder.typicode.com/users',
                         verify=False).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos',
                        verify=False).json()

    # Initialize dictionaries to store user and task data
    user_dict = {}
    usernamedict = {}

    # Iterate through the retrieved user data and create a key-value pair
    # for each user ID
    # in the user dictionary, and store the username for each user ID
    # in the usernamedict
    for user in users:
        ID = user.get("id")
        user_dict[ID] = []
        usernamedict[ID] = user.get('username')

    # Iterate through the retrieved task data
    # and add task data to the user dictionary
    for task in todo:
        task_dict = {}
        ID = task.get("userId")
        task_dict['username'] = usernamedict.get(ID)
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        user_dict.get(ID).append(task_dict)

    # Write the user dictionary to a JSON file
    with open("todo_all_employees.json", 'w') as jsfile:
        json.dump(user_dict, jsfile)
