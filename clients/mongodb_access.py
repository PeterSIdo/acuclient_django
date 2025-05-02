from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import certifi
import os
from dotenv import load_dotenv

def connect_to_mongodb():
    """
    Connect to MongoDB and return the database client.
    Returns the database collection if successful, None if connection fails.
    """
    try:
        # Load the MongoDB URI from environment variables
        load_dotenv()
        
        # Get MongoDB connection string
        mongo_uri = os.getenv('MONGO_DB_URI', 'mongodb://localhost:27017/')
        db_name = os.getenv('DB_NAME')
        
        # Connect to MongoDB using certificate authority file
        ca = certifi.where()
        client = MongoClient(
            mongo_uri,
            tlsCAFile=ca,
            serverSelectionTimeoutMS=5000,  # 5 second timeout
            connectTimeoutMS=5000
        )
        
        # Test the connection
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        
        # Get the database
        db = client[db_name]
        return db.clients  # Return the clients collection
        
    except ConnectionFailure as e:
        print(f"Failed to connect to MongoDB. Error: {str(e)}")
        return None
def get_all_documents(collection):
    """
    Retrieve all documents from the specified collection.
    """
    if collection:
        try:
            documents = list(collection.find({}))
            return documents
        except Exception as e:
            print(f"Error retrieving documents: {str(e)}")
            return None
    return None
# Example usage
if __name__ == "__main__":
    # Connect to MongoDB
    collection = connect_to_mongodb()
    
    if collection:
        # Retrieve all documents
        documents = get_all_documents(collection)
        if documents:
            print("\nDocuments in collection:")
            for doc in documents:
                print(doc)
        else:
            print("No documents found or error retrieving documents.")