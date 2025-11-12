import requests
from bs4 import BeautifulSoup
import os
import re
from datetime import datetime
import pandas as pd

def get_soup(url):
    # curl=f"http://api.scraperapi.com?api_key=c99755aae5339a44da7ebad428c2d24f&url={url}"
    # response = requests.get(curl)
    response = requests.get(url,headers=headers)
    response_code=response.status_code
    soup= BeautifulSoup(response.content, 'html.parser')
    return soup

headers={'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}

url=('https://revistas.ucm.es/index.php/ESMP/article/view/92160')

soup=get_soup(url)
print(soup)

