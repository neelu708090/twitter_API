import sys
import os
from os import getenv 
from dotenv import load_dotenv
import logging

'''Insertion of paths in our program'''
BASE_PATH = os.getcwd()
sys.path.insert(0,BASE_PATH)
sys.path.insert(1,os.path.join(os.path.dirname(__file__)))

'''Loading .env file '''
load_dotenv(os.path.join(os.path.dirname(__file__),'.env'))

'''get all necessary information form our .env file'''
API_key=getenv('API_key',None)
API_Key_Secret=getenv('API_Key_Secret',None)
Access_Token=getenv('Access_Token',None)
Access_Token_Secret=getenv('Access_Token_Secret',None)
Bearer_Token=getenv('Bearer_Token',None)


'''Logging settings for this project'''
logger = logging.getLogger("tweepy")
handler = logging.FileHandler(filename= getenv('worker_log_path',None))
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
handler.setFormatter(formatter)

