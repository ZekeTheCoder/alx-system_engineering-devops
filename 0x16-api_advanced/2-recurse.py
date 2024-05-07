#!/usr/bin/python3
"""
This script Contains the recurse function
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.
    """
    global after

    headers = {'User-Agent': 'zeke/1.0.0'}
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    response = requests.get(URL, params=params, headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        after_data = response.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)

        titles = response.json().get("data").get("children")

        for title in titles:
            hot_list.append(title.get("data").get("title"))
        return (hot_list)
    else:
        return (None)
