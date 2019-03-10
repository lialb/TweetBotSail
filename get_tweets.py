
import json
import twitter
import pprint
import csv
import re
import tweepy
import argparse

def generate_csv(tweet_handle, writeto):

    with open('api_keys_copy.json') as f:
        api_keys = json.load(f)

    api = twitter.Api(consumer_key=api_keys['key'],
                      consumer_secret=api_keys['secret'],
                      access_token_key=api_keys['access_token'],
                      access_token_secret=api_keys['access_secret'])

    all_statuses = []
    #get statuses, will get 200 at a time, let's go fetch 2000
    statuses = api.GetUserTimeline(screen_name=tweet_handle, exclude_replies=True, trim_user=True, include_rts=False, count=200)
    all_statuses.extend(statuses)
    pprint.pprint(statuses)

    for i in range(0, 9):
        statuses = api.GetUserTimeline(screen_name=tweet_handle, exclude_replies=True, trim_user=True, include_rts=False, count=200, max_id=statuses[-1].id)
        # pprint.pprint(statuses)
        all_statuses.extend(statuses)

    with open(writeto, 'w') as csvfile:
        fieldnames = ['id', 'text', 'source']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for status in all_statuses:
            #sources come in as "<a href=""http://twitter.com"" rel=""nofollow"">Twitter Web Client</a>" so let's just get
            #the good stuff out
            cleaner_source = re.search("\>.+\<", status.source).group(0)
            clean_source = cleaner_source[1: -1]
            writer.writerow({'id': status.id, 'text': status.text, 'source': clean_source})
    print("Your status has " + str(len(all_statuses)) + " items ")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("handle", type=str, help="The twitter user handle to get tweets from")
    parser.add_argument("output", type=str, help="The output file to write to")
    args = parser.parse_args()
    generate_csv(args.handle, args.output)

