import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
print(myclient.list_database_names())

'''Database connection and selecting it'''
mydb = myclient["twitter_api"]

'''Collection selecting'''
user_follower = mydb["user_follower"]



