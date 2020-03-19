#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" this script parses the Berlin COVID-19 ticker in a JSON structure which can be further processed """
import os
from datetime import datetime
import json
import textwrap
import configparser
import requests
from bs4 import BeautifulSoup
from wa_hack_cli import simple_send

def load_config(cfg_file=os.path.dirname(__file__)+'/data/'+'ts_covid_tt.cfg'):
    """ small configparser wrappter to load a config file """
    config = configparser.RawConfigParser()
    config.read(cfg_file)
    return config


def print_debug(debug, text):
    """ little helper to print debug messages """
    if debug:
        print('{0}: {1}'.format(datetime.now(), text))

def json_load(file_name_):
    """ load json structure from file """
    print_debug(DEBUG, 'json_load({0})\n'.format(file_name_))
    if os.path.isfile(file_name_):
        with open(file_name_, encoding='utf8') as json_file:
            data = json.load(json_file)
    else:
        data = {}
    return data

def json_store(file_name_, data_):
    """ store structure as json to file """
    with open(file_name_, 'w', encoding='utf-8') as out_file:
        json.dump(data_, out_file, ensure_ascii=False, indent=4)


if __name__ == "__main__":

    URL = 'https://www.tagesspiegel.de/berlin/25605226.html'
    JSON_FILE = '/usr/local/ts_covid_tt/data/tsbln.json'
    DEBUG = False

    # fetch URL and put them into a SOUP structure
    REQOBJ = requests.get(URL)
    SOUPOBJ = BeautifulSoup(REQOBJ.text, 'lxml')

    DATA_DIC = json_load(JSON_FILE)
    CFG_DIC = load_config()

    # new headlines will be stored here....
    NEW_ARTICLES = []

    for t_obj in SOUPOBJ.findAll('div', attrs={'class': ['timeline-body']}):
        # filter articles
        for article in t_obj.findAll('article', attrs={'class': ['lb-post']}):
            obj_id = article['data-post-id']

            post_header = article.find('div', attrs={'class': ['lb-post-header']})
            lb_type = post_header.find('div', attrs={'class': ['lb-type']})

            if 'lb-type--embed-twitter' in lb_type['class']:
                # stop twitter shit
                continue

            div_container = article.find('div', attrs={'class': ['items-container']})
            # print(div_container)
            div_obj = div_container.find('div', attrs={'class': ['lb-item', 'text']})

            if div_obj.find('h4'):
                headline = div_obj.find('h4').text.strip()
                msg_text = div_obj.find(['p', 'div', 'article']).text.strip().replace(headline, '')
            elif div_obj.find('b'):
                headline = div_obj.find('b').text.strip()
                msg_text = None
            elif div_obj.find('article'):
                headline = div_obj.find('article').text.strip()
                msg_text = None
            elif div_obj.find('div', attrs={'class': ['item--embed__element']}):
                # this is bullshit from social networks lets ignore
                headline = None
                msg_text = None
            else:
                headline = None
                msg_text = None

            # if lb-type--embed-twitter
            if headline and obj_id:
                if obj_id not in DATA_DIC:
                    DATA_DIC[obj_id] = {'headline': headline, 'text': msg_text}
                    if msg_text:
                        NEW_ARTICLES.append('_{0}_\n{1}\n'.format(headline, textwrap.shorten(msg_text, width=200)))
                    else:
                        NEW_ARTICLES.append('{0}\n'.format(headline))

    json_store(JSON_FILE, DATA_DIC)
    if NEW_ARTICLES and 'DEFAULT' in CFG_DIC:
        NOW = datetime.now()
        MESSAGE = '*Tagesspiegel COVID-19  Blog:*\n{1}\nurl: {0}\n'.format(URL, NOW.strftime("%d.%m. %H:%M"))
        if 'WA_SRV' in CFG_DIC['DEFAULT'] and 'WA_PORT' in CFG_DIC['DEFAULT'] and 'WA_DESTINATION' in CFG_DIC['DEFAULT']:
            WA_SRV = CFG_DIC['DEFAULT']['WA_SRV']
            WA_PORT = int(CFG_DIC['DEFAULT']['WA_PORT'])
            WA_DST = CFG_DIC['DEFAULT']['WA_DESTINATION']

            for article in NEW_ARTICLES:
                MESSAGE = '{0}\n{1}'.format(MESSAGE, article)
            simple_send(WA_SRV, WA_PORT, WA_DST, MESSAGE)
