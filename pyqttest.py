from twitter import *
import os 
import sys

f = open('.key','r') 

CONSUMER_KEY=f.readline().strip()
CONSUMER_SECRET=f.readline().strip()

MY_TWITTER_CREDS = os.path.expanduser('.my_app_credentials')
if not os.path.exists(MY_TWITTER_CREDS):
    oauth_dance("My App Name", CONSUMER_KEY, CONSUMER_SECRET,
                MY_TWITTER_CREDS)

oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

twitter = Twitter(auth=OAuth(
    oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

#これで呟ける
#twitter.statuses.update(status='yatta')
