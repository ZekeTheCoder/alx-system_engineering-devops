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
    if subreddit is None or type(subreddit) is not str:
        return 0

    URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'ZekeTheCoder'}
    response = requests.get(URL, headers=header, allow_redirects=False).json()
    number_of_subscribers = response.get("data", {}).get("subscribers", 0)
    return (number_of_subscribers)
