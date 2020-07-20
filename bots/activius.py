# TwitterBot/bots/activius.py

import tweepy
import logging
import time

from cfg import create_api


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()

class LikeAndRetweet(tweepy.StreamListener):
    """Bot activiues - who is responsbile to search for

    The tweets with given keywords, like them, and rewteet.
    Only if the tweet has not been liked and retweeted before.
    """

    def __init__(self, api):
        self.api = api
        self.me = api.me()


    def on_status(self, tweet):
        LOGGER.info(f"Processing tweet id: {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, I ignore it.
            return
        
        if not tweet.favorited:
            # Like the tweet if not liked already.
            try:
                tweet.favorite()
            except Exception:
                LOGGER.error("Error on favorited", exc_info=True)
        
        if not tweet.retweeted:
            # Retweeting the tweet if not rt'ed already.
            try:
                tweet.retweet()
            except Exception:
                LOGGER.error("Error on retweeting", exc_info=True)

        
        def or_error(self, status):
            LOGGER.error(status)

def main(keywords):
    api = create_api()
    tweets_listener = LikeAndRetweet(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=['en'])


if __name__ == '__main__':
    main(['Data Science', 'Data Analytics', 'Machine Learning', 'Data Visualization', 'Mathematics', 'Python Programming'
        'Data Engineering', 'Programming', 'Artificial Intelligence', 'Software Engineering', 'Java Programming'])