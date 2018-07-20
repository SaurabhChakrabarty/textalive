from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import json
from pro_data_handler import ProDataHandler
 
class TwtListener(StreamListener):
    def __init__(self):
        self._pro = ProDataHandler('../data/prof.txt')
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
        consumer_key = 'K94NTRD4Lh9eQKWXzBHYfwguV'
        consumer_secret = 'mh9PuiLsruNo1PYNE37WSW29vl8oz0Xiw72r0iJ4ZXUI39XzUf'
        access_token = '278985689-8aUxgxfc4zDQdKVB0JQmYdd6St9zKjTBOqowzbnP'
        access_secret = 'JKPpXAocL7uKdy5melZzglzxErdXqYURH0qUPR96VP24M'
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        self._twitter_stream = Stream(auth, TwtListener())
    def start_streaming(self):
        self._twitter_stream.sample()

ts = TwtStreamer()
ts.start_streaming()
#twitter_stream.filter(track=[''])
#help(twitter_stream.sample)
