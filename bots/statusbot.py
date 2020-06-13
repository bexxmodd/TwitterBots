# # TwitterBot/bots/statusbot.py

"""
- [ ] Add the randomness of the Hashtags bot picks from the pull of hashtags
- [ ] Create a function which tweets about the articles found on Economist
- [ ] Create a function which tweets about the tech world news
- [ ] Create a function which tweets about video games on Sundays
"""


import json
import tweepy
import logging
import requests
import dayandtime as dat

from bs4 import BeautifulSoup
from time import sleep
from cfg import create_api


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class StatusUpdate():
    
    def __init__(self, api):
        self.api = api
        self.soups = [BeautifulSoup(requests.get(f'https://www.datasciencecentral.com/page/search?q={i}').text,
                        'html.parser') for i in ['AI', 'Machine+Learning', 'Deep+Learning']]

    def ds_central(self):
        try:
            for s in self.soups:
                for i in s.find_all('a', href=True, text=True):
                    if i['href'].startswith('https://www.datasciencecentral.com/profiles/blogs'):
                        if i.string.startswith(('Subscribe', 'subscribe', 'See', 'More', 'Old')):
                            pass
                        else:
                            sleep(5)
                            self.api.update_status(str(i.string + ' >> ' + i['href'] + ' #DataScience #AI #MachineLearning'))
        except:
            self.api.update_status("How's your Data Science project doing?")

def main():
    api = create_api()
    today = dat.find_day(dat.today())
    print(today)
    if today in ['Monday', 'Wednesday', 'Thursday']:
        tweeting = StatusUpdate(api).ds_central()
    else:
        pass


if __name__ == '__main__':
    main()
