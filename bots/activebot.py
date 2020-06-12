# tweepy-bots/bots/activebot.py

import tweepy
import logging
from cfg import create_api


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class LikeAndRetweet(tweepy.StreamListener):
    
    def __init__(self, api):
        self.api = api
        self.me = api.me()


    def on_status(self, tweet):
        logger.info(f"Processing tweet id: {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, I ignore it.
            return
        
        if not tweet.favorited:
            # Like the tweet if not liked already.
            try:
                tweet.favorite()
            except Exception:
                logger.error("Error on favorited", exc_inf=True)
        
        if not tweet.retweeted:
            # Retweeting the target tweet if not rt'ed before.
            try:
                tweet.retweet()
            except Exception:
                logger.error("Error on retweeting", exc_info=True)

        
        def or_error(self, status):
            logger.error(status)

def main(keywords):
    api = create_api()
    tweets_listener = LikeAndRetweet(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=['en'])


if __name__ == '__main__':
    main(['Data Science', 'Data Analytics', 'Machine Learning', 'Data Visualization', 'Data Engineering', 'Python'])