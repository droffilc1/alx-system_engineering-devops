#!/usr/bin/python3
"""Queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, found_list=[], after=None):
    """Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """
    headers = {'User-agent': 'test45'}
    response = requests.get(
        f'http://www.reddit.com/r/{subreddit}/hot.json?after={after}',
        headers=headers
    )
    if after is None:
        word_list = [word.lower() for word in word_list]

    if response.status_code == 200:
        response = response.json()['data']
        after_data = response['after']
        response = response['children']
        for post in response:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_list.append(word)
        if after_data is not None:
            count_words(subreddit, word_list, found_list, after_data)
        else:
            result = {}
            for word in found_list:
                if word.lower() in result:
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print(f'{key}: {value}')
    else:
        return
