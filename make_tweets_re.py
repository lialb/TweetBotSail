import json
import requests
import argparse
import time
from requests_oauthlib import OAuth1
from markov_generator import generate_tweet

def make_tweets(csv_file, num_tweets):
    with open('api_keys.json') as f:
        api_keys = json.load(f)
    auth = OAuth1(api_keys['key'], api_keys['secret'], api_keys['access_token'], api_keys['access_secret'])

    post_url = 'https://api.twitter.com/1.1/statuses/update.json'
    count = 0
    while count < num_tweets:
        post_params = {
            'status': generate_tweet(csv_file)
        }
        r = requests.post(post_url, auth=auth, params=post_params)

        time.sleep(10)
        count += 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_file', type=str, help='the csv file to make tweets using')
    parser.add_argument('num_tweets', type=int, nargs='?', default=10, help='the number of tweets to make')
    args = parser.parse_args()
    make_tweets(args.csv_file, args.num_tweets)

