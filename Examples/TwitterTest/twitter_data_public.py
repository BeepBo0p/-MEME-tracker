import tweepy
import pandas as pd
from api import twitter_setup

# authentication
api = twitter_setup()

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







