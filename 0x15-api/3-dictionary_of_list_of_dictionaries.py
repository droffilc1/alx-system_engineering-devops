#!/usr/bin/python3
"""Export data in the json format"""

import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(url)

    users = response.json()

    data = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
                .format(user_id)
        response = requests.get(url)
        tasks = response.json()

        data[user_id] = [
                {
                    "task": task.get('title'),
                    "completed":task.get('completed'),
                    "username": username
                }
                for task in tasks
        ]

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)
