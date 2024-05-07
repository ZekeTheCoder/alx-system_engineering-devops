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

    try:
        response = requests.get(URL, headers=header, allow_redirects=False)
        response.raise_for_status()
        number_of_subscribers = response.json().get("data", {}).get("subscribers", 0)
        return (number_of_subscribers)
    
    except requests.exceptions.RequestException:
        return 0

    except (KeyError, ValueError):
        return 0
