#!/usr/bin/python3
"""
This script Contains the number_of_subscribers function.
"""
import requests


def number_of_subscribers(subreddit):
    """
    This function queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit.
    """
    headers = {'User-Agent': 'zeke/1.0.0'}
    URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(URL, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return (response.json()['data']['subscribers'])
    else:
        return (0)
