# TwitterClient.py
# Sierra Clibourne, ID: 2263981
# Jennifer Prosinski, ID: 2262063
# A twitter Client implimentation
# Final Project - Data Communications/ Computer Networks - Michael Fahy
# Start Date: 11/7/2017

# Connect to twitter and access stream
import twitter

twitter_api = twitter.Api(consumer_key='d8ICLBVp1RE6hEIuohrNUyCGT',
                      consumer_secret='Ri4GQ1eEc8yLwpkCI4UkKxtbMXxObLzor8Gep97pXHROlLF9WR',
                      access_token_key='908004742424518656-ePYoPahlW08jOWm62ppI9U6FOqUOEeN',
                      access_token_secret='5nP7uYGnnE5qo2sYKKpYkQ4QDQJ9oEB7RTOWoLabFC5cc')
#user ID for acc is 908004742424518656, @ is @clibo100, we'll make this modular once i figure out how logging in will work

import json
import tkinter #this is for the gui

from urllib import unquote

def userPrompt():
    #get input from user
    print "\nto exit, enter 0"
    print "to list who you're following, enter 1"
    print "to list who's following you, enter 2"
    print "to print all of your tweets, enter 3"
    print "to print your timeline, enter 4"
    print "to post a tweet, enter 5"
    user_input = input("Your choice: ")
    return user_input

def printFollowing():
    #lists everyone acc is following 
    users = twitter_api.GetFriends()
    print "\n"
    for u in users:
        print u.screen_name

def printFollowers():
    #prints all followers
    users = twitter_api.GetFollowers()
    print "\n"
    for u in users:
        print u.screen_name

def printUserTweets():
    #lists all tweets from acc
    statuses = twitter_api.GetUserTimeline(908004742424518656) #this is the ID of @clibo100, once we impliment loggin we need to change this to the user ID of the user in question
    print "\n"
    for s in statuses:
        print s.text

def printTimeline(): #TODO: this is broken i think
    #prints tweets from users acc follows
    statuses = twitter_api.GetHomeTimeline()
    print "\n"
    for s in statuses:
        print s.text

def tweet():
    #posts a tweet from @clibo100
    user_input = raw_input("Tweet Body: ")
    if len(user_input) > 140:
        print "this tweet is too long"
    else:
        status = twitter_api.PostUpdate(user_input)
        print "tweet successful"

def main():
    print "Welcome to TweetTeamRocket, a Twitter Client"
    done = 0
    
    #these are for the gui
    top = tkinter.Tk()
    top.mainloop()

    #main program loop
    while done == 0:
        choice = userPrompt()
        if choice == 0:
            done = 1
        if choice == 1:
            printFollowing()
        if choice == 2:
            printFollowers()
        if choice == 3:
            printUserTweets()
        if choice == 4:
            printTimeline()
        if choice == 5:
            tweet()

if __name__ == "__main__": main()