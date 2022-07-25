from turtle import title
import tweepy
import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np
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

    # Visalization Help Method
    def add_value_label(x_list,y_list):
        for i in range(len(x_list)):
            plt.text(i,y_list[i]/2,y_list[i], ha="center")


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
    print('No   Count  User')
    counter = 1
    for tweet in range(5):
        favorite_count = top_five_favorite_count['favorite_count'].values[tweet]
        user = top_five_favorite_count['user'].values[tweet]['name']
        print(str(counter) + ':   ' + str(favorite_count) + '      ' + user)
        counter += 1
    print()

    # Visualization
    user_name = [ tweet['name'] for tweet in top_five_favorite_count['user'].values ]
    favorite_count = [ count for count in top_five_favorite_count['favorite_count'].values ]
    plt.bar(user_name, favorite_count)
    add_value_label(user_name, favorite_count)
    plt.title('Top five Tweets by favorites')
    plt.xlabel('Users')
    plt.ylabel('Favorite Count')
    # plt.legend(user_name, loc='upper right')          # Funker ikke
    plt.show()

    ### Retweet Count ###
    top_five_retweet_count = tweets_df.copy().sort_values(by=['retweet_count'], ascending=False).head(5)

    # Printing
    print('### Retweet Count ###')
    print('Top five Tweets by retweets')
    print('No   Count  User')
    counter = 1
    for tweet in range(5):
        retweet_count = top_five_retweet_count['retweet_count'].values[tweet]
        user = top_five_retweet_count['user'].values[tweet]['name']
        print(str(counter) + ':   ' + str(retweet_count) + '     ' + user)
        counter += 1
    print()

    # Visualization
    user_name = [ tweet['name'] for tweet in top_five_retweet_count['user'].values ]
    retweet_count = [ count for count in top_five_retweet_count['retweet_count'].values ]
    plt.pie(retweet_count, labels=user_name, autopct='%1.1f%%', textprops={'fontsize': 'x-small'}, startangle=90)   # Prosent   *Funker, men skal ikke være 100%
    # plt.pie(retweet_count, labels=user_name, autopct=lambda p: '{:.0f}'.format(p * total / 100), startangle=90)   # Tall      *Funker ikke
    plt.title('Top five Tweets by retweets')
    plt.legend(title='Users', loc='upper left', fontsize='x-small')   
    plt.show()

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