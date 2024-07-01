#!/usr/bin/python3
"""script that exports all users information to JSON"""
import json
import requests


def todo():
    """module that exports all users information to JSON"""
    responsetodo = requests.get("https://jsonplaceholder.typicode.com/todos")
    responseusers = requests.get("https://jsonplaceholder.typicode.com/users")

    data = {}
    for user in responseusers.json():
        part_of_data = {user.get("id"): []}
        for i in responsetodo.json():
            if i.get("userId") == user.get("id"):
                username = user.get("username")
                part_of_data[i.get("userId")].append({"username": username,
                                                     "task": i.get("title"),
                                                      "completed":
                                                      i.get("completed")})
        data.update(part_of_data)

    with open("todo_all_employees.json", "w") as fd:
        json.dump(data, fd)


if __name__ == "__main__":
    todo()
