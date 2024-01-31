#!/usr/bin/python3
"""This script exports all users data in the JSON format"""

import json
import requests


def fetch_user_date():
    """Fetches user details and TO-DO lists of all employees"""
    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users").json()

    export_data = {}

    for user in users:
        user_id  = user["id"]

        todo_response = requests.get(url + f"todos?userId={user_id}")

        todos = todo_response.json()

        export_data[user_id] = []

        for todo in todos:
            task_info = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            }
            export_data[user_id].append(task_info)

    return export_data

if __name__ == "__main__":
    export_data = fetch_user_date()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(export_data, jsonfile, indent=4)
