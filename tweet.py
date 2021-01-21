import tweepy
from translator import bulk_trans
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

def check_or_write(filename:str, s1:str):
    """
    Will check if s1 is in a single line within filename and also write 
    the tweet to filename if it is not inside. Returns true when s1 is
    not inside, returns false when s1 is found

    :param filename: str(must)
    :param s1: str(must)

    :return: bool
    """
    with open(filename, 'r', encoding='utf8') as f1:
        f1.seek(0)
        for line in f1:
            if s1 in line:
                return False
    with open(filename, 'a', encoding='utf8') as f1:
        f1.write(s1 + '\n')
        return True

while True:
    timeline = api.user_timeline("HapaGucci", count=5, tweet_mode="extended")
    for tweet in timeline:
        if check_or_write('tweet.txt', tweet.full_text):
            curr = bulk_trans(tweet.full_text)
            try:
                api.update_status(curr)
            except:
                print('couldn\'t tweet' + curr)
            print(tweet.full_text)
    time.sleep(60)