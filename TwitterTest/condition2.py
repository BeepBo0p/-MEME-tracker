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
user = 'elonmusk'
keyword = 'Dogecoin'                            #case-sensitive
limit=300                                       #increase
counter=0


# runs request multiple times
for tweet in tweepy.Cursor(api.user_timeline, screen_name=user, count=100, tweet_mode='extended', exclude_replies=True).items(limit):
    try:
        if keyword in tweet.full_text:
            print(str(counter) + ' ' + tweet.user.name + ': ' + tweet.full_text)
        else:
            print(str(counter) + ' Does not contain: ' + keyword)
    except tweepy.TweepyException as e:
        print(e.reason)
    except StopIteration:
        break
    
    counter += 1