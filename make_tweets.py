import tweepy
import json
from markov_generator import generate_tweet
'''
This class is to make the actual tweets from the AI generated tweets. It parses
through the json containing the keys and access tokens.
'''
with open('api_keys_copy.json') as data_file:
    api_keys = json.load(data_file)

auth = tweepy.OAuthHandler(api_keys['key'], api_keys['secret'])
auth.set_access_token(api_keys['access_token'], api_keys['access_secret'])

api = tweepy.API(auth)


#check if you have the right account info

user = api.me()
print(user.name)

tweet = generate_tweet('trump_tweets.csv')
api.update_status(tweet)


import time
count = 0
while count < 10:
    tweet = generate_tweet('trump_tweets.csv')
    api.update_status(tweet)
    time.sleep(10)
    count += 1
