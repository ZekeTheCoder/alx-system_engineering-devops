#!/usr/bin/python3
"""
This script queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    This function returns the number of subscribers for a given subreddit.
    """
    
    URL = f'https://www.reddit.com/r/{subreddit}/about.json'
    header = {'User-Agent': 'ZekeTheCoder'}
    response = requests.get(URL, headers=header, allow_redirects=False)
    if response.status_code == 200:
        return (response.json()['data']['subscribers'])
    else:
        return (0)
