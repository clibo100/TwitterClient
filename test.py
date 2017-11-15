
from Tkinter import *
import twitter
import json
from urllib import unquote

twitter_api = twitter.Api(consumer_key='d8ICLBVp1RE6hEIuohrNUyCGT',
                      consumer_secret='Ri4GQ1eEc8yLwpkCI4UkKxtbMXxObLzor8Gep97pXHROlLF9WR',
                      access_token_key='908004742424518656-ePYoPahlW08jOWm62ppI9U6FOqUOEeN',
                      access_token_secret='5nP7uYGnnE5qo2sYKKpYkQ4QDQJ9oEB7RTOWoLabFC5cc')

class TwitterClient:
    def __init__(self, master):
        self.master = master
        master.title("TeamRocketTweet")

        self.entered_text = ""

        self.label = Label(master, text="Welcome to Twitter but worse")

        self.greet_button = Button(master, text="Greet", command=self.greet)

        vcmd = master.register(self.validate)
        self.enter_text = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.close_button = Button(master, text="Close", command=master.quit)

        self.label.grid(row = 0, column = 0, columnspan = 2, sticky = W+E)
        self.greet_button.grid(row = 1, column = 0, sticky = W)
        self.close_button.grid(row = 1, column = 1, sticky = E)
        self.enter_text.grid(row = 2, column = 0, columnspan = 2, sticky = W+E)


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

root = Tk()
twitter_gui = TwitterClient(root)
root.mainloop()