import tweepy
from translator import bulk_trans
from googletrans import Translator
from collections import deque
import time
import json

f=open('keys.json',)
keys=json.load(f)

# Authenticate to Twitter
auth = tweepy.OAuthHandler(keys['api-key'], 
    keys['secret-api-key'])
auth.set_access_token(keys['access-token'], 
    keys['secret-access-token'])

api = tweepy.API(auth)

#create a queue that stores the latest 3 tweets
last_3 = deque()
# timeline = api.user_timeline("HapaGucci", count=3)
# for tweet in timeline:
#     last_3.appendleft(tweet)

while True:
    timeline = api.user_timeline("HapaGucci", count=3, tweet_mode="extended")
    for tweet in timeline:
        if tweet not in last_3:
            #if not found put it into list of found tweets
            last_3.append(tweet)
            #translate and tweet
            curr = bulk_trans(tweet.full_text)
            try:
                api.update_status(curr)
            except:
                print('couldn\'t tweet' + curr)
            print(tweet.full_text)
    #make sure queue only has 5 elements or less since we tracking last 5 tweets
    while len(last_3)>3:
        last_3.popleft()
    time.sleep(60)