#!/usr/bin/python3
"""Queries the Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
        for a given subreddit
    If an invalid subreddit is given, the function should return 0
    """
    # API endpoint for getting subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Set a custom User-Agent to avoid too many requests errors
    headers = {'User-Agent': 'My User Agent 1.0'}

    # Send a Get request
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Chek if the request was successful
    if response.status_code == 200:
        data = response.json().get('data', {})
        count = data.get('subscribers', 0)
        return count
    return 0
