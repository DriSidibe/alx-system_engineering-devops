#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    # Set up the base URL and headers
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)'}
    
    try:
        # Make the GET request
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the status code indicates success
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        # If any request exception occurs, return 0
        return 0
