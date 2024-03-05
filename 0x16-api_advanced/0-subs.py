import requests

def number_of_subscribers(subreddit):
    # Reddit API endpoint URL to get subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Custom User-Agent header to avoid Too Many Requests error
    headers = {
        'User-Agent': 'MyBot/0.1'
    }
    
    try:
        # Send GET request to the Reddit API
        response = requests.get(url, headers=headers)
        
        # Check if the response is successful
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()
            
            # Extract and return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the subreddit is not valid, return 0
            return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0