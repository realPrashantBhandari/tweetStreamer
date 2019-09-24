import tweepy
from textblob import TextBlob
import json
import pandas as pd
import twitterCredentials

# authenticating api
auth = tweepy.OAuthHandler(twitterCredentials.CONSUMER_KEY, twitterCredentials.CONSUMER_SECRET)
auth.set_access_token(twitterCredentials.ACCES_TOKEN, twitterCredentials.ACCES_TOKEN_SECRET)

api = tweepy.API(auth)

#creating dataframe
df = pd.DataFrame (columns=['User', 'Date and Time','Polarity','Subjectivity','Tweet'])

# keyword you need to search
hashtag_list = ['machine learning'] 

#steput tweet stream (count = number of tweets you want to stream)
streamTweet = api.search(hashtag_list,tweet_mode='extended',count=100)
user=[]
tweet_tx=[]
date=[]
pol=[]
sub=[]

for tweet in streamTweet:
       # to get extended tweets and re-tweets
       if 'retweeted_status' in dir(tweet):
              tweet_text=tweet.retweeted_status.full_text
       else:
              tweet_text=tweet.full_text
       tbText = TextBlob(tweet_text)

       #apeending the list
       user.append(tweet.user.screen_name)
       tweet_tx.append(tweet_text)
       date.append(tweet.created_at)
       pol.append(tbText.sentiment.polarity)
       sub.append(tbText.sentiment.subjectivity)

#creating the CSV file
df['Tweet'] = tweet_tx
df['Date and Time'] = date
df['User'] = user
df['Polarity'] = pol
df['Subjectivity'] = sub
df.to_csv('tweetAnalysis.csv',index=False)
print('File generated')

    


    
    
