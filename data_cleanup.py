from lib2to3.pygram import Symbols
from operator import index
import pandas as pd
import db_connection 

# Function declaration

def prune_data(dataframe: pd.DataFrame):
    
    return dataframe

def add_to_database(dataframe: pd.DataFrame):
    
    return True # Return True if database upload is successful



# Main program


# Read tweets from file
#TODO: Should probably create way to load directly from script without JSON intermediary
raw_data_df = pd.read_json("./resources/tweets.json")

# Drops all data not that shouldn't be kept according to specs on Trello
index_drop_list = ["id",
                   "truncated",
                   "display_text_range",
                   "source",
                   "in_reply_to_status_id",
                   "in_reply_to_status_id_str",
                   "in_reply_to_user_id",
                   "in_reply_to_user_id_str",
                   "in_reply_to_screen_name",
                   "geo",
                   "coordinates",
                   "place",
                   "contributors",
                   "retweeted_status",
                   "is_quote_status",
                   "favorited",
                   "retweeted",
                   "possibly_sensitive",
                   "quoted_status_id",
                   "quoted_status_id_str",
                   "quoted_status"
                    ]

pruned_data_df = raw_data_df.drop(columns=index_drop_list)

pruned_data_json = pruned_data_df.to_dict('records')
#print(pruned_data_json)

#db_connection.connect_to_db()['TWEETS'].delete_many({}) #NOTE: Added to remove all documents in db inbetween runs
#db_connection.upload_to_db('TWEETS', pruned_data_json)


#TODO: Separate into hashtags and cashtags. Drop indices and store all instances of symbols

"""
TODO: implement the following

How to get desired hashtag-dataset:
    
1. From pruned data, get df with id_str and entities[] coloumns
"""

entities_df = pd.DataFrame({'id_str': pruned_data_df['id_str'],'entities': pruned_data_df['entities']})

entities_df = entities_df.set_index('id_str')


"""    
2. Seperate this into hashtag_df with id_str and hashtags[] coloumns
"""

entities_df['hashtags'] = entities_df['entities'].apply(lambda x: x.get('hashtags'))
entities_df['symbols'] = entities_df['entities'].apply(lambda x: x.get('symbols'))
entities_df = entities_df.drop(columns=['entities'])

symbols_df = entities_df.drop(columns=['hashtags'])
hashtags_df = entities_df.drop(columns=['symbols'])


"""    
3. Unpack hashtags[] so that you get 2 x N matrix with id_str and hashtag dict coloumns

 
4. Somehow drop 'indices' field in hashtag-dict so you're left with N rows with 'id_str' and 'hashtag' coloumns
"""

hashtags_df['hashtags'] = hashtags_df['hashtags'].apply(lambda x: [i.get('text') for i in x])


   
""" 
5. Create size M set-object containing all 'hashtag' values
"""

l = []
[l.extend(i) for i in hashtags_df["hashtags"]]


hashtags = set(l)

#print(hashtags)

"""
6. Create df with 'id_str' as row index and coloumns for all M hashstags
"""

for i in hashtags:
    hashtags_df[i] = 0


"""
7. Create matrix such that for each row, a cell is marked '1' if it contains hashtag, '0' otherwise
"""


#FIXME: This runs in O(n^2) time. Must be some way to utilise vectorisation, especially once we scale up

for index, row in hashtags_df.iterrows():

    for j in row['hashtags']:
        
        hashtags_df.at[index,j] = 1 
    
hashtags_df = hashtags_df.drop(columns=['hashtags'])


"""
8. You now have an occurance matrix that contains info about prevalance of hashtags, as well as info about which 
hashtags are found in the same tweets
"""

hashtags_df.to_csv(path_or_buf='./resources/hashtags_matrix.csv')



def main():

    #TODO: Do all the things
    
    return None