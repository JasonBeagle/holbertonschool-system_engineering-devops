#!/usr/bin/python3
"""
0-gather_data_from_an_API.py
"""
import requests
import sys


def get_employee_data(employee_id):
    """Get the employee data for the given employee ID"""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(url)
    return response.json()


def get_employee_tasks(employee_id):
    """Get the employee's tasks for the given employee ID"""
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)
    response = requests.get(url)
    return response.json()


def main(employee_id):
    """Main function"""
    employee_data = get_employee_data(employee_id)
    tasks = get_employee_tasks(employee_id)

    total_tasks = len(tasks)
    completed_tasks = [task for task in tasks if task['completed']]

    print("Employee {} is done with tasks({}/{})".format(
        employee_data['name'], len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task['title']))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        main(int(sys.argv[1]))
    else:
        print("Usage: {} employee_id".format(sys.argv[0]))
