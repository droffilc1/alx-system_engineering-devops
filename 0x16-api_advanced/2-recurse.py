#!/usr/bin/python3
"""Queries the Reddit API and returns a list containing the titles of all
hot articles for a given subreddit.

If no results are found for a given subreddit, function should return None
"""

import requests

after = ""


def recurse(subreddit, hot_list=[]):
    """Recursively queries the Reddit API"""
    global after
    # API endpoint for getting subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    # Set a custom User-Agent to avoid too many requests errors
    headers = {'User-Agent': 'My User Agent 1.0'}

    params = {'after': after}

    response = requests.get(url, params=params, headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        after_data = response.json().get('data').get('after')
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        titles = response.json().get('data').get('children')
        for t in titles:
            hot_list.append(t.get('data').get('title'))
        return hot_list
    else:
        return None
