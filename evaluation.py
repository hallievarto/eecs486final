import tweepy as tw
import pandas as pd
import requests
import json
import pprint

api_key = "BD099NIvp7AP4lW7LevyF7Qe2"
api_secret = "tftgs8GGyNa7j8Jgwa0O5JaYdvVkdt8qNmp974tgmxsGhOQ1ZE"
accessToken = "2336815568-NAA5UDdws21NwMytIp88sP4ROW1OfX3NS6N0CAk"
accessSecret = "i2KOOHDxBOnlSWfB3uIMbNG584ILktzQSapu367IgYd9m"
bearer = 'AAAAAAAAAAAAAAAAAAAAAKyEbQEAAAAAZG58%2FSnLV9ymmgRgL98VZOQ6xow%3DawbBK4LDYraI5lj6KOW2PmhhnAP2zOB8rhcSnFiHIg63lUnLFf'

client = tw.Client(bearer_token=bearer, 
                    consumer_key=api_key, 
                    consumer_secret=api_secret, 
                    access_token=accessToken, 
                    access_token_secret=accessSecret, 
                    return_type = dict,
                    wait_on_rate_limit=True)

search_query = 'Safari'

tweets = client.search_recent_tweets(query=search_query, end_time=None, expansions=None, max_results=100, media_fields=None, next_token=None, place_fields='country', poll_fields=None, since_id=None, sort_order=None, start_time=None, tweet_fields='source', until_id=None, user_fields=None, user_auth=False)

tweets_copy = []
for tweet in tweets['data']:
    tweets_copy.append(tweet)
pprint.pprint(tweets_copy)

with open('Safari.txt', 'wt') as out:
    pprint.pprint(tweets_copy, stream=out)


#tweets_dict = tweets.json()
#tweets_data = tweets_dict['data'] 
#df = pd.json_normalize(tweets_data) 

#df.to_csv("tweets.csv")

