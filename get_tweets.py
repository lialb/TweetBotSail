import tweepy
import json

with open('api_keys_copy.json') as f:
    api_keys = json.load(f)

auth = tweepy.OAuthHandler(api_keys['key'], api_keys['secret'])
auth.set_access_token(api_keys['access_token'], api_keys['access_secret'])

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

#print(api_keys['key'])
#print(api_keys['secret'])
