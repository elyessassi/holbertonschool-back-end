#!/usr/bin/python3
"""script that exports user information to CSV"""
import csv
import requests
import sys


def todo():
    """module that exports user information to CSV"""

    id_value = int(sys.argv[1])
    responsetodo = requests.get("https://jsonplaceholder.typicode.com/todos")
    responseusers = requests.get("https://jsonplaceholder.typicode.com/users")

    for i in responseusers.json():
        if id_value == i.get("id"):
            username = i.get("name")
            break

    with open(f"{id_value}.csv", "w") as fd:
        writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
        for todo_item in responsetodo.json():
            if id_value == todo_item.get("userId"):
                writer.writerow([id_value,
                                 username,
                                 todo_item.get("completed"),
                                 todo_item.get("title")])


if __name__ == "__main__":
    todo()
