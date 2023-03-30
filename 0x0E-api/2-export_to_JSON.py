#!/usr/bin/python3

"""Python script that, using this REST API, for a given employee ID"""

import requests
import sys
import json

if __name__ == "__main__":
    if len(sys.argv) > 1:
        """Get the user ID from command line argument"""
        user_id = sys.argv[1]

        """Construct the API URL using the user ID"""
        url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

        """Send a GET request to the API URL"""
        response = requests.get(url)

        """Check if the response is successful"""
        if response.status_code == 200:
            """Get the response data in JSON format"""
            tasks = response.json()

            """Get the name of the user from the API"""
            user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
            user_response = requests.get(user_url)
            user_data = user_response.json()
            user_name = user_data["name"]

            """Calculate the number of completed tasks and total tasks"""
            num_completed_tasks = 0
            total_tasks = len(tasks)
            completed_tasks = []
            for task in tasks:
                if task["completed"]:
                    completed_tasks.append(task)
                    num_completed_tasks += 1

            """Create a dictionary with the required JSON format"""
            json_tasks = {user_id: [{"task": task["title"], "completed": task["completed"], "username": user_name} for task in completed_tasks]}

            """Write the dictionary to a JSON file"""
            with open(f"{user_id}.json", "w") as json_file:
                json.dump(json_tasks, json_file)

            """Print the result"""
            # print(f"Employee {user_name} is done with tasks ({num_completed_tasks}/{total_tasks})")
        else:
            print(f"Error: {response.status_code}")
    else:
        print("Please provide a user ID as a command line argument.")