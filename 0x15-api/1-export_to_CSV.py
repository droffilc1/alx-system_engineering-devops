#!/usr/bin/python3
"""Export data in the CSV format"""

from sys import argv
import requests
import csv


if __name__ == '__main__':
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = requests.get(url)

    username = response.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos' \
        .format(user_id)
    response = requests.get(url)
    tasks = response.json()
    with open('{}.csv'.format(user_id), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user_id, username, task.get('completed'),
                            task.get('title')])
