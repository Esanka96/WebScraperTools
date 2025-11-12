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
    ]
#formatted_proxies = [{'http': f'http://{proxy.split(":")[2]}:{proxy.split(":")[3]}@{proxy.split(":")[0]}:{proxy.split(":")[1]}'} for proxy in proxies_list]

formatted_proxies = []
for proxy in proxies_list:
    ip, port, user, password = proxy.split(':')
    formatted_proxy = f'http://{user}:{password}@{ip}:{port}'
    formatted_proxies.append({'http': formatted_proxy, 'https': formatted_proxy})

def get_random_proxy():
    return random.choice(formatted_proxies)

def get_soup(url):
    res = requests.get(url, proxies=get_random_proxy(), headers=headers)
    soup = BeautifulSoup(res.content, "html.parser")
    return soup

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "cookie": "_gid=GA1.1.824627959.1754379508;",
              #"waap_id=DGv/+xn0iZnMDdfBjQYq93eTpPoq472z3+iX9XyBFojOiNcJY6IdYwaVlrixyVqPYdcRgnFqsf+LjbWwzuDB2B0KKh7CcCpFg2t8vIJj34F7wuheyz38DAEPmwa14it5noS+ZQiCItOCdy5OUOTLq6IpAry3LQuTR8j06VcgHxaAD2MAolfS7bJYdmPJr2swQ2pKChdH5HMhxk6/YM5zHO8nTMDw1g73ypAF2nkUNKoj1AGq2NvNW2a1VLD8jpMAIdGPBhB/yG39RYxvh9T4B9+bHiWS+JcFzBI_;",
              #"deviceChannel=Default;",
              #"_gat=1;",
              #"_ga_F5VXQ9Z7N5=GS2.1.s1755763851$o10$g0$t1755763851$j60$l0$h0;",
              #"_ga=GA1.1.824627959.1754379508; ",
              #"WSS_FullScreenMode=false",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://main.knesset.gov.il/pages/default.aspx",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}

url='https://main.knesset.gov.il/pages/default.aspx'
soup=get_soup(url)
print(soup)


