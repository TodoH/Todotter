from twitter import *
import os 
import sys
import json

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
auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET)
#これで呟ける
#twitter.statuses.update(status='yatta')
stream = TwitterStream(auth=auth)

twitter_userstream = TwitterStream(auth=auth, domain='userstream.twitter.com')


class TimeLineTweet:
    name=""
    user_id=""
    text=""
    tweet_id=""
    
    def __init__(self,name,user_id,text,tweet_id):
        self.name = name
        self.user_id = user_id
        self.text = text
        self.tweet_id = tweet_id
    
    def getText(self):
        return(self.text)
timeline=[]
for status in twitter_userstream.user():
    try:
        timeline.append(TimeLineTweet(
                status["user"]["name"],
                status["user"]["screen_name"],
                status["text"],
                status["id"]))
        
#        print(status["text"])
    except:
        print("error")
    for i in timeline:
        print(i.getText())
#    data = json.dumps(status, ensure_ascii=False)
    
#    print(type(data))
#    print(data)
#    data = json.loads(data)
#    print(data)
#
#    try:
#        print(data["friends"])
##        print(data["text"])
#    except:
#        print("error")
#            
##Streaming APIからツイートを読み出す
#def main():
#  while 1:
#    #ストリームに接続して適当にツイートを読み出す
#    statuses = stream.statuses.user()
#    for status in statuses:
##      参照に送る
#      print(status)
#
#if __name__ == '__main__':
# main()

