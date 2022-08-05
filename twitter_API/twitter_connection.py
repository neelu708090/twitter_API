import settings
from settings import API_key,API_Key_Secret,Access_Token,Access_Token_Secret,Bearer_Token
import tweepy
import logging

# auth = tweepy.OAuth2BearerHandler(bearer_token=Bearer_Token)
auth = tweepy.OAuth1UserHandler(API_key,API_Key_Secret,Access_Token,Access_Token_Secret)
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
