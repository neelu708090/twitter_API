from mongo_conn import mydb
from settings import logger

'''creating collection for specfic user'''
def create_collection(user_name=None):
    collection_name=mydb[user_name]
    collection_name.create_index('id',unique=True)
    return collection_name


def save_user_data(user_collection,user_data):
    try:
        user_collection.insert_one(user_data)
    except Exception as e:
        logger.error(str(e))
    