import time
import requests
from bs4 import BeautifulSoup
import os
import re
from datetime import datetime
import pandas as pd
import json

def get_soup(url):
    # curl=f"http://api.scraperapi.com?api_key=1b76ffea4316105cc9baba7ff64b8353&url={url}"
    # response = requests.get(curl)
    response = requests.get(url,headers=headers)
    soup= BeautifulSoup(response.content, 'html.parser')
    return soup

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Priority": "u=1, i",
    "Referer": "https://formative.jmir.org/2024",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "X-Journal-Id": "27",
    "X-Journal-Slug": "formative"
}

url=f'https://formative.jmir.org/v1/issues/2024?page=1&perPage=1000'
soup=get_soup(url)
data=json.loads(soup.text)["results"]
print(len(data))
for i in data:
    title=i["title"]
    print(title)




