# File following this tutorial:
# https://www.mongodb.com/languages/python

# Step 1: Connect python to Atlas cluster

# Step 2:

def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = ""

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example ( we will use the same database throughout the tutorial)
    return client['user_shopping_list']


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":

    # Get the database
    dbname = get_database() #NOTE: This seems like some sort of useful macro. Explore this facet of python