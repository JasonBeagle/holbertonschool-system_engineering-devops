#!/usr/bin/python3

"""Python script that, using this REST API, for a given employee ID"""

import requests
import sys
import csv

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
            data = response.json()

            """Get the name of the user from the API"""
            user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
            user_response = requests.get(user_url)
            user_data = user_response.json()
            user_name = user_data["name"]

            """Create a CSV file with the user ID as the name"""
            filename = f"{user_id}.csv"
            with open(filename, mode="w", newline="") as csvfile:
                """Create a CSV writer"""
                csvwriter = csv.writer(csvfile, delimiter=",", quotechar='"',
                                       quoting=csv.QUOTE_MINIMAL)
                """Write the header row"""
                csvwriter.writerow(["USER_ID", "USERNAME",
                                    "TASK_COMPLETED_STATUS", "TASK_TITLE"])
                """Write each row of task data"""
                for task in data:
                    csvwriter.writerow([task["userId"], user_name,
                                        task["completed"], task["title"]])

            """Print a success message"""
            print(f"Data exported to {filename}.")
        else:
            print(f"Error: {response.status_code}")
    else:
        print("Please provide a user ID as a command line argument.")
