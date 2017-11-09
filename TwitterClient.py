# TwitterClient.py
# Sierra Clibourne, ID: 2263981
# Jennifer Prosinski, ID: //TODO
# A twitter Client implimentation
# Final Project - Data Communications/ Computer Networks - Michael Fahy
# Start Date: 11/7/2017

# Connect to twitter and access stream


import twitter

CONSUMER_KEY = 'd8ICLBVp1RE6hEIuohrNUyCGT'
CONSUMER_SECRET = 'Ri4GQ1eEc8yLwpkCI4UkKxtbMXxObLzor8Gep97pXHROlLF9WR'
OAUTH_TOKEN = '908004742424518656-ePYoPahlW08jOWm62ppI9U6FOqUOEeN'
OAUTH_TOKEN_SECRET = '5nP7uYGnnE5qo2sYKKpYkQ4QDQJ9oEB7RTOWoLabFC5cc' 
#THESE OAUTH TOKENS ARE FOR @clibo100 SO ALL TWEETING AND VIEWING WILL BE FROM THIS ACCOUNT UNTIL WE GET TWITTER ACCOUNT AUTH WORKING

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET) 

twitter_api = twitter.Twitter(auth=auth)

import json

from urllib import unquote

