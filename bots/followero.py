# tweepy-bots/bots/followero.py

import tweepy
import logging
from cfg import create_api
import time

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()

def follow_followers(api):
    """Follows user's back who follow me"""
    LOGGER.info("Following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            LOGGER.info(f"Following {follower.name}")
            follower.follow()

def main():
    api = create_api()
    while True:
        follow_followers(api)
        LOGGER.info("Loading...")
        time.sleep(180)

if __name__ == "__main__":
    main()