#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests

def top_ten(subreddit):
    # Reddit API endpoint for getting the hot posts of a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent header to avoid potential issues
    headers = {'User-Agent': 'my_bot/1.0'}

    # Make the API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the titles from the response JSON
        try:
            data = response.json()
            posts = data['data']['children']

            # Print the titles of the first 10 hot posts
            for post in posts:
                title = post['data']['title']
                print(title)

        except KeyError:
            print("Error: Unable to extract data from the Reddit API response.")
    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found. Please provide a valid subreddit.")
    else:
        print(f"Error: Unable to fetch data from the Reddit API. Status code: {response.status_code}")

# Example usage
top_ten("python")