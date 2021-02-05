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

api = tweepy.API(auth, wait_on_rate_limit=True)

def check_or_write(filename:str, s1:str):
    """
    Will check if s1 is in a single line within filename and also write 
    the tweet to filename if it is not inside. Returns true when s1 is
    not inside, returns false when s1 is found. Keeps line length of text
    file less than 22

    :param filename: str(must)
    :param s1: str(must)

    :return: bool
    """
    #checks to see if s1 is already inside
    with open(filename, 'r', encoding='utf8') as f1:
        f1.seek(0)
        lines=f1.readlines()
        l=0
        for line in lines:
            l+=1
            if s1 in line:
                return False
    #makes sure that there is not more than 20 lines in txt file
    if l>20:
        while l>20:
            del lines[0]
            l-=1
        new_file=open(filename, "w+", encoding='utf8')
        for line in lines:
            new_file.write(line)
        new_file.close()

    #returns true and also writes down text into file at the end
    with open(filename, 'a', encoding='utf8') as f1:
        f1.write(s1 + '\n')
        f1.close()
        return True

#loops endlessly(60 sec interval) and checks,translates,and posts tweets
while True:
    timeline = api.user_timeline("Hapagucci", count=5, tweet_mode="extended")
    for tweet in timeline:
        if check_or_write('tweet.txt', " ".join(tweet.full_text.splitlines())):
            curr = bulk_trans(tweet.full_text)
            api.update_status(curr)
            print(tweet.full_text)
    time.sleep(60)