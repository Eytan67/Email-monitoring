from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost:27018/'
DB_NAME = 'emails'
COLLECTION_NAME = "all_messages"

def get_mongo_connection():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    return collection


# try:
#     db, client = get_mongo_connection()
#     print("Database names:", client.list_database_names())
#     print("Collection names in db:", db.list_collection_names())
#     if COLLECTION_NAME in db.list_collection_names():
#         print(f"Connection successful! Collection '{COLLECTION_NAME}' exists in database '{DB_NAME}'.")
#     else:
#         print(f"Connected to '{DB_NAME}', but collection '{COLLECTION_NAME}' does not exist.")
# except Exception as e:
#     print("Failed to connect to MongoDB:", e)
# finally:
#     client.close()