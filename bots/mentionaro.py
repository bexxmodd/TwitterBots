# TwittweBots/bots/mentionary.py

import tweepy
import logging

from cfg import create_api


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()

def check_mentions(api, keywords, since_id):
    LOGGER.info('Checking mentions')
    new_since_id = since_id # Stores the id as a new to compare on a new run.
    """Runs through the client's timeline for the tweets
    
    with the matching keywords to respond to them.
    """
    try:
        for tweet in tweepy.Cursor(api.mentions_timeline,
            since_id=since_id).items():
            new_since_id = max(tweet.id, new_since_id)
            for k in keywords:
                if k in tweet.text.lower():
                    LOGGER.info(f'Replying to {tweet.user.name}')
                    api.update_status(
                        status='💯💯💯',
                        in_reply_to_status_id=tweet.id,
                    )
                    break;
    except Exception:
        LOGGER.error("Error on reply", exc_info=True)
    return new_since_id

def main(keywords):
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, keywords, since_id)
        LOGGER.info("Waiting...")

if __name__ == '__main__':
    main(['thanks', 'rt', 'bexx', 'beka', 'modd', 'modebadze', 'like'])