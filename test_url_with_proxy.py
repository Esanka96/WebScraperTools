import requests
from bs4 import BeautifulSoup
import os
import re
from datetime import datetime
import pandas as pd
import random
import time

proxies_list = [
    "185.205.199.161:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "216.10.5.126:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "185.207.96.233:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "67.227.121.110:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "67.227.127.100:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "181.177.76.122:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "185.207.97.85:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "186.179.21.77:3199:mariyarathna-dh3w3:IxjkW0fdJy",
]

formatted_proxies = [{'http': f'http://{proxy.split(":")[2]}:{proxy.split(":")[3]}@{proxy.split(":")[0]}:{proxy.split(":")[1]}'} for proxy in proxies_list]

def get_random_proxy():
    return random.choice(formatted_proxies)

def get_soup(url):
    pdf_content = requests.get(url, proxies=get_random_proxy(), headers=headers).content
    #pdf_content = BeautifulSoup(requests.get(url, proxies=get_random_proxy(), headers=headers,verify=False).content,"html.parser")
    return pdf_content

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

url='http://www.aest.org.cn/CN/1000-6931/home.shtml'
soup=get_soup(url)
print(soup)


