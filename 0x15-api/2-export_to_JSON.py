#!/usr/bin/python3
"""Export data in the json format"""

from sys import argv
import json
import requests


if __name__ == '__main__':
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = requests.get(url)

    username = response.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos' \
        .format(user_id)
    response = requests.get(url)
    tasks = response.json()

    data = {
        user_id: [
            {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            }
            for task in tasks
        ]
    }

    with open('{}.json'.format(user_id), 'w') as file:
        json.dump(data, file)
