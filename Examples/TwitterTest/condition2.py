import tweepy
import pandas as pd
from api import twitter_setup

# Finds tweets by Elon Musk AND contains #dogecoin

# authentication
api = twitter_setup()

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