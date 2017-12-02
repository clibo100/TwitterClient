# TwitterClient.py
# Sierra Clibourne, ID: 2263981
# Jennifer Prosinski, ID: 2262063
# A twitter Client implimentation
# Final Project - Data Communications/ Computer Networks - Michael Fahy
# Start Date: 11/7/2017


from Tkinter import *
import twitter
import json
from urllib import unquote
import urlparse
import oauth2 as oauth

#instantiate the API with the Oauth tokens 
#twitter_api = twitter.Api(consumer_key='d8ICLBVp1RE6hEIuohrNUyCGT',
#                      consumer_secret='Ri4GQ1eEc8yLwpkCI4UkKxtbMXxObLzor8Gep97pXHROlLF9WR',
#                      access_token_key='908004742424518656-ePYoPahlW08jOWm62ppI9U6FOqUOEeN',
#                      access_token_secret='5nP7uYGnnE5qo2sYKKpYkQ4QDQJ9oEB7RTOWoLabFC5cc') 

#global variables
counter = 0
global choice 
choice = 0
users = []
statuses1 = []
statuses2 = []
statuses3 = []

#main class
class TwitterClient:

    #establishes GUI
    def __init__(self, master):
        #makes the GUI window
        self.master = master
        counter = 0
        #set title in window
        master.title("TeamRocketTweet")

        #needed for entry fields
        global vcmd
        vcmd = master.register(self.validate)

        self.URL_label = Label(master, text = "Please visit this website:")
        self.URL = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.pin_label = Label(master, text = "Please Enter Pin:")
        self.pin_entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.pin_button = Button(master, text="Enter", command = self.clickEnterPin)

        self.URL_label.grid(row = 0, column = 0, columnspan = 20, sticky = W)
        self.URL.grid(row = 1, column = 0, columnspan = 20, sticky = W)
        self.pin_label.grid(row = 2, column = 0, columnspan = 20, sticky = W)
        self.pin_entry.grid(row = 3, column = 0, columnspan = 10, sticky = W)
        self.pin_button.grid(row = 3, column = 11, columnspan = 10, sticky = W)

        global consumer_key
        consumer_key = 'd8ICLBVp1RE6hEIuohrNUyCGT'
        global consumer_secret
        consumer_secret = 'Ri4GQ1eEc8yLwpkCI4UkKxtbMXxObLzor8Gep97pXHROlLF9WR'

        global request_token_url
        request_token_url = 'https://api.twitter.com/oauth/request_token'
        global access_token_url
        access_token_url = 'https://api.twitter.com/oauth/access_token'
        global authorize_url
        authorize_url = 'https://api.twitter.com/oauth/authorize'

        global consumer
        consumer = oauth.Consumer(consumer_key, consumer_secret)
        global client
        client = oauth.Client(consumer)
            
        resp, content = client.request(request_token_url, "GET")
        if resp['status'] != '200':
            raise Exception("Invalid response %s." % resp['status'])

        global request_token
        request_token = dict(urlparse.parse_qsl(content))

        self.URL.insert(0, "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token']))

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

    def clickFollowing(self): #removes and adds elements of GUI, configures next button, displays first element
        self.next.grid()
        self.tweetfield.grid_remove()
        self.tweetbutton.grid_remove()
        users = twitter_api.GetFriends()
        global counter
        global choice
        counter = 0
        choice = 0
        self.body.configure(text = " ")
        self.clickNext()

    def clickMyTweets(self): #removes and adds elements of GUI, configures next button, displays first element
        self.next.grid()
        self.tweetfield.grid_remove()
        self.tweetbutton.grid_remove()
        global counter
        global choice
        counter = 0
        choice = 1

        statuses = twitter_api.GetUserTimeline(user_ID) 
        self.clickNext()

    def clickTimeline(self): #removes and adds elements of GUI, configures next button, displays first element
        self.next.grid()
        self.tweetfield.grid_remove()
        self.tweetbutton.grid_remove()
        global counter
        global choice
        counter = 0
        choice = 2
        statuses = twitter_api.GetHomeTimeline()
        self.clickNext()

    def clickTweet(self): #removes and adds elements of GUI, configures next button, displays first element
        self.name.configure(text = " ")
        self.user.configure(text = " ")
        self.body.configure(text = " ")
        self.next.grid_remove();
        self.tweetfield.grid()
        self.tweetbutton.grid()
        self.tweetfield.delete(0, 'end')

    def clickSendTweet(self): #sends a tweet if it's short enough
        user_input = self.tweetfield.get()
        global statuses1
        global statuses2
        if len(user_input) > 140:
            self.name.configure(text = "tweet too long")
        else:
            self.name.configure(text = "tweet successful")
            status = twitter_api.PostUpdate(user_input)
            statuses1 = twitter_api.GetUserTimeline(user_ID)
            statuses2 = twitter_api.GetHomeTimeline()

    def clickSearch(self): #gets array of tweets with a search term, displays first one
        self.tweetfield.grid_remove()
        self.tweetbutton.grid_remove()
        global counter
        global choice
        counter = 0
        choice = 3
        global query
        global statuses3
        query = self.searchbar.get()
        if query != "":
            self.next.grid()
            statuses3 = twitter_api.GetSearch(term = query)
            self.clickNext()

    def clickNext(self): #displays next tweet or user to the GUI
        global counter
        global users
        global statuses1
        global statuses2
        global statuses3
        if choice == 0:
            if users == []:
                users = twitter_api.GetFriends()
            if counter < len(users):
                self.name.configure(text = users[counter].name)
                self.user.configure(text = "@" + users[counter].screen_name)
                counter += 1
        if choice == 1:
            if statuses1 == []:
                statuses1 = twitter_api.GetUserTimeline(user_ID)
            if counter < len(statuses1):
                self.name.configure(text = statuses1[counter].user.name)
                self.user.configure(text = "@" + statuses1[counter].user.screen_name)
                self.body.configure(text = statuses1[counter].text)
                counter += 1
        if choice == 2:
            if statuses2 == []:
                statuses2 = twitter_api.GetHomeTimeline()
            if counter < len (statuses2):
                self.name.configure(text = statuses2[counter].user.name)
                self.user.configure(text = "@" + statuses2[counter].user.screen_name)
                self.body.configure(text = statuses2[counter].text)
                counter += 1
        if choice == 3:
            global query
            if statuses3 == []:
                statuses = twitter_api.GetSearch(term = query)
            if counter < len(statuses3):
                self.name.configure(text = statuses3[counter].user.name)
                self.user.configure(text = "@" + statuses3[counter].user.screen_name)
                self.body.configure(text = statuses3[counter].text)
                counter += 1

    def clickEnterPin(self):
        oauth_verifier = self.pin_entry.get()

        token = oauth.Token(request_token['oauth_token'],
            request_token['oauth_token_secret'])
        token.set_verifier(oauth_verifier)
        client = oauth.Client(consumer, token)

        resp, content = client.request(access_token_url, "POST")
        access_token = dict(urlparse.parse_qsl(content))

        self.URL_label.grid_remove()
        self.URL.grid_remove()
        self.pin_label.grid_remove()
        self.pin_entry.grid_remove()
        self.pin_button.grid_remove()

        global twitter_api
        twitter_api = twitter.Api(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token_key = access_token['oauth_token'], access_token_secret = access_token['oauth_token_secret'])

        self.enter_name_label = Label(self.master, text = "Please enter your screen name. Example: @twitter", wraplength = 200)
        self.enter_name = self.searchbar = Entry(self.master, validate="key", validatecommand=(vcmd, '%P'))
        self.enter_name_button = Button(self.master, text="Enter", command = self.clickEnterScreenName)

        self.enter_name_label.grid(row = 0, column = 0, columnspan = 20, sticky = W)
        self.enter_name.grid(row = 1, column = 0, columnspan = 10, sticky = W)
        self.enter_name_button.grid(row = 1, column = 11, columnspan = 10, sticky = W)

    def clickEnterScreenName(self):
        global user_screenname 
        user_screenname = self.enter_name.get()
        if user_screenname[0] == "@":
            user_screenname = user_screenname[1:]

        global user_object
        user_object = twitter_api.GetUser(screen_name = user_screenname)

        global user_ID 
        user_ID = user_object.id

        self.enter_name_label.grid_remove()
        self.enter_name.grid_remove()
        self.enter_name_button.grid_remove()

        #make all of the elements of the GUI, assign them titles and commands
        self.searchbar = Entry(self.master, validate="key", validatecommand=(vcmd, '%P'))
        self.searchbutton = Button(self.master, text="Search Tweets", command = self.clickSearch)
        self.mytweets = Button(self.master, text="My Tweets", command = self.clickMyTweets)
        self.timeline = Button(self.master, text="Timeline", command = self.clickTimeline)
        self.followers = Button(self.master, text="Following", command = self.clickFollowing)
        self.tweet = Button(self.master, text="Tweet", command = self.clickTweet)
        self.name = Label(self.master, text="Choose an option above")
        self.user = Label(self.master, text=" ")
        self.body = Label(self.master, text=" ", wraplength = 200)
        self.next = Button(self.master, text="Next", command = self.clickNext)
        self.tweetfield = Entry(self.master, validate = "key", validatecommand = (vcmd, '%P'))
        self.tweetbutton = Button(self.master, text="Tweet", command = self.clickSendTweet)

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

#run program
root = Tk()
twitter_gui = TwitterClient(root)
root.mainloop()