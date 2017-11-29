# twitterexample.py
# Demonstrates connecting to the twitter API and accessing the twitter stream
# Author: Michael Fahy
# ID: 14508
# Email: fahy@chapman.edu
# Course: CPSC 353-01
# Assignment: PA01 Sentiment Analysis
# Version 1.1
# Date: February 15, 2016

# Demonstrates connecting to the twitter API and accessing the twitter stream


from twitter import *

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information
# on Twitter's OAuth implementation.

CONSUMER_KEY = 'oErHMiMAKXdCAVOdu1nddX8UW'
CONSUMER_SECRET = 'oZczTQlCg2t5eXehUiLGRA3XJbSkWMoqKqj1tPmetxktuT0AxS'
OAUTH_TOKEN = '316267339-KI3N2G8SxaEeIp2u4AssN8wTonCaUsvh8DDJt2Cs'
OAUTH_TOKEN_SECRET = 'MmCZLrXry3dxwagSpvo9rRn6DYIbCDMmp65PjIiMjBKIZ'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET) 

twitter_api = twitter.Twitter(auth=auth)

import json

from urllib import unquote

q1 = raw_input('Search term 1: ')

count = 1000

search_results1 = twitter_api.search.tweets(q=q1, count=count)

statuses1 = search_results1['statuses']

for _ in range(5):
    print ("Status length ", len(statuses1))
    try:
        next_results = search_results1['search_metadata']['next_results']
    except (KeyError, e): 
        break

    kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])

    search_results1 = twitter_api.search.tweets(**kwargs)
    statuses1 += search_results1['statuses']

print (json.dumps(statuses1[0], indent=1))
q2 = raw_input('Search term 2: ')

count = 1000

search_results2 = twitter_api.search.tweets(q=q2, count=count)

statuses2 = search_results2['statuses']

for _ in range(5):
    print ("Status length", len(statuses2))
    try:
        next_results = search_results2['search_metadata']['next_results']
    except (KeyError, e): 
        break
    kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])

    search_results2 = twitter_api.search.tweets(**kwargs)
    statuses2 += search_results2['statuses']

print (json.dumps(statuses2[0], indent=1))

print ("Term 1:")

status_texts = [ status['text']
                 for status in statuses1 ]
screen_names = [ user_mention['screen_name']
                 for status in statuses1
                     for user_mention in status['entities']['user_mentions'] ]
word1 = [ w
          for t in status_texts
              for w in t.split() ]


hashtags = [ hashtag['text']
             for status in statuses1
                 for hashtag in status['entities']['hashtags'] ]
print (json.dumps(status_texts[0:5], indent=1))
print (json.dumps(screen_names[0:5], indent=1))
print (json.dumps(hashtags[0:5], indent=1))
print (json.dumps(word1[0:5], indent=1))


print ("Term 2:")

status_texts2 = [ status['text']
                 for status in statuses2 ]

screen_names2 = [ user_mention['screen_name']
                 for status in statuses2
                     for user_mention in status['entities']['user_mentions'] ]

hashtags2 = [ hashtag['text']
             for status in statuses2
                 for hashtag in status['entities']['hashtags'] ]


word2 = [ w
          for t in status_texts2
              for w in t.split() ]


print (json.dumps(status_texts2[0:5], indent=1))
print (json.dumps(screen_names2[0:5], indent=1))
print (json.dumps(hashtags2[0:5], indent=1))
print (json.dumps(word2[0:5], indent=1))


def lexical_diversity(tokens):
    return 1.0*len(set(tokens))/len(tokens)

def average_words(statuses):
    total_words = sum([ len(s.split()) for s in statuses ])
    return 1.0*total_words/len(statuses)
print ("Term One:")
print ('Lexical diversity of words: ')
print (lexical_diversity(word1))
print ('Lexical diversity of screen names: ')
print (lexical_diversity(screen_names))
print ('Lexical diversity of hashtags: ')
print (lexical_diversity(hashtags))
print ('Average number of words per tweet: ')
print (average_words(status_texts))


def average_words(statuses2):
    total_words = sum([ len(s.split()) for s in statuses2 ])
    return 1.0*total_words/len(statuses2)
print ("Term Two:")
print ('Lexical diversity of words: ')
print (lexical_diversity(word2))
print ('Lexical diversity of screen names: ')
print (lexical_diversity(screen_names2))
print ('Lexical diversity of hashtags: ')
print (lexical_diversity(hashtags2))
print ('Average number of words per tweet: ')
print (average_words(status_texts2))

sent_file = open('AFINN-111.txt')


print ("TERM 1")
scoresFirst = {}
for line in sent_file:
    term, score  = line.split("\t") 
    scoresFirst[term] = int(score)  

scoreFirst = 0
for word in word1:
    uword = word.encode('utf-8')
    if uword in scoresFirst.keys():
        scoreFirst = scoreFirst + scoresFirst[word]
print (float(scoreFirst))

print ("TERM 2")
sent_file = open('AFINN-111.txt')

scoresTwo = {} 
for line in sent_file:
    term, score  = line.split("\t")  
    scoresTwo[term] = int(score) 
scoreTwo = 0
for word in word2:
    uword = word.encode('utf-8')
    if uword in scoresTwo.keys():
        scoreTwo = scoreTwo + scoresTwo[word]
print (float(scoreTwo))

if scoreFirst > scoreTwo:
    print ("Term 1 has more positive sentiment on Twitter.")
else:
    print ("Term 2 has more positive sentiment on Twitter.")