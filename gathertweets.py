from socketserver import DatagramRequestHandler
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


consumerKey = 'BD099NIvp7AP4lW7LevyF7Qe2'
consumerSecret = 'tftgs8GGyNa7j8Jgwa0O5JaYdvVkdt8qNmp974tgmxsGhOQ1ZE'
authorToken = 'AAAAAAAAAAAAAAAAAAAAAKyEbQEAAAAAQbbiw8R1BPFE4UQJulLMBORvaOk%3D4x9CmyGQohCaEpjZsYL7OHrIUyvOKVp7RgoYOQ9tC5oOClYuXg'
authorSecret = 

class StdOutListener(StreamListener) :
    def on_data(self, data) :
        print(data)
        return True
    
    def on_error(self, status) :
        print(status)

def main() :
    l = StdOutListener()
    auth = OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(authorToken, authorSecret)
    stream = Stream(auth, l)

    stream.filter(track=['iPhone', 'Android', 'Galaxy', 'Samsung', 'Pixel'])

# __name__
if __name__=="__main__":
    main()