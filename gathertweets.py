from socketserver import DatagramRequestHandler
from tweepy import API
from tweepy import OAuthHandler
from tweepy import Stream
import pandas as pd
import json
import time
import re


consumerKey = 'BD099NIvp7AP4lW7LevyF7Qe2'
consumerSecret = 'tftgs8GGyNa7j8Jgwa0O5JaYdvVkdt8qNmp974tgmxsGhOQ1ZE'
authorToken = 'AAAAAAAAAAAAAAAAAAAAAKyEbQEAAAAAQbbiw8R1BPFE4UQJulLMBORvaOk%3D4x9CmyGQohCaEpjZsYL7OHrIUyvOKVp7RgoYOQ9tC5oOClYuXg'
authorSecret = 'iOquhAanqYPWWfhMYoX9qN5ECq96hGULsaaxe8bD3wWw4'


class StdOutListener(StreamListener) :
    def on_data(self, data) :
        try:
            #writing data to file
            saveFile = open('tweetDBphones.csv','a')
            saveFile.write(data)
            saveFile.close()
            return True
        except BaseException as e:
            print('failed writing data,', str(e))
            time.sleep(5)
        print(data)
        return True
    
    def on_error(self, status) :
        print(status)

def search_brand(brand, tweet):
    brand = brand.lower()
    tweet = brand.lower()
    match = re.search(brand, tweet)
    if match:
        return True
    else:
        return False


def main() :
    l = StdOutListener()
    auth = OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(authorToken, authorSecret)
    twitterStream = Stream(auth, l)
    api = API(auth, wait_on_rate_limit=True)

    twitterStream.filter(track=['iPhone', 'Apple', 'Android', 'Galaxy', 'Samsung', 'Pixel', 'LG', 'Huawei', 'Motorola', 'Nexus', 'Nokia', 'Sony', 'BlackBerry', 'iOS', 'Siri', 'Safari'])

    tweetsDataPath = 'tweetDBphones.csv'
    tweetsData = []
    tweetsFile = open(tweetsDataPath, "r")

    for line in tweetsFile:
        try:
            tweet = json.loads(line)
            tweetsData.append(tweet)
        except: 
            continue

    
    tweets_df = pd.DataFrame()

    for tweet in tweetsData:
        hashtags = []
        try:
             for hashtag in tweet.entities["hashtags"]:
                 hashtags.append(hashtag["text"])
             text = api.get_status(id=tweet.id, tweet_mode='extended').full_text
        except:
            pass

        tweets_df = tweets_df.append(pd.DataFrame({'user_name': tweet.user.name, 'user_location': tweet.user.location, 'user_description': tweet.user.description, 'date': tweet.created_at, 'text': text, 'hashtags': [hashtags if hashtags else None], 'source': tweet.source}))
        tweets_df = tweets_df.reset_index(drop=True)
    
    tweets_df.head()


# __name__
if __name__=="__main__":
    main()