#!/usr/bin/python3
"""api
"""
import requests
import json
from sys import argv


if __name__ == "__main__":
    todoUrl = "https://jsonplaceholder.typicode.com/todos/"
    userUrl = "https://jsonplaceholder.typicode.com/users/"
    tod = requests.get(todoUrl, params={"userId": argv[1]})
    userx = requests.get(userUrl, params={"id": argv[1]})
    tasks = tod.json()
    user = userx.json()
    for obj in user:
        name = obj.get("name")
    doneTasks = 0
    for obj in tasks:
        if obj.get("completed"):
            doneTasks += 1
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          doneTasks,
                                                          len(tasks)))
    for x in tasks:
        if x.get("completed"):
            print("\t {}".format(x.get("title")))
