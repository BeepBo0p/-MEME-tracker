import tweepy
import pandas as pd
from api import twitter_setup

# Finds tweets with 500-1000 likes AND contains #bitcoin AND contains more than or equal to 3 !

# authentication
api = twitter_setup()

# search tweets
search = '#bitcoin'                            #case-sensitive
keyword = '!'
nrKeywords = 3
favoriteUpper = 1000
favoriteLower = 500
limit=5                                       #increase
counter=0


# runs request multiple times
for tweet in tweepy.Cursor(api.search_tweets, q=search, count=100, tweet_mode='extended', exclude_replies=True).items(limit):
    try:
        if tweet.favorite_count > favoriteLower:
            if tweet.favorite_count < favoriteUpper:
                if tweet.full_text.count(keyword) >= nrKeywords:
                    print(str(counter) + ' Favorites: ' + str(tweet.favorite_count) + ' Keywords: ' + str(tweet.full_text.count(keyword)) + ' ' + tweet.user.name + ': ' + tweet.full_text)
                else:
                    print(str(counter) + ' Does not contain ' + str(nrKeywords) + ': ' + keyword)
            else:
                print(str(counter) + ' Does not have favorites lower than: ' + str(favoriteUpper))
        else:
            print(str(counter) + ' Does not have favorites greater than: ' + str(favoriteLower))
    except tweepy.TweepyException as e:
        print(e.reason)
    except StopIteration:
        break
    
    counter += 1
