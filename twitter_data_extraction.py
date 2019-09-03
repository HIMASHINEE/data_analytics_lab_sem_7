#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:52:20 2019

@author: Apple
"""
# this code is to extract tweets using tweepy
import tweepy as tw
import pandas as pd
access_token = "1148476189863866368-PYxfmUWkw7iffSXfdKPxMcxYgnCJPv"
access_token_secret = "4fWjalGI52iefSFsUJupwCZ0ASsbgZN8ZOVRZpTOXoluH"
consumer_key = "hrJrzflXRMi9b2In6TasctDho"
consumer_secret = "LrAe6Y5UIGQ9PAKuRjuJ6Evle8LbZJPma99311ljWtnZXcRvnd"
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)
tweets = api.search(q="Obama",count=1000, since="2005-04-03")
message=[]
for tweet in tweets:
    message.append(tweet.text)
df=pd.DataFrame({'Message':message})
df.to_csv(r"/Users/Apple/Search_Tweets.csv")
print(df)

tweets = api.search(q="himalayas",count=1000, since="2005-04-03")
message=[]
for tweet in tweets:
    message.append(tweet.text)
df=pd.DataFrame({'Message':message})
df.to_csv(r"/Users/Apple/Search_Tweets2.csv")
print(df)
