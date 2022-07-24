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

    # print(tweets_df.columns)
    # print()
    # print(tweets_df['entities'].values[0])
    # print()
    # print(tweets_df['entities'].values[0]['hashtags'])
    # print()
    # print(tweets_df['entities'].values[0]['hashtags'][0])
    # print()
    # print(tweets_df['entities'].values[0]['hashtags'][0]['text'])

    ### Tweets ###
    number_of_tweets = len(tweets_df['entities'].values)

    # Printing
    print()
    print('### Tweets ###')
    print('Total number of tweets: ' + str(number_of_tweets))
    print()


    ### Hashtags ###
    number_of_hashtags = 0
    dict_of_unique_hashtags = {}

    for tweets in tweets_df['entities'].values:
        for hashtag in tweets['hashtags']:
            
            # Count number of hashtags in total
            number_of_hashtags += 1

            # Add and count hashtags to list of unique hashtags
            if hashtag['text'] not in dict_of_unique_hashtags.keys():
                dict_of_unique_hashtags[hashtag['text']] = 1
            else:
                dict_of_unique_hashtags[hashtag['text']] += 1

    number_of_unique_hashtags = len(dict_of_unique_hashtags)

    # Analysis
    average_number_of_hashtags = number_of_hashtags / number_of_tweets
    
    # Printing
    print('### Hashtags ###')
    print('Total number of hashtags: ' + str(number_of_hashtags))
    print('Average number of hashtags per tweet: ' + str(average_number_of_hashtags))
    print('Number of unique hashtags: ' + str(number_of_unique_hashtags))
    print()
    print('Top 5 hashtags')
    print('No   Count Hashtag')
    counter = 1
    for hashtag in sorted(dict_of_unique_hashtags, key=dict_of_unique_hashtags.get, reverse=True)[:5]:
        print(str(counter) + ':   ' + str(dict_of_unique_hashtags[hashtag]) + '    #' + hashtag)
        counter += 1
    print()

    ### Favorite Count ###
    top_five_favorite_count = tweets_df.copy().sort_values(by=['favorite_count'], ascending=False).head(5)
    
    # Printing
    print('### Favorite Count ###')
    print('Top five Tweets by favorites')
    print('No   Favorite Count  User')
    print(top_five_favorite_count.columns)
    counter = 1
    for tweet in top_five_favorite_count:
        print(tweet[2])
        # print(tweet['favorite_count'])
        # print(str(counter) + ': ' + tweet['user'] + '   ' + str(tweet['favorite_count'])
        counter += 1
    
    print(top_five_favorite_count)
    print()

    ### Retweet Count ###
    # top_five_retweet_count = tweets_df['retweet_count'].sort_values(by=['retweet_count'], inplace=True).head(5)
    # print('Top five Tweets by retweets:')
    # print(top_five_retweet_count)
    # print()

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