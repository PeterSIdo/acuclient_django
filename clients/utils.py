# acuclient_django/clients/utils.py |||
from pymongo import MongoClient
import certifi
import os
def get_mongodb_connection():
    ca = certifi.where()
    client = MongoClient(os.getenv('MONGO_URI'), tlsCAFile=ca)
    db = client.acu_clients_db
    return db.clients