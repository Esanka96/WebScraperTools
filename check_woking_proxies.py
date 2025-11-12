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
    "141.98.155.137:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "2.58.80.143:3199:mariyarathna-dh3w3:IxjkW0fdJy",
]

#formatted_proxies = [{'http': f'http://{proxy.split(":")[2]}:{proxy.split(":")[3]}@{proxy.split(":")[0]}:{proxy.split(":")[1]}'} for proxy in proxies_list]

formatted_proxies = []
for proxy in proxies_list:
    ip, port, user, password = proxy.split(':')
    formatted_proxy = f'http://{user}:{password}@{ip}:{port}'
    formatted_proxies.append({'http': formatted_proxy, 'https': formatted_proxy})

def get_random_proxy():
    return random.choice(formatted_proxies)

def get_soup(url,i):
    pdf_content = requests.get(url, proxies=i, headers=headers).content
    #pdf_content = BeautifulSoup(requests.get(url, proxies=get_random_proxy(), headers=headers,verify=False).content,"html.parser")
    return pdf_content

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

url='https://www.google.com/'

for i in formatted_proxies:
    try:
        soup=get_soup(url,i)
        print("work!")
    except:
        print(i)


