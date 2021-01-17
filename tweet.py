import tweepy
from translator import bulk_trans
from googletrans import Translator
from collections import deque
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("kfT1kMqDb1OYsKAVMByMlIG0I", 
    "OPwrPcdfC5ipemzO945R76bUStUi5DycQattE7vqHTiOxpfNX9")
auth.set_access_token("1189949666999226368-nKTwhWRf6ZVx2twnBhRS6lGV1gg0ae", 
    "M22hdGdUxk6QE21oFvx2zxR4t745ZGUCJrmO2My18YVgV")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

while True:
    timeline = api.user_timeline("HapaGucci", count=5)
    last_5 = deque()
    for tweet in timeline:
        if tweet.text not in last_5:
            #if not found put it into list of found tweets
            last_5.append(tweet.text)
            #translate and tweet
            curr = bulk_trans(tweet.text)
            try:
                api.update_status(curr + '\n\n' + tweet.text)
            except:
                print('couldn\'t tweet' + curr)
            #if more than 5 reduce queue by 1
            last_5.popleft()
    time.sleep(60)