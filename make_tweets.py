import json
import argparse
import time
import tweepy
from markov_generator import generate_tweet

'''
This class is to make the actual tweets from the AI generated tweets. It parses
through the json containing the keys and access tokens.
'''

def make_tweets(csv_file, num_tweets):
    with open('api_keys.json') as data_file:
        api_keys = json.load(data_file)

    auth = tweepy.OAuthHandler(api_keys['key'], api_keys['secret'])
    auth.set_access_token(api_keys['access_token'], api_keys['access_secret'])

    api = tweepy.API(auth)

    #check if you have the right account info

    user = api.me()
    print('Making tweets from:', user.name)

    count = 0
    while count < num_tweets:
        tweet = generate_tweet(csv_file)
        api.update_status(tweet)
        time.sleep(10)
        count += 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_file', type=str, help='the csv file to make tweets using')
    parser.add_argument('num_tweets', type=int, nargs='?', const=10, help='the number of tweets to make')
    args = parser.parse_args()
    make_tweets(args.csv_file, args.num_tweets)
