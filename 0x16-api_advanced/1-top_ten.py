#!/usr/bin/python3
"""
This script  queries the Reddit API and
prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ This function prints the titles of the first 10 hot posts listed """
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    h = {'User-Agent': 'ZekeTheCoder/1.0'}
    p = {'limit': 10}
    response = requests.get(URL, headers=h, params=p, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title']

            print(title)
    else:
        print(None)
