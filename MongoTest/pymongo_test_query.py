# Get the database using the method we defined in pymongo_test_insert file
from pymongo_test_insert import get_database
dbname = get_database()


# Create a new collection
collection_name = dbname["user_1_items"]

# Naive way to print out database contents
"""
item_details = collection_name.find()
for item in item_details:
    # This does not give a very readable output
    print(item['item_name'], item['category'])    
"""
#NOTE: ^The major issue with doing it this way is handling missing values. This method can throw plenty of errors which all need handling


# Pandas way to print out database contents
item_details = collection_name.find({"category" : "food"})

from pandas import DataFrame
# convert the dictionary objects to dataframe
items_df = DataFrame(item_details)

print(items_df)