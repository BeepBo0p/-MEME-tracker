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


# public tweets
public_tweets = api.home_timeline()

# print(public_tweets[0].created_at)
# print(public_tweets[0].text)
# print(public_tweets[0].user.screen_name)

# for tweet in public_tweets:
#     print(tweet.text)


# store as CSV
columns = ['Time', 'User', 'Tweet']
data = []

for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

df = pd.DataFrame(data, columns=columns)
df.to_csv('tweets.csv')







