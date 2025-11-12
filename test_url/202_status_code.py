import json
import time
import requests
# import cloudscraper
from bs4 import BeautifulSoup
import re
from datetime import datetime
import certifi

def getSoup(url):
    response = requests.get(url,headers=headers)
    print(response.status_code)
    soup= BeautifulSoup(response.content, 'html.parser')
    return soup

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "cookie": "",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}

url = "https://journals.ametsoc.org/view/journals/mwre/152/4/mwre.152.issue-4.xml"

#
# with open("url.txt","r",encoding="utf-8") as file:
#     url = file.read().strip().splitlines()[0]

current_soup = getSoup(url)

#print(current_soup)





