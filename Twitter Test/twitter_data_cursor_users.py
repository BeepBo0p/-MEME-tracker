import tweepy
import configparser
import pandas as pd

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']


# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# create cursor
cursor = tweepy.Cursor(api.user_timeline, id='realDonaldTrump', tweet_mode="extended").items(1)


# iterate over cursor, dir() shows available fields in JSON
# for tweet in cursor:
#     print(dir(tweet))

for tweet in cursor:
    print(tweet.full_text)