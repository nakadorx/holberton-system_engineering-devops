#!/usr/bin/python3
"""api
"""
import requests
from sys import argv


if __name__ == "__main__":
    todoURL = "https://jsonplaceholder.typicode.com/todos/"
    usersURL = "https://jsonplaceholder.typicode.com/users/"
    tod = requests.get(todoURL, params={"userId": argv[1]})
    userx = requests.get(usersURL, params={"id": argv[1]})
    tasks = tod.json()
    user = userx.json()
    for obj in user:
        name = obj.get("name")
    doneTasks = 0
    for t in tasks:
        if t.get("completed"):
            doneTasks += 1
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          doneTasks,
                                                          len(tasks)))
    for x in tasks:
        if x.get("completed"):
            print("\t {}".format(x.get("title")))
