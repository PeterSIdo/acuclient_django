from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
def test_mongodb_connection():
    # Connection string from MongoDB Atlas
    connection_string = "mongodb+srv://caresoftdevelop:Kecskegida2017@cluster0.cxv3j.mongodb.net/acu_clients_db?retryWrites=true&w=majority&ssl=true"
    
    try:
        # Initialize MongoClient
        client = MongoClient(connection_string)
        
        # The server_info() command forces a call to the server and will raise an exception if the connection fails.
        client.server_info()
        
        print("Connection to MongoDB established successfully!")
        
        # Optionally, access the specific database and list its collections
        db = client.acu_clients_db
        collections = db.list_collection_names()
        print("Collections in the 'acu_clients_db' database:", collections)
        
    except ConnectionFailure as e:
        print("Could not connect to MongoDB:", e)
    except Exception as e:
        print("An error occurred:", e)
if __name__ == "__main__":
    test_mongodb_connection()