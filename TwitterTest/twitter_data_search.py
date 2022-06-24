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
keywords = '2022'
limit=2

# keywords = '2022'
# keywords = '#2022'
# keywords = '@veritasium'

# Runs request multiple times
# Bypasses Twitter API restrictions (max 100 tweets per function call)
tweepy.Cursor(api.user_timeline, q=keywords, count=100, tweet_mode='extended').items(limit)



# create DataFrame
columns = ['User', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)

print(df)