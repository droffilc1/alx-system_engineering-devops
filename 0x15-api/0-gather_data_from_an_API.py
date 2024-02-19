#!/usr/bin/python3
"""Using this REST API, for a given employee ID, returns information
about his/her TODO list progress.
"""

from sys import argv
import requests


if __name__ == '__main__':
    # URL of the REST API
    url = 'https://jsonplaceholder.typicode.com/'

    # Get user info
    user = requests.get(url + "users/{}".format(argv[1])).json()

    # Retrive the TODO list
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()

    # Filter completed TODO list and store titles in a list
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Display employee's name, number of done tasks and total number of tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Display the title of completed tasks
    [print("\t {}".format(c)) for c in completed]
