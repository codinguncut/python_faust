import os

import twitter

from dotenv import load_dotenv
load_dotenv()

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
TWITTER_TOKEN = os.environ['TWITTER_TOKEN']
TWITTER_SECRET = os.environ['TWITTER_SECRET']


def get_tweets():
    stream = None
    try:
        stream = twitter.TwitterStream(
            auth=twitter.OAuth(TWITTER_TOKEN,
                               TWITTER_SECRET,
                               CONSUMER_KEY,
                               CONSUMER_SECRET))

        for tweet in stream.statuses.sample():
            yield tweet
    finally:
        if stream:
            del stream
