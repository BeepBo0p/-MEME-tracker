import tweepy
import pandas as pd
import json
from api import *
from db_connection import *

def analyse_tweets():

    tweets_collection = 'TWEETS'
    hashtags_collection = 'HASHTAGS'
    number_of_items = 100

    # Read data from MongoDB
    tweets = get_docs_in_collection(tweets_collection, number_of_items)
    hashtags = get_docs_in_collection(hashtags_collection, number_of_items)
    tweets_df = pd.DataFrame(tweets.clone())
    hashtags_df = pd.DataFrame(hashtags.clone())


    # Hashtags
    number_of_hashtags = tweets_df['entities']['hashtags'].groupby(['hashtags']).size()
    print('Number of hashtags:')
    print(number_of_hashtags)
    print()

    # Favorite Count
    top_five_favorite_count = tweets_df['favorite_count'].sort_values(by=['favorite_count'], inplace=True).head(5)
    print('Top five Tweets by favorites:')
    print(top_five_favorite_count)
    print()

    # Retweet Count
    top_five_retweet_count = tweets_df['retweet_count'].sort_values(by=['retweet_count'], inplace=True).head(5)
    print('Top five Tweets by retweets:')
    print(top_five_retweet_count)
    print()

analyse_tweets()

# index_drop_list = ["id",
#                    "truncated",
#                    "display_text_range",
#                    "source",
#                    "in_reply_to_status_id",
#                    "in_reply_to_status_id_str",
#                    "in_reply_to_user_id",
#                    "in_reply_to_user_id_str",
#                    "in_reply_to_screen_name",
#                    "geo",
#                    "coordinates",
#                    "place",
#                    "contributors",
#                    "retweeted_status",
#                    "is_quote_status",
#                    "favorited",
#                    "retweeted",
#                    "possibly_sensitive",
#                    "quoted_status_id",
#                    "quoted_status_id_str",
#                    "quoted_status"
#                     ]