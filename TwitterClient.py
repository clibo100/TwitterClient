# TwitterClient.py
# Sierra Clibourne, ID: 2263981
# Jennifer Prosinski, ID: //TODO
# A twitter Client implimentation
# Final Project - Data Communications/ Computer Networks - Michael Fahy
# Start Date: 11/7/2017

# Connect to twitter and access stream
import twitter

twitter_api = twitter.Api(consumer_key='d8ICLBVp1RE6hEIuohrNUyCGT',
                      consumer_secret='Ri4GQ1eEc8yLwpkCI4UkKxtbMXxObLzor8Gep97pXHROlLF9WR',
                      access_token_key='908004742424518656-ePYoPahlW08jOWm62ppI9U6FOqUOEeN',
                      access_token_secret='5nP7uYGnnE5qo2sYKKpYkQ4QDQJ9oEB7RTOWoLabFC5cc')
#user ID for acc is 908004742424518656, @ is @clibo100

import json

from urllib import unquote

def userPrompt():
    print "Welcome to TweetTeamRocket, a Twitter Client"

def printFollowing():
    #lists everyone acc is following 
    users = twitter_api.GetFriends()
    print([u.screen_name for u in users])

def printFollowers():
    #prints all followers
    users = twitter_api.GetFollowers()
    print([u.screen_name for u in users])

def printUserTweets():
    #lists all tweets from acc
    statuses = twitter_api.GetUserTimeline(908004742424518656)
    print([s.text for s in statuses])

def printTimeline():
    #prints tweets from users acc follows
    statuses = twitter_api.GetHomeTimeline()
    print([s.text for s in statuses])

def tweet(text):
    #posts a tweet from @clibo100
    status = twitter_api.PostUpdate(text)
    print(status.text)