import os
from utils.user_auth import validate_user, hash_password
from pymongo.mongo_client import MongoClient
from functools import wraps

def mongo_connection(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        client = None
        db = None
        try:
            db_password = os.getenv("MONGODB_PASSWORD")
            uri = f"mongodb+srv://infowebnaweb:{db_password}@cluster0.4kkqgaa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
            
            client = MongoClient(uri)
            db = client["database"]

            result = func(client, db, *args, **kwargs)
            return result
        except Exception as e:
            print("Error connecting to MongoDB: ", e)
        finally:
            if client:
                client.close()
    
    return wrapper


@mongo_connection
async def check_connection(client, db):
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


@mongo_connection
async def insert_user(client, db, user_data: dict):
    try:
        users_collection = db["users"]
        if validate_user(user_data):
            user_data['password'] = hash_password(user_data['password'])
            users_collection.insert_one(user_data)
    except Exception as e:
        print(e)