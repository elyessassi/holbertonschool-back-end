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
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(fd, fieldnames=fieldnames)
        for i in responsetodo.json():
            if id_value == i.get("userId"):
                writer.writerow({'USER_ID': id_value, "USERNAME": username,
                                "TASK_COMPLETED_STATUS": i.get("completed"),
                                 "TASK_TITLE": i.get("title")})


if __name__ == "__main__":
    todo()
