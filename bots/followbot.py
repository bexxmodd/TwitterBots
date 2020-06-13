# tweepy-bots/bots/followerbot.py

import tweepy
import logging
from cfg import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def follow_followers(api):
    logger.info("Following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()

def main():
    api = create_api()
    while True:
        follow_followers(api)
        logger.info("Loading...")
        time.sleep(180)

if __name__ == "__main__":
    main()