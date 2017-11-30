# TwitterClient.py
# Sierra Clibourne, ID: 2263981
# Jennifer Prosinski, ID: 2262063
# A twitter Client implimentation
# Final Project - Data Communications/ Computer Networks - Michael Fahy
# Start Date: 11/7/2017


#TODO:
#Figure out how logging in works and then do that
#Next button does not work (the self.next.configure(command = whatever) seems to not actually be configuring the command)

from Tkinter import *
import twitter
import json
from urllib import unquote

#instantiate the API with the Oauth tokens 
twitter_api = twitter.Api(consumer_key='d8ICLBVp1RE6hEIuohrNUyCGT',
                      consumer_secret='Ri4GQ1eEc8yLwpkCI4UkKxtbMXxObLzor8Gep97pXHROlLF9WR',
                      access_token_key='908004742424518656-ePYoPahlW08jOWm62ppI9U6FOqUOEeN',
                      access_token_secret='5nP7uYGnnE5qo2sYKKpYkQ4QDQJ9oEB7RTOWoLabFC5cc') #this logs in @clibo100

#global variables
global counter
counter = 0

#main class
class TwitterClient:

    #establishes GUI
    def __init__(self, master):

        #makes the GUI window
        self.master = master

        #set title in window
        master.title("TeamRocketTweet")

        #needed for entry fields
        vcmd = master.register(self.validate)

        #make all of the elements of the GUI, assign them titles and commands
        self.searchbar = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.searchbutton = Button(master, text="Search Tweets", command = self.searchTwitter)
        self.mytweets = Button(master, text="My Tweets", command = self.clickMyTweets)
        self.timeline = Button(master, text="Timeline", command = self.clickTimeline)
        self.followers = Button(master, text="Following", command = self.clickFollowing)
        self.tweet = Button(master, text="Tweet", command = self.clickTweet)
        self.name = Label(master, text="Choose an option above")
        self.user = Label(master, text=" ")
        self.body = Label(master, text=" ", wraplength = 200)
        self.next = Button(master, text="Next", command = self.greet)
        self.tweetfield = Entry(master, validate = "key", validatecommand = (vcmd, '%P'))
        self.tweetbutton = Button(master, text="Tweet", command = self.clickSendTweet)

        #place elements of the GUI in the right place using a grid layout. 
        self.searchbar.grid(row = 0, column = 0, columnspan = 10, sticky = W)
        self.searchbutton.grid(row = 0, column = 11, columnspan = 10, sticky = W)
        self.mytweets.grid(row = 1, column = 0, columnspan = 5, sticky = W)
        self.timeline.grid(row = 1, column = 6, columnspan = 5, sticky = W)
        self.followers.grid(row = 1, column = 11, columnspan = 5, sticky = W)
        self.tweet.grid(row = 1, column = 16, columnspan = 5, sticky = W)
        self.name.grid(row = 2, column = 0, columnspan = 20, sticky = W)
        self.user.grid(row = 3, column = 0, columnspan = 20, sticky = W)
        self.body.grid(row = 4, column = 0, columnspan = 20, sticky = W)
        self.next.grid(row = 5, column = 17, columnspan = 5, sticky = E)
        self.tweetfield.grid(row = 5, column = 0, columnspan = 10, sticky = W)
        self.tweetbutton.grid(row = 5, column = 11, columnspan = 5, sticky = W)

        #remove the elements that should be hidden on the screen on create
        self.tweetfield.grid_remove()
        self.tweetbutton.grid_remove()
        self.next.grid_remove()


    def validate(self, new_text): #function needed to validate the entry on an EditText field
        if not new_text:
            self.entered_text = 0
            return True

        try:
            self.entered_text = new_text
            return True
        except ValueError:
            return False

    def greet(self): #this is for error testing 
        print("Greetings!")

    def printMyTweet(self, counter): #puts tweet into the GUI and incriments counter 
        statuses = twitter_api.GetUserTimeline(908004742424518656) #this is the ID of @clibo100, once we impliment loggin we need to change this to the user ID of the user in question
        self.name.configure(text = statuses[counter].user.name)
        self.user.configure(text = "@" + statuses[counter].user.screen_name)
        self.body.configure(text = statuses[counter].text)
        counter += 1

    def printTimelineTweet(self, counter): #puts tweet into the GUI and incriments counter 
        statuses = twitter_api.GetHomeTimeline()
        self.name.configure(text = statuses[counter].user.name)
        self.user.configure(text = "@" + statuses[counter].user.screen_name)
        self.body.configure(text = statuses[counter].text)
        counter += 1

    def printFollowing(self, counter): #puts following into the GUI and incriments counter 
        users = twitter_api.GetFriends()
        self.name.configure(text = users[counter].name)
        self.user.configure(text = "@" + users[counter].screen_name)
        counter += 1

    def clickFollowing(self): #removes and adds elements of GUI, configures next button, displays first element
        self.next.grid()
        self.tweetfield.grid_remove()
        self.tweetbutton.grid_remove()
        counter = 0
        self.body.configure(text = " ")
        self.next.configure(command = self.printFollowing(counter))
        self.printFollowing(counter)
        counter += 1

    def clickMyTweets(self): #removes and adds elements of GUI, configures next button, displays first element
        self.next.grid()
        self.tweetfield.grid_remove()
        self.tweetbutton.grid_remove()
        counter = 0
        self.printMyTweet(counter)
        counter += 1

    def clickTimeline(self): #removes and adds elements of GUI, configures next button, displays first element
        self.next.grid()
        self.tweetfield.grid_remove()
        self.tweetbutton.grid_remove()
        counter = 0
        self.printTimelineTweet(counter)
        counter += 1

    def clickTweet(self): #removes and adds elements of GUI, configures next button, displays first element
        self.name.configure(text = " ")
        self.user.configure(text = " ")
        self.body.configure(text = " ")
        self.next.grid_remove();
        self.tweetfield.grid()
        self.tweetbutton.grid()

    def clickSendTweet(self): #sends a tweet if it's short enough
        user_input = self.tweetfield.get()
        if len(user_input) > 280:
            self.name.configure(text = "tweet too long")
        else:
            self.name.configure(text = "tweet successful")
            status = twitter_api.PostUpdate(user_input)

    def searchTwitter(self): #gets array of tweets with a search term, displays first one
        self.next.grid()
        count = 1000
        counter = 0
        query = self.searchbar.get()
        statuses = twitter_api.GetSearch(term = query)
        self.next.configure(command = self.searchNext(statuses, counter))
        self.searchNext(statuses, counter)

    def searchNext(self, statuses, counter): #displays nest tweet
        self.name.configure(text = statuses[counter].user.name)
        self.user.configure(text = "@" + statuses[counter].user.screen_name)
        self.body.configure(text = statuses[counter].text)
        counter += 1

#run program
root = Tk()
twitter_gui = TwitterClient(root)
root.mainloop()