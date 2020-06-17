# tweepy-bots/bots/followero.py

import tweepy
import logging
from cfg import create_api
import time

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()
FOLLOWERS = []

def follow_followers(api):
    """Follows user's back who follow me"""
    LOGGER.info("Following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            try:
                LOGGER.info(f'Following {follower.name}')
                follower.follow()
            except:
                print(f'I can\'t follow {follower.name}')

def msg_follower(api):
    """Thanks a user for the follow"""
    for dm in tweepy.Cursor(api.followers_ids).items(10):
        if dm not in FOLLOWERS:
            LOGGER.info('msg sent')
            api.send_direct_message(dm, 'Thanks for the follow!')
            FOLLOWERS.append(dm)


def main():
    api = create_api()
    while True:
        msg_follower(api)
        follow_followers(api)
        LOGGER.info("Loading...")
        time.sleep(3600)

if __name__ == "__main__":
    main()