

# Establishes a connection to the Atlas-cluster database, connects to 'stonks-project'
def connect_to_db():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://henrik:cWAW5nxszfzu65U6@testdb-plz-ignore.dtpcdz6.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example ( we will use the same database throughout the tutorial)
    return client['stonks-project']

# Returns list of all collections currently in database
def get_collection_list():
    
    db = connect_to_db()
    
    return db.list_collections()

# Returns list with names of all collections currently in database
def get_collection_names():

    collection_list = get_collection_list()
    collection_names = []

    for collection in collection_list:
        collection_names.append(collection['name'])

    return collection_names

# Creates a collection in the database, unless naming conflict, in which error is returned
def create_collection(collection_name):

    return None

# Uploads a list on the format [{json object 1}, ... , {json object n}] to a collection in the database
def upload_to_db(target_collection, list_of_json):

    db = connect_to_db()
    # print(list_of_json)

    if(target_collection in get_collection_names()):
        
        db[target_collection].insert_many(list_of_json)
        #TODO: make sure no errors occur
        
        return None
        
        
    else:
        
        print("Collection ", target_collection, " does not exist. Would you like to create it?")
        #TODO: handle this case
        
        
    # return None

# Returns list of objects from collection in database (if collection exists, otherwise None). Defaults to 50 items.
# Returned data on the format [{json object 1}, ... , {json object n}]
def get_docs_in_collection(target_collection, number_of_items=50):
    
    db = connect_to_db()

    if(target_collection in get_collection_names()):
        
        items = db[target_collection].find().limit(number_of_items)
        #TODO: make sure no errors occur
        
        return items
        
        
    else:

        print("Target collection does not exist, no documents returned")
    
        return None

