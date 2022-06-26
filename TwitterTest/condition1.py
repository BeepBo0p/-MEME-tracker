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


# search tweets
search = '#bitcoin'
limit=5                                      #increase
nrRetweets=10000
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