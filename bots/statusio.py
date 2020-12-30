# # TwitterBot/bots/statusbot.py

"""
- [x] Add the randomness of the Hashtags bot picks from the pull of hashtags
- [ ] Create a function which tweets about the articles found on Economist
- [x] Create a function which tweets about the tech world news
- [ ] Create a function which tweets about video games on Sundays
"""

import json
import tweepy
import logging
import requests
import random
import dayandtime as dat

from bs4 import BeautifulSoup
from cfg import create_api


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()

class StatusUpdate():
    """Bot Statusio - scraps the web-page for the new articles.

    Determins what day of the week it is, scraps articles
    from the predetermined pages and starts tweeting them.
    """
    
    def __init__(self, api):
        self.api = api
        self.soups = [BeautifulSoup(requests.get(f'https://www.datasciencecentral.com/page/search?q={i}').text,
                        'html.parser') for i in ['AI', 'Machine+Learning', 'Deep+Learning']]

    def ds_central(self):
        ai_hashtags = ['DataScience', 'AI', 'MachineLearning', 'DataAnalytics', 'DataViz', 'BigData',
                    'ArtificialIntelligence', 'data', 'python', 'DeepLearning']
        try:
            for s in self.soups:
                for i in s.find_all('a', href=True, text=True):
                    if i['href'].startswith('https://www.datasciencecentral.com/profiles/blogs'):
                        if i.string.startswith(('Subscribe', 'subscribe', 'See', 'More', 'Old')):
                            pass
                        else:
                            hashtag = ''
                            for h in random.sample(ai_hashtags, k=4): # Pick three unique random hashtags from the list.
                                hashtag += " #" + str(h)             
                            self.api.update_status(str(i.string + ' >> ' + i['href']) + hashtag)
        except:
            self.api.update_status("How's your Data Science project going? #DataScience #MachineLearning #AI")


    def swe_news(self):
        swe_hashtags = ['softwareengineer', 'softwaredeveloper', 'coding', 'programming',
            'programmer', 'computerscince', 'developerlife', 'technews']
        try:
            s = BeautifulSoup(requests.get('https://news.ycombinator.com/newest').text,
                    'html.parser')
            for i in s.find_all(class_='storylink'):
                for h in random.sample(swe_hashtags, k=4): # Pick four unique random hashtags from the list.
                    hashtag += " #" + str(h)  
                self.api.update_status(str(i.string) + "!!! " + i['href'] + hashtag)
        except:
            self.api.update_status("How's your programming project going? #softwareengineer #programming #coding")

    def custom_status(self):
        message = 'I created a Linux program which graphically displayes disk/partition usage! This is a first released and I plan to expand and make it better. You can support my efforts just by starring the project https://github.com/bexxmodd/vizex #python #opensource #linux'
        self.api.updated_status(message)
        # self.api.update_with_media('/home/bexx/Downloads/bexxterminal.gif', status=message)


def main():
    api = create_api()
    today = dat.find_day(dat.today())
    # while today in ['Monday', 'Wednesday', 'Friday', 'Saturday']:
    while True:
        try:
            LOGGER.info(f'Today is a {today}, time to start posting')
            # StatusUpdate(api).ds_central()
            # StatusUpdate(api).swe_news()
            StatusUpdate(api).custom_status()
            print("Status posted!")
            break
        except:
            LOGGER.info('resting')

if __name__ == '__main__':
    main()
