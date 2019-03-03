import tweepy
'''
This class is to make the actual tweets from the AI generated tweets.
'''

auth = tweepy.OAuthHandler(api_keys['key'], api_keys['secret'])
auth.set_access_token(api_keys['access_token'], api_keys['access_secret'])

#check if you have the right account info
user = api.me()
print (user.name)


api = tweepy.API(auth)
api.update_status (**status** = 'YOUR_TWEET_HERE')
