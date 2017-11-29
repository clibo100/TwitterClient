
from Tkinter import *
import twitter
import json
from urllib import unquote

twitter_api = twitter.Api(consumer_key='d8ICLBVp1RE6hEIuohrNUyCGT',
                      consumer_secret='Ri4GQ1eEc8yLwpkCI4UkKxtbMXxObLzor8Gep97pXHROlLF9WR',
                      access_token_key='908004742424518656-ePYoPahlW08jOWm62ppI9U6FOqUOEeN',
                      access_token_secret='5nP7uYGnnE5qo2sYKKpYkQ4QDQJ9oEB7RTOWoLabFC5cc')
global buttonswitch 
buttonswitch = 0
global counter
counter = 0


class TwitterClient:
    def __init__(self, master):
        self.master = master
        master.title("TeamRocketTweet")

        vcmd = master.register(self.validate)

        self.entered_text = ""

        self.searchbar = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.searchbutton = Button(master, text="Search", command = self.greet)
        self.mytweets = Button(master, text="My Tweets", command = self.greet)
        self.timeline = Button(master, text="Timeline", command = self.greet)
        self.followers = Button(master, text="Followers", command = self.clickFollowers)
        self.tweet = Button(master, text="Tweet", command = self.greet)
        self.name = Label(master, text="Barack Obama")
        self.user = Label(master, text="@BarackObama")
        self.body = Label(master, text="body is empty")
        self.next = Button(master, text="Next", command = self.clickNext(buttonswitch, counter))


        self.searchbar.grid(row = 0, column = 0, columnspan = 10, sticky = W)
        self.searchbutton.grid(row = 0, column = 11, columnspan = 10, sticky = W)
        self.mytweets.grid(row = 1, column = 0, columnspan = 5, sticky = W)
        self.timeline.grid(row = 1, column = 6, columnspan = 5, sticky = W)
        self.followers.grid(row = 1, column = 11, columnspan = 5, sticky = W)
        self.tweet.grid(row = 1, column = 16, columnspan = 5, sticky = W)
        self.name.grid(row = 2, column = 0, columnspan = 20, sticky = W)
        self.user.grid(row = 3, column = 0, columnspan = 20, sticky = W)
        self.body.grid(row = 4, column = 0, columnspan = 20, sticky = W)
        self.next.grid(row = 5, column = 15, columnspan = 5, sticky = E)



    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_text = 0
            return True

        try:
            self.entered_text = new_text
            return True
        except ValueError:
            return False

    def greet(self):
        print("Greetings!")

    def tweet(self, text):
        print text

    def printFollowing(self, counter):
        users = twitter_api.GetFriends()
        self.name.configure(text = users[counter].name)
        self.user.configure(text = "@" + users[counter].screen_name)
        counter += 1

    def clickNext(self, buttonswitch, counter): #TODO: next button doesn't work so yeah fix that
        if buttonswitch == 2:
            self.printFollowing(counter)

    def clickFollowers(self):
        counter = 0
        buttonswitch = 2
        self.body.configure(text = " ")
        self.clickNext(buttonswitch, counter)




root = Tk()
twitter_gui = TwitterClient(root)
root.mainloop()