from mongo_conn import user_follower

def save_into_mongo(user_data):
    user_follower.insert_one(user_data)
