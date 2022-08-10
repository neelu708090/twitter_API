from datetime import datetime
import settings
from settings import logger
from twitter_connection import api
from database import save_user_data,create_collection
from request_window import get_remaining_requests
import tweepy
import time

class UserData:

    def __init__(self):
        self.__user_id_list=[]
        self.__ids_limit=get_remaining_requests(ids_limit=True)
        self.__user_lookup=get_remaining_requests(user_lookup=True)
    pass

    def get_user_follower_data(self,user_name):
        print('Started')
        self.user_name=user_name
        self.__get_followers_ids()
        self.__get_followers_data_by_ids()
        print("Ended")

    def __get_followers_ids(self,cursor=-1):
        try:
            if self.__ids_limit[0] > 0:
                data = api.get_follower_ids(screen_name=self.user_name,cursor=cursor,count=5000)
                self.__ids_limit[0]-=1
            else:
                current_time=datetime.utcnow().replace(microsecond=0)
                reset_time=datetime.utcfromtimestamp(self.__ids_limit[1])
                logger.warning(f'User_ids API Limit Exceeded at: {current_time}')
                delay=(reset_time - current_time).total_seconds()
                time.sleep(delay)
                self.__ids_limit=get_remaining_requests(ids_limit=True)
            if data is not None:
                self.__user_id_list.extend(data[0])
                if data[1][1] !=0:
                    self.__get_followers_ids(cursor=data[1][1])
                else:
                    return
        except tweepy.errors.TweepyException as e:
            print(type(e))
            logger.error(str(e))
    
    def __get_followers_data_by_ids(self):
        try:
            user_collection=create_collection(self.user_name)
            loops=int(len(self.__user_id_list)/100)+1
            start=0
            end=99
            for i in range(loops):
                user_list=[]
                try:
                    '''Getting user data in a batch of 100 user'''
                    for j in range(start,end):
                        user_list.append(self.__user_id_list[j])
                    if self.__user_lookup[0] > 0:
                        user_data=api.lookup_users(user_id=user_list)
                        self.__user_lookup[0]-=1
                    else:
                        current_time=datetime.utcnow().replace(microsecond=0)
                        reset_time=datetime.utcfromtimestamp(self.__ids_limit[1])
                        logger.warning(f'lookup_users API Limit Exceeded at: {current_time}')
                        delay=(reset_time - current_time).total_seconds()
                        time.sleep(delay)
                        self.__user_lookup=get_remaining_requests(user_lookup=True)
                    start+=100
                    end+=100
                    '''Saving user data in MongoDB'''
                    for j in user_data:
                        save_user_data(user_collection,j._json)
                except tweepy.errors.TweepyException as e:
                    logger.error(str(e))
        except tweepy.errors.TweepyException as e:
            logger.error(str(e))
            
userdata_obj=UserData()
userdata_obj.get_user_follower_data('DRDO_India')