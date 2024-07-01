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

    with open(f"{id_value}.csv", "w", newline="") as fd:
        writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
        for i in responsetodo.json():
            if id_value == i.get("userId"):
                writer.writerow([id_value, username,
                                i.get("completed"), i.get("title")])


if __name__ == "__main__":
    todo()
