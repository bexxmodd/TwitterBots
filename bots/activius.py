# TwitterBot/bots/activius.py

import tweepy
import logging
import time
import json

from cfg import create_api
from collections import defaultdict
from datetime import datetime


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()

class ActionBot(tweepy.StreamListener):
    """Bot activiues - who is responsbile to search for

    The tweets with given keywords, like them, and rewteet.
    Only if the tweet has not been liked and retweeted before.
    """

    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def save_tweet(self, file_name: str, data: dict) -> None:
        """Writes given data to a json file"""
        with open(file_name, 'a') as outfile:
            json.dump(data, outfile, indent=4, default=str)

    def on_status(self, tweet):
        LOGGER.info(f"Processing tweet id: {tweet.id}")
        if tweet.in_reply_to_status_id or tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, I ignore it.
            LOGGER.error("Can't like my own tweet nor like the reply")
            return

        try:
            if not tweet.favorited:
                tweet.favorite()
            if not tweet.retweeted:
                tweet.retweet()
            time.sleep(45)
        except Exception as e:
            code = e.response.status_code
            if code == 429:
                LOGGER.error("Limit reached! Going to sleep for 15 minutes")
                time.sleep(1500)
            elif code == 185:
                LOGGER.error("Daily limit reached! Sleep for 3 hours")
                time.sleep(6000)
            LOGGER.error("Error on retweeting", exc_info=True)


def main(keywords):
    api = create_api()
    tweets_listener = ActionBot(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=['en'])


if __name__ == '__main__':
    main([
        'Data Science', 'Machine Learning', 'csharp',
        'Data Visualization', 'Mathematics', 'Data Engineering', 
        'Python Programming', 'Artificial Intelligence', 
        'Software Engineering', 'Java', 'software engineer', 'software developer',
        'computer science', 'javaprogramming', 'coding', 'rust programming',
        'software developer engineer', 'web development'
        ])