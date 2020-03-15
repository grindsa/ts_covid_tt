#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" this script parses the Berlin COVID-19 ticker in a JSON structure which can be further processed """
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":

    URL = 'https://www.tagesspiegel.de/berlin/25605226.html'
    
    # fetch URL and put them into a SOUP structure
    REQOBJ = requests.get(URL)
    SOUPOBJ = BeautifulSoup(REQOBJ.text, 'lxml').encode("utf-8")
        
    