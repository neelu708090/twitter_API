import settings
from settings import logger
import tweepy
from datetime import datetime

from twitter_connection import api

def get_remaining_requests(follower_limit=None,ids_limit=None,user_lookup=None):
    try:
        rate_limit=api.rate_limit_status()
        '''Data List 0'th index is for remaining Api hit & 1'st index is for reset time'''
        data=[]
        
        if follower_limit is not None:
            data.append(int(rate_limit['resources']['followers']['/followers/list']['remaining']))
            data.append(int(rate_limit['resources']['followers']['/followers/list']['reset']))
            return data
        elif ids_limit is not None:
            data.append(int(rate_limit['resources']['followers']['/followers/ids']['remaining']))
            data.append(int(rate_limit['resources']['followers']['/followers/ids']['reset']))
            return data
        elif user_lookup is not None:
            data.append(int(rate_limit['resources']['users']['/users/lookup']['remaining']))
            data.append(int(rate_limit['resources']['users']['/users/lookup']['reset']))
            return data
        else:
            return -1
    except tweepy.TweepError as e:
        settings.logger.error(str(e))

# limit=get_remaining_requests(ids_limit=True)
# temp1=(datetime.utcnow().replace(microsecond=0))
# temp2=(datetime.utcfromtimestamp(limit[1]))
# delay=(temp2-temp1)
# delay_in_sec=delay.total_seconds()
# print(delay_in_sec)