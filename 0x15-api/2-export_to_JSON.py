#!/usr/bin/python3
"""This script exports data in json format using REST API"""

import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user_id = sys.argv[1]

    response = requests.get(url + "users/{}".format(user_id))

    user = response.json()

    username = user.get("username")

    args = {"userId": user_id}

    todo_list = requests.get(url + "todos", params=args)

    todos = todo_list.json()

    data_to_export = {user_id: []}

    for todo in todos:
        task_info = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
        }
        data_to_export[user_id].append(task_info)

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
