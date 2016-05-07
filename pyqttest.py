# -*- coding: utf-8 -*-
                                                                     
import twitter

CONSUMER_KEY="SaDuZBg0XMLanyNFPCELZEMQ4"
CONSUMER_SECRET="UvDGlfppKKmw5SRY1EAEeHeJQFM1L5hfp0jGeGAr50E99UgdRz"
ACCESS_TOKEN="2942019786-Qc3kejjsJj860rktJSzZi6SwO0vjGjgzJsuJFAt"
ACCESS_TOKEN_SECRET="Xa3uIhaQLQISFiv36pFxKs2tJzV99yQWgYhKtfABGjLFr"


#
#api = twitter.api(consumer_key=CONSUMER_KEY,
#                      consumer_secret=CONSUMER_SECRET,
#                      access_token_key=ACCESS_TOKEN,
#                      access_token_secret=ACCESS_TOKEN_SECRET,
#                      cache=None)
#
#api.PostUpdate("test")
#


auth = OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_stream = TwitterStream(auth=auth, domain="userstream.twitter.com")
for msg in twitter_stream.user():
    if "in_reply_to_screen_name" in msg and "text" in msg:
        if msg["in_reply_to_screen_name"] == "kasajei":
            print msg["text"]
            