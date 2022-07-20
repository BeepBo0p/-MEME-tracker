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

db_connection.connect_to_db()['TWEETS'].delete_many({}) #NOTE: Added to remove all documents in db inbetween runs
db_connection.upload_to_db('TWEETS', pruned_data_json)


# Extracts entities and puts them in seperate dataframe

entity_df = pd.DataFrame(list(pruned_data_df['entities']))

#print(entity_df.columns)

#TODO: Separate into hashtags and cashtags. Drop indices and store all instances of symbols

hashtags_json = entity_df['hashtags'].to_dict()



def main():

    #TODO: Do all the things
    
    return None