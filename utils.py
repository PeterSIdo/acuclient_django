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
            os.getenv('MONGO_DB_URI', 'mongodb://localhost:27017/'),
            tlsCAFile=ca,
            serverSelectionTimeoutMS=5000,  # 5 second timeout
            connectTimeoutMS=5000,
            retryWrites=True
        )
        # Test the connection
        client.admin.command('ping')
        db = client.acu_clients_db
        return db.clients
    except ConnectionFailure as e:
        print(f"Failed to connect to MongoDB. Error: {str(e)}")
        print("Please check if:")
        print("1. MongoDB is running on localhost:27017")
        print("2. MONGO_URI environment variable is set correctly")
        print("3. Network connectivity is available")
        raise ConnectionFailure(f"Failed to connect to MongoDB: {str(e)}")