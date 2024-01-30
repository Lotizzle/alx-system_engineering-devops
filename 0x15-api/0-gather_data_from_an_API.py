#!/usr/bin/python3
"""This script uses a REST API to get the information about a user's TODO list progress"""

import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]

    response = requests.get(url + "users/{}".format(employee_id))

    user = response.json()

    args = {"userId": employee_id}

    todo_list = requests.get(url + "todos", params=args)

    todos = todo_list.json()

    completed = []

    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{}))".format(user.get("name"),
                                                          len(completed), len(todos)))

    for complete in completed:
        print("\t {}".format(complete))
