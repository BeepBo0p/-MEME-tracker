import tweepy
import configparser
import pandas as pd
from api import twitter_setup

# Find tweets with more than 10 000 retweets AND contains #bitcoin

# authentication
api = twitter_setup()

# search tweets
search = '#bitcoin'
limit=100                                      #increase
nrRetweets=5
counter=0

# runs request multiple times
for tweet in tweepy.Cursor(api.search_tweets, q=search, count=100, tweet_mode='extended').items(limit):
    try:
        if tweet.retweet_count > nrRetweets:
            print(str(counter) + ' ' + tweet.user.name + ': ' + tweet.full_text)
        else:
            print(str(counter) + ' Not enough RTs')
    except tweepy.TweepyException as e:
        print(e.reason)
    except StopIteration:
        break
    
    counter += 1