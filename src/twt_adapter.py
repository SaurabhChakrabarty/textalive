from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import json
from get_metadata import GetMetadata
from pro_data_handler import ProDataHandler
 
class TwtListener(StreamListener):
    def __init__(self):
        self._pro = ProDataHandler("../data/prof.txt")
        super(TwtListener, self).__init__()
    def on_data(self, data):
        try:
            tweet = json.loads(data.strip())
            if 'text' in tweet:
                if self._pro.has_profane(tweet['text']):
                    print ""
                    print tweet['text']
                else:
                    print "-",
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
    def on_error(self, status):
        print(status)
        return True

class TwtStreamer():
    def __init__(self):
        get_meta_data = GetMetadata()
        consumer_key = get_meta_data.get_consumer_key()
        consumer_secret = get_meta_data.get_consumer_secret()
        access_token = get_meta_data.get_access_token()
        access_secret = get_meta_data.get_access_secret()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        self._twitter_stream = Stream(auth, TwtListener())
    def start_streaming(self):
        self._twitter_stream.sample()

