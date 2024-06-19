#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def top_ten(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return None
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/drissa)'}, allow_redirects=False).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
