from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import certifi
import os
from dotenv import load_dotenv

def get_mongodb_connection():
    load_dotenv()  # Load environment variables from .env
    ca = certifi.where()
    try:
        # Add connection timeout and retry logic
        client = MongoClient(
            os.getenv('MONGO_DB_URI'),
            tlsCAFile=ca,  # Ensure SSL/TLS is used
            serverSelectionTimeoutMS=5000,  # 5 second timeout
            connectTimeoutMS=5000,
            retryWrites=True
        )
        # Test the connection
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        
        # Get the database
        db = client[os.getenv('DB_NAME')]  # Use the DB_NAME from .env
        return db['client_client']  # Return the specific collection
    except ConnectionFailure as e:
        print(f"Failed to connect to MongoDB. Error: {str(e)}")
        raise ConnectionFailure(f"Failed to connect to MongoDB: {str(e)}")
