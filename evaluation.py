import tweepy as tw
import pandas as pd

api_key = "BD099NIvp7AP4lW7LevyF7Qe2"
api_secret = "tftgs8GGyNa7j8Jgwa0O5JaYdvVkdt8qNmp974tgmxsGhOQ1ZE"
accessToken = "2336815568-NAA5UDdws21NwMytIp88sP4ROW1OfX3NS6N0CAk"
accessSecret = "i2KOOHDxBOnlSWfB3uIMbNG584ILktzQSapu367IgYd9m"
bearer = 'AAAAAAAAAAAAAAAAAAAAAKyEbQEAAAAAZG58%2FSnLV9ymmgRgL98VZOQ6xow%3DawbBK4LDYraI5lj6KOW2PmhhnAP2zOB8rhcSnFiHIg63lUnLFf'

client = tw.Client(bearer_token=bearer)

search_query = 'america'

tweets = client.search_recent_tweets(query=search_query, tweet_fields=["context_annotations", "created_at", "source"], max_results=100)
tweets_copy = []
file_name = 'tweets.txt'

for tweet in tweets:
    tweets_copy.append(tweet)
print(tweets_copy)