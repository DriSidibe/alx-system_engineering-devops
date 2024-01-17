#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests

def number_of_subscribers(subreddit):
    # Reddit API endpoint for getting subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent header to avoid potential issues
    headers = {'User-Agent': 'my_bot/1.0'}

    # Make the API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the subscriber count from the response JSON
        try:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        except KeyError:
            print("Error: Unable to extract data from the Reddit API response.")
            return 0
    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found. Please provide a valid subreddit.")
        return 0
    else:
        print(f"Error: Unable to fetch data from the Reddit API. Status code: {response.status_code}")
        return 0

# Example usage
subreddit = "python"
subscribers_count = number_of_subscribers(subreddit)
print(f"The number of subscribers for '{subreddit}' is: {subscribers_count}")