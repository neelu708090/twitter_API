import settings
from twitter_API.database import save_into_mongo
from twitter_connection import api


'''Getting Home timeline tweets'''
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.id)

'''Getting API.get_followers rate limit'''
def get_remaining_get_followers():
    rate_limit=api.rate_limit_status()
    # print(rate_limit['resources']['followers']['/followers/list']['limit'])
    return rate_limit['resources']['followers']['/followers/list']['remaining']

'''Getting user ID form screen_name'''
def get_user_id(user):
    user_data= api.get_user(screen_name=user)
    return user_data.id
# print(get_user_id('TheShubhamtv'))

'''Getting suer Followers'''
def get_followers_id(user_id,cursor=-1):
    try:
        if get_remaining_get_followers() >=1:
            hello=api.get_followers(user_id=user_id,count=200,cursor=cursor)
            for data in hello[0]:
                save_into_mongo(data._json)
            if hello[1][1] != 0:
                get_followers_id(user_id,cursor=hello[1][1])
                pass
            else:
                return -1
    except:
        return -1
        
# get_followers_id(get_user_id('TheShubhamtv'))

print(get_remaining_get_followers())