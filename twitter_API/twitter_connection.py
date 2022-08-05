import settings
from settings import API_key,API_Key_Secret,Access_Token,Access_Token_Secret,Bearer_Token
import tweepy
import logging

# auth = tweepy.OAuth2BearerHandler(bearer_token=Bearer_Token)

auth = tweepy.OAuth1UserHandler(API_key,API_Key_Secret,Access_Token,Access_Token_Secret)
api = tweepy.API(auth)

# client = tweepy.Client(bearer_token=Bearer_Token)

# client = tweepy.Client(consumer_key=API_key,consumer_secret=API_Key_Secret,access_token=Access_Token,access_token_secret=Access_Token_Secret)


