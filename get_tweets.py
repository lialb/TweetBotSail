import requests
from requests_oauthlib import OAuth1

import json
import csv
import pprint
from markov_generator import generate_tweet

pp = pprint.PrettyPrinter()
with open('api_keys.json') as data_file:
    api_keys = json.load(data_file)

# Authentication for Twitter loaded into OAuth1 object
auth = OAuth1(api_keys['key'], api_keys['secret'], api_keys['access_token'], api_keys['access_secret'])

def get_tweets(tweet_handle, writeto):

    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    params = {
        'screen_name': tweet_handle,
        'tweet_mode': 'extended',
        'count': '200',
        'include_rts': False,
        'exclude_replies': True,
        'trim_user': True,
    }

    with open(writeto, 'w') as csvfile:
        fieldnames = ['id', 'text', 'source']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        r = requests.get(url, auth=auth, params=params)
        for status in r.json():
            writer.writerow({'id': status['id'], 'text': status['full_text'], 'source': status['source']})

        for i in range(9):
            params['max_id'] = r.json()[-1]['id']
            r = requests.get(url, auth=auth, params=params)
            print(len(r.json()))
            for status in r.json():
                writer.writerow({'id': status['id'], 'text': status['full_text'], 'source': status['source']})

get_tweets('neiltyson', 'csv/ndt.csv')
