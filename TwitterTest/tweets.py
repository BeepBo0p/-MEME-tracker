import tweepy
import configparser
import pandas as pd
import json
from api import *

# Finds tweets containing one of the given hashtags (#) and contains a cashtag ($)
api = twitter_setup()

# Create search
search = '('

# Add hashtags to search
resources_df = pd.read_csv('../resources/hashtag.csv')
hashtags = resources_df['Hashtags']

for hashtag in hashtags:
    search += hashtag + ' OR '

search = search[:-4]
search += ')'

# Add cashtag to search
search += ' $'
print(search)

# Making search more effective
search += ' -is:retweet -$0 -$1'
print(search)

# search tweets
limit=100                                       #increase
counter=0
cash_counter=0
tweets_df = pd.DataFrame()

# runs request multiple times
for tweet in tweepy.Cursor(api.search_tweets, q=search, lang='en', count=100, tweet_mode='extended', exclude_replies=True).items(limit):
    try:
        # print(str(counter) + ' ' + tweet.user.name + ': ' + tweet.full_text)
        if '$' in tweet.full_text:
            print(str(counter))
            cash_counter += 1
    except tweepy.TweepyException as e:
        print(e.reason)
    except StopIteration:
        break
    
    tweets_df = pd.concat([tweets_df, pd.DataFrame([tweet._json])], axis=0)
    counter += 1

print()
print('Hentet ' + str(counter) + ' tweets.')
print(str(cash_counter) + ' av de inneholder $.')
print()
# print(df)
tweets_df.to_json(r'../resources/tweets.json', orient='records', default_handler=str)

#condition: (your keyword without the brackets) since:2010-12-27 until:2013-12-22