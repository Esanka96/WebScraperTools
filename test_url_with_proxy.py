import requests
from bs4 import BeautifulSoup
import os
import re
from datetime import datetime
import pandas as pd
import random
import time
import chromedriver_autoinstaller as chromedriver
import undetected_chromedriver as uc


chromedriver.install()

def get_driver_content(url):
    options = uc.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--incognito')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-software-rasterizer')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--version_main=108')

    driver = uc.Chrome(options=options)
    try:
        driver.get(url)
        content = driver.page_source
        cookies = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in driver.get_cookies()])
        soup = BeautifulSoup(content, 'html.parser')
        return soup,cookies
    finally:
        driver.close()

proxies_list = [
    "141.98.155.137:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "185.205.199.161:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "216.10.5.126:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "2.58.80.143:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "185.207.96.233:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "67.227.121.110:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "67.227.127.100:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "181.177.76.122:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "185.207.97.85:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "186.179.21.77:3199:mariyarathna-dh3w3:IxjkW0fdJy"
]

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
# }

formatted_proxies = []
for proxy in proxies_list:
    ip, port, user, password = proxy.split(':')
    formatted_proxy = f'http://{user}:{password}@{ip}:{port}'
    formatted_proxies.append({'http': formatted_proxy, 'https': formatted_proxy})

def get_random_proxy():
    return random.choice(formatted_proxies)

def get_soup(url):
    response = requests.get(url,proxies=get_random_proxy(),headers=headers)
    soup= BeautifulSoup(response.content, 'html.parser')
    print(soup)
    return soup

main_url="https://pubsonline.informs.org/"
current_soup,cookies=get_driver_content(main_url)
headers = {
    'Cookie': f"{cookies}",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

for i in range(1):
    try:
        url='https://www.utpjournals.press/toc/jcfs/current'

        soup=get_soup(url)
        print("Soup ok")
        soup2=get_soup(url2)
        print("Soup2 ok")
    except Exception as error:
        print(error)

