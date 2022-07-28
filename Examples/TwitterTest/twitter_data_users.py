import tweepy
import pandas as pd
from api import twitter_setup

# authentication
api = twitter_setup()

# user tweets
user = 'veritasium'
limit=2

# Runs request multiple times
# Bypasses Twitter API restrictions (max 200 tweets per function call)
# tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)

tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')

for tweet in tweets:
    print(tweet.full_text)


# create DataFrame
columns = ['User', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)

print(df)