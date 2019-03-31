import requests
from requests_oauthlib import OAuth1
import argparse
import json
import csv
import pprint
from markov_generator import generate_tweet

'''
This class gets tweets from a specific user and outputs their tweets to a
csv file
'''

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
    #for non-Windows users, remove the encoding='utf-8'
    with open(writeto, 'w', encoding='utf-8') as csvfile:
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

#get_tweets('Drawfeeshow', 'drawfee.csv')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('tweet_handle', type=str, help='the twitter user to pull tweets from')
    parser.add_argument('writeto', type=str, help='output tweets into a file')
    args = parser.parse_args()
    get_tweets(args.tweet_handle, args.writeto)
