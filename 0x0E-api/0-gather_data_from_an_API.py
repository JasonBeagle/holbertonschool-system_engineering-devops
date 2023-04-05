#!/usr/bin/python3
"""Using a REST API, for a given employee ID, returns information about
his/her TODO list progress.
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    employee_id = argv[1]
    tasks_done, total_tasks = 0, 0
    base_url = "https://jsonplaceholder.typicode.com"

    # creating response objects for employee
    employee_response = requests.get("{}/users/{}"
                                     .format(base_url, employee_id))
    # creating dictionary objects for response objects
    employee_info = employee_response.json()

    # creating response objects for employee & their todo list
    todo_response = requests.get("{}/users/{}/todos"
                                 .format(base_url, employee_id))
    # creating dictionary objects for response objects
    todo_list = todo_response.json()

    # name variable placeholder
    name = employee_info['name']

    # task incrementation
    for task in todo_list:
        total_tasks += 1
        if task['completed']:
            tasks_done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, tasks_done, total_tasks))

    for task in todo_list:
        if task['completed']:
            print("\t {}".format(task['title']))
