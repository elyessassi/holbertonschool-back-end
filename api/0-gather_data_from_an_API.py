#!/usr/bin/python3
import requests
import sys

"""fonction that shows user name and tasks done"""


def todo():
    """fonction that shows user name and tasks done"""
    id_value = int(sys.argv[1])
    responsetodo = requests.get("https://jsonplaceholder.typicode.com/todos")
    responseusers = requests.get("https://jsonplaceholder.typicode.com/users")

    for i in responseusers.json():
        if id_value == i.get("id"):
            username = i.get("name")

    tasks_num = 0
    tasks_done = 0
    for i in responsetodo.json():
        if id_value == i.get("userId"):
            tasks_num = tasks_num + 1
        if id_value == i.get("userId") and i.get("completed") is True:
            tasks_done = tasks_done + 1

    print(f"Employee {username} is done with tasks({tasks_done}/{tasks_num}):")
    for i in responsetodo.json():
        if id_value == i.get("userId") and i.get("completed") is True:
            print(f"	 {i.get('title')}")


if __name__ == "__main__":
    todo()
