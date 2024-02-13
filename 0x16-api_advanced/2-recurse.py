#!/usr/bin/python3
"""
This script contains a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozila/5.0'}
    params = {'limit': 100}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        if posts:
            for post in posts:
                hot_list.append(post['data']['title'])

                after = data['data']['after']
                if after:
                    return recurse(subreddit, hot_list=hot_hotlist)
                else:
                    return (hot_list)
        else:
            return (None)
    else:
        return (None)
