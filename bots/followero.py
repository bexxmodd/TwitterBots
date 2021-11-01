# tweepy-bots/bots/followero.py

import tweepy
import logging
import time
import os

from cfg import create_api


# Define logger to log the system messages
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()

# Create the path to the followers text file
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
followers_file = os.path.join(THIS_FOLDER, 'followers.txt')


def follow_followers(api):
    """Follows user's back who follow me"""
    LOGGER.info("Following followers")
    for follower in tweepy.Cursor(api.followers).items(20):
        if not follower.following:
            try:
                LOGGER.info(f'Following {follower.name}')
                follower.follow()
            except Exception:
                print(f'I can\'t follow {follower.name}')

def message_followers(api):
    """Thank a user for the follow"""
    for dm in tweepy.Cursor(api.followers_ids).items(25):
        if not check_if_user_in_followers(followers_file, str(dm)):
            LOGGER.info('msg sent')
            api.send_direct_message(dm, 'Thanks for the follow!')
            with open(followers_file, 'a') as f:
                f.write(str(dm) + "\n")
    LOGGER.info('no new followers')

def check_if_user_in_followers(file_name, user_to_search):
    """Check if any line in the file contains given string"""
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if user_to_search in line:
                return True
    return False

def unfollow(api):
    for f in tweepy.Cursor(api.friends).items():
        try:
            u = f.id
            count = api.get_user(u).followers_count
            if count < 330:
                api.destroy_friendship(u)
        except Exception:
            continue


def main():
    api = create_api()
    while True:
        try:
            message_followers(api)
            # follow_followers(api)
            LOGGER.info("Resting...")
            time.sleep(60 * 180)
            # unfollow(api)
        except Exception:
            continue
        # message_followers(api)
        # follow_followers(api)
        # LOGGER.info("Resting...")
        # time.sleep(60 * 180)

if __name__ == "__main__":
    main()