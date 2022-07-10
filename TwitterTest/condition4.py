import tweepy
import configparser
import pandas as pd

# Finds number of tweets from Elon Musk where Dogecoin is mentioned in an ID interval

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
keyword = 'Dogecoin'                          #case-sensitive
fromId = 1505660429338460162                  #fromDate = '2010-12-27'
untilId = 1545166492408328193                 #untilDate = '2010-12-28'
nrKeywords = 0
limit=5                                       #increase
counter=0


# runs request multiple times
for tweet in tweepy.Cursor(api.user_timeline, screen_name=user, since_id=fromId, max_id=untilId, count=100, tweet_mode='extended', exclude_replies=True).items(limit):
    try:
        if keyword in tweet.full_text:
            print(str(counter) + ' ' + tweet.user.name + ': ' + tweet.full_text)
            nrKeywords += 1
        else:
            print(str(counter) + ' Does not contain: ' + keyword)
    except tweepy.TweepyException as e:
        print(e.reason)
    except StopIteration:
        break
    
    counter += 1

print(nrKeywords)

#condition: (your keyword without the brackets) since:2010-12-27 until:2013-12-22