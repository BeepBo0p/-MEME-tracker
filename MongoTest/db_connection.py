# TODO: write some actual god damn code, eh?

# Establishes a connection to the Atlas-cluster database
def connect_to_db():

    return None

# Uploads a list on the format [{json object 1}, ... , {json object n}] to a collection in the database
def upload_to_db(target_collection, list_of_json):

    return None

# Returns list of objects from collection in database (if collection exists, otherwise None). Defaults to 50 items.
# Returned data on the format [{json object 1}, ... , {json object n}]
def get_docs_in_collection(target_collection, number_of_items=50):

    return None

# Returns list of all collections currently in database
def get_collection_list():

    return None

# Creates a collection in the database, unless naming conflict, in which error is returned
def create_collection(collection_name):

    return None

