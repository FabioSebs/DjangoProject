import website.twitter_credentials as twitter_credentials
import numpy as np
import pandas as pd

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
from google_trans_new import google_translator



######TWITTER CLIENT ##########
class TwitterClient():
    
    def __init__(self, twitter_user = None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user
        
    def get_twitter_client_api(self):
        return self.twitter_client
        
        
    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id = self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets
    
    def get_friend_list(self, num_friends):
        friend_list = []
        for friend in Cursor(self.twitter_client.friends ,  id = self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list
    
    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline,  id = self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets
            

    


####### TWITTER AUTHENTICATOR ########
class TwitterAuthenticator():
    
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACESS_TOKEN_SECRET)
        return auth
        


###### TWITTER STREAMER ###########
class TwitterStreamer():
    
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()
    
    def stream_tweets(self , fetched_tweets_filename, hash_tag_list):
        # This handles twitter authentication and the connection to the twitter streaming api
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()    
        stream = Stream(auth, listener)
        
        # This line filters Twitter Streams to capture data by keywords
        stream.filter(track = hash_tag_list)


####### TWITTER STREAM LISTENER ######
class TwitterListener(StreamListener):
    
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
        
    
    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
                return True
        except BaseException as e:
            print("Error on data: %s" % str(e))
            
        return True
    
    def on_error(self, status):
        
        if status == 420:
            return False
        
        print(status)

class TweetAnalyzer():
    """
    Functionality for analyzing and categorizing content from tweets
    """
    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(data = [tweet.text for tweet in tweets], columns = ['Tweets'])
        
        #df['id'] = np.array([tweet.id for tweet in tweets])
        #df['len'] = np.array([len(tweet.text) for tweet in tweets])
        #df['date'] = np.array([tweet.created_at for tweet in tweets])
        #df['source'] = np.array([tweet.source for tweet in tweets]) 
        #df['likes'] = np.array([tweet.favorite_count for tweet in tweets])   
        #df['retweers'] = np.array([tweet.retweet_count for tweet in tweets])
        return df
    
    def tweet_list(self, tweets):
        quotelist = [tweet.full_text for tweet in tweets ]
        return quotelist
        
def CreateTweets():
    # Function to create tweets and use it for my project
    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()
    api = twitter_client.get_twitter_client_api()  
    
    tweets = api.user_timeline(screen_name="naruto_quote", count=10, tweet_mode='extended')
    
    df = tweet_analyzer.tweet_list(tweets)
    return(df)

def TweetsTranslated():
    translator = google_translator()
    
    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()
    api = twitter_client.get_twitter_client_api()  
    
    tweets = api.user_timeline(screen_name="naruto_quote", count=10, tweet_mode='extended')
    
    df = tweet_analyzer.tweet_list(tweets)
    
    english_tweets = []
    
    for i in df:
        t = translator.translate(i, lang_src='id', lang_tgt='en')
        english_tweets.append(t)
    
    return english_tweets
        

    
    

    
    
if __name__ == "__main__":
    TweetsTranslated()
        
 
     
