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
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    # Send a Get request
    response = requests.get(url, headers=headers,
                            allow_redirects=False).json()
    subscribers = response.get('data', {}).get('subscribers')

    if not subscribers:
        return 0
    return subscribers
