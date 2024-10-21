import requests
from bs4 import BeautifulSoup
import os
import re
from datetime import datetime
import pandas as pd

def get_soup(url):
    # curl=f"http://api.scraperapi.com?api_key=c99755aae5339a44da7ebad428c2d24f&url={url}"
    # response = requests.get(curl)
    response = requests.post(url,verify=False)
    response_code=response.status_code
    soup= BeautifulSoup(response.content, 'html.parser')
    return soup,response_code

headers={'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}

url=('https://www.aimsciences.org/data/article/current-data?publisherId=DCDS-S')

soup,status_code=get_soup(url)
print(soup)
print(status_code)

