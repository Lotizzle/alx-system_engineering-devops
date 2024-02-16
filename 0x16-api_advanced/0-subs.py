#!/usr/bin/python3
"""
This script queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        subscribers = requests.get(url, headers=headers,
                                   allow_redirects=False).json().get("data")
        print(subscribers)
        return subscribers.get("subscribers")
    except Exception:
        return 0
