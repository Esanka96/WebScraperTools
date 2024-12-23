import time
import requests
import cloudscraper
from bs4 import BeautifulSoup
import os
import re
from datetime import datetime
import pandas as pd

def getSoup(url):
    response = requests.get(url,headers=headers)
    soup= BeautifulSoup(response.content, 'html.parser')
    return soup

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "Sec-Ch-Ua-Arch": "\"x86\"",
    "Sec-Ch-Ua-Bitness": "\"64\"",
    "Sec-Ch-Ua-Full-Version": "\"126.0.6478.127\"",
    "Sec-Ch-Ua-Full-Version-List": "\"Not/A)Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"126.0.6478.127\", \"Google Chrome\";v=\"126.0.6478.127\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Model": "\"\"",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Ch-Ua-Platform-Version": "\"15.0.0\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

url="https://recyt.fecyt.es/index.php/RLM/issue/archive"

print(getSoup(url))




