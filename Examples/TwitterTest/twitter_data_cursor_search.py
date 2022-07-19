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


# create cursor (endret til search_tweets?)
# cursor = tweepy.Cursor(api.search, q="Bitcoin", tweet_mode="extended").items(1)


# iterate over cursor, dir() shows available fields in JSON
# for tweet in cursor:
#     print(dir(tweet))

# for tweet in cursor:
#     print(tweet.full_text)

number_of_tweets = 2
tweets = []
likes = []
time = []

for tweet in tweepy.Cursor(api.user_timeline, id="realDonaldTrump", tweet_mode="extended").items(number_of_tweets):
    tweets.append(tweet.full_text)
    likes.append(tweet.favorite_count)
    time.append(tweet.created_at)


# create DataFrame
df = pd.DataFrame({'tweets': tweets, 'likes': likes, 'time': time})

# remove RTs
df = df[~df.tweets.str.contains("RT")]
df = df.reset_index(drop=True)


# find most liked tweets
mostlike = df.loc[df.likes.nlargest(5).index]
