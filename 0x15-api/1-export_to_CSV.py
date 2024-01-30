#!/usr/bin/python3
"""This script exports data in csv format using REST API"""

import csv
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

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([user_id, username, todo.get("completed"),
                            todo.get("title")])
