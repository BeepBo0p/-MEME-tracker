import tweepy
import pandas as pd
from api import twitter_setup

# authentication
api = twitter_setup()

# create cursor
cursor = tweepy.Cursor(api.user_timeline, id='realDonaldTrump', tweet_mode="extended").items(1)


# iterate over cursor, dir() shows available fields in JSON
# for tweet in cursor:
#     print(dir(tweet))

for tweet in cursor:
    print(tweet.full_text)