import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
# Load environment variables from .env file
load_dotenv()
# Get the MongoDB URI from environment variables
mongo_db_uri = os.getenv("MONGO_DB_URI")
if not mongo_db_uri:
    raise ValueError("Please set the MONGO_DB_URI environment variable in your .env file.")
try:
    # Connect to MongoDB using the URI from the environment variable
    client = MongoClient(mongo_db_uri)
    # Force a server call to check the connection
    client.server_info()
    print("Connection to MongoDB established successfully!")
    # Use get_default_database() to automatically fetch the database mentioned in the URI
    db = client.get_default_database()
    collections = db.list_collection_names()
    print("Collections in the database:", collections)
except ConnectionFailure as e:
    print("Could not connect to MongoDB:", e)
except Exception as e:
    print("An error occurred:", e)