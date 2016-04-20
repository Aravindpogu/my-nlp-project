# Import the necessary methods from tweepy library
import re

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import codecs

# Variables that contains the user credentials to access Twitter API
access_token = "139812297-5zBMRGR8qw2Ap5bFbf7qXQsYSI5c2CqdjgpHfoTc"
access_token_secret = "AXiFTjSeLkAcXmcuAOTmuaJB5xZgizIYVik7LhMZXEMLA"
consumer_key = "ev4ZlqiRif3z8hK1BhpiJ1L8a"
consumer_secret = "WmJQbfB5rskd7DzubgIuScLsH3Pn4GoKWNjXUlljnxGncgJunO"


class StdOutListener(StreamListener):
    def on_data(self, data):
        # with codecs.open('fetched_tweets_trump.txt','a') as tf:
        with codecs.open('fetched_tweets_clinton.txt','a') as tf:
            tweet = json.loads(data)['text'].encode('ascii', 'ignore').decode('ascii')

            temp = re.sub(r'https?:\/\/.*\/[a-zA-Z0-9]*', '', tweet)
            temp = re.sub(r'http?:\/\/.*\/[a-zA-Z0-9]*', '', temp)
            temp = re.sub(r'https*', '', temp)
            temp = re.sub(r'http*', '', temp)
            #Remove quotes
            temp = re.sub(r'&amp;quot;|&amp;amp||&amp;', '', temp)
            #Remove citations
            temp = re.sub(r'@[a-zA-Z0-9]*', '', temp)
            temp = re.sub(r'^RT', '', temp)


            #Remove tickers
            temp = re.sub(r'\$[a-zA-Z0-9]*', '', temp)
            #Remove numbers
            temp = re.sub(r'[0-9]*','',temp)
            #remove punctuations
            temp = ''.join(c for c in temp if c not in ('!','.',':'))
            #to lower case
            temp = temp.lower().strip()

            if len(temp.split()) > 2:
                print temp
                tf.write(temp)
                tf.write('\n')
            tf.close()
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    # stream.filter(track=['Trump', 'DonaldTrump'])
    stream.filter(track=['Hillary', 'Clinton', 'HillaryClinton'])