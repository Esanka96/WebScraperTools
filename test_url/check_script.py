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
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "experimentalFeaturesActivated=false; AWSALBAPP-1=_remove_; AWSALBAPP-2=_remove_; AWSALBAPP-3=_remove_;",
    "Host": "eur-lex.europa.eu",
    "Pragma": "no-cache",
    "Referer": "https://eur-lex.europa.eu/legal-content/IT/ALL/?uri=CELEX%3A32018R0914",
    "Sec-Ch-Ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"
}

url = "https://eur-lex.europa.eu/legal-content/IT/ALL/?uri=CELEX%3A32018R0914"

# with open("url.txt","r",encoding="utf-8") as file:
#     url = file.read().strip().splitlines()[0]

current_soup = getSoup(url)

print(current_soup)





