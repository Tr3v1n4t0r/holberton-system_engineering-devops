#!/usr/bin/python3
"""
Query the Reddit API and return the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    try:
        req = requests.get('https://www.reddit.com/r/{}/about.json'.
                           format(subreddit), headers={'User-Agent': 'custom'},
                           allow_redirects=False)
        return req.json().get('data').get('subscribers')
    except:
        return 0
