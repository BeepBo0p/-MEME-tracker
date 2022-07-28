import tweepy
import pandas as pd
from api import twitter_setup

# authentication
api = twitter_setup()

# Class
class Listener(tweepy.Stream):

    tweets = []
    limit = 1

    def on_status(self, status):
        self.tweets.append(status)
        # print(status.user.screen_name + ": " + status.text)

        if len(self.tweets) == self.limit:
            self.disconnect()


stream_tweet = Listener(api_key, api_key_secret, access_token, access_token_secret)


# stream by users
users = ['MehranShakarami', 'veritasium']
user_ids = []

for user in users:
    user_ids.append(api.get_user(screen_name=user).id)

stream_tweet.filter(follow=user_ids)


# create DataFrame
columns = ['User', 'Tweet']
data = []

for tweet in stream_tweet.tweets:
    if not tweet.truncated:
        data.append([tweet.user.screen_name, tweet.text])
    else:
        data.append([tweet.user.screen_name, tweet.text, tweet.extended_tweet['full_text']])

df = pd.DataFrame(data, columns=columns)

print(df)