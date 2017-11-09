# TwitterClient.py
# Sierra Clibourne, ID: 2263981
# Jennifer Prosinski, ID: //TODO
# A twitter Client implimentation
# Final Project - Data Communications/ Computer Networks - Michael Fahy
# Start Date: 11/7/2017

# Connect to twitter and access stream


import twitter

CONSUMER_KEY = 'HJTZurnso3tIaKPy4Z13lxPGN'
CONSUMER_SECRET = 'n0YdLgQECGJt8k013QCRrQkKM8aZwYWnaBciZw1cO19zvtftek'
OAUTH_TOKEN = '316267339-6AyRTrFspamWMAcBVYNQ1oaW4Vw0QfzKj5UjduOJ'
OAUTH_TOKEN_SECRET = 'YQu6mLffg7q6wWvLOBALd8euru5mBNmoxSGVOj3qo4IAa' #THESE OAUTH TOKENS ARE FOR MY PERSONAL TWITTER ACCOUNT SO IF YOU'RE TESTING TWEETS WITH IT TELL ME FIRST PLS THX

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET) 

twitter_api = twitter.Twitter(auth=auth)

import json

from urllib import unquote

