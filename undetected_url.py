import re
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import time
import os
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import pandas as pd
import chromedriver_autoinstaller as chromedriver
import json

#chromedriver.install()

def get_driver_content(url):
    options = uc.ChromeOptions()
    #options.add_argument('--headless')
    options.add_argument('--incognito')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-software-rasterizer')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-popup-blocking')
    #options.add_argument('--user-agent=YOUR_USER_AGENT_STRING')
    options.add_argument('--version_main=108')

    driver = uc.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(10)
        content = driver.page_source
        cookies = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in driver.get_cookies()])
        soup = BeautifulSoup(content, 'html.parser')
        return soup,cookies
    finally:
        driver.close()

url='https://iwaponline.com/wst/issue'
soup,cookies = get_driver_content(url)
# date=soup.find('div',class_='volume_box')
#print(soup)





