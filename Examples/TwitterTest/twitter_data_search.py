import tweepy
import pandas as pd
from api import twitter_setup

# authentication
api = twitter_setup()

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