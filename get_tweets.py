
import json
import twitter
import pprint
import csv
import re
import tweepy

with open('api_keys_copy.json') as f:
    api_keys = json.load(f)

auth = tweepy.OAuthHandler(api_keys['key'], api_keys['secret'])
auth.set_access_token(api_keys['access_token'], api_keys['access_secret'])

api = twitter.Api(consumer_key = api_keys['key'],
                  consumer_secret = api_keys['secret'],
                  access_token_key = api_keys['access_token'],
                  access_token_secret = api_keys['access_secret'])

all_statuses = []
#get statuses, will get 200 at a time, let's go fetch 2000
statuses = api.GetUserTimeline(screen_name = "realDonaldTrump", exclude_replies = True,
trim_user = True, include_rts = False, count = 200)
all_statuses.extend(statuses)
pprint.pprint(statuses)

for i in range(0, 9):
    statuses = api.GetUserTimeline(screen_name = 'realDonaldTrump', exclude_replies=True,
    trim_user = True, include_rts = False, count = 200, max_id = statuses[-1].id)
    # pprint.pprint(statuses)
    all_statuses.extend(statuses)


with open('trump_tweets.csv', 'w') as csvfile:
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
