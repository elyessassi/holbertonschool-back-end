#!/usr/bin/python3
"""script that exports user information to JSON"""
import json
import requests
import sys


def todo():
    """module that exports user information to JSON"""
    id_value = int(sys.argv[1])
    responsetodo = requests.get("https://jsonplaceholder.typicode.com/todos")
    responseusers = requests.get("https://jsonplaceholder.typicode.com/users")

    for i in responseusers.json():
        if id_value == i.get("id"):
            username = i.get("username")
            break

    data = {id_value: []}

    for i in responsetodo.json():
        if id_value == i.get("userId"):
            data[id_value].append({"task": i.get("title"), "completed":
                                  i.get("completed"), "username": username})

    with open(f"{id_value}.json", "w") as fd:
        json.dump(data, fd)


if __name__ == "__main__":
    todo()
