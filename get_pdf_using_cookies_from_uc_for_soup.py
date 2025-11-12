import time
import os
import re
import requests
from bs4 import BeautifulSoup
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import pandas as pd
import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver

#chromedriver.install()

def get_soup(url):
    response = requests.get(url,headers=headers)
    soup= BeautifulSoup(response.content, 'html.parser')
    return soup

out_path='Out'
if not os.path.exists(out_path):
    os.makedirs(out_path)

def get_driver_content(url):
    options = uc.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-software-rasterizer')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--user-agent=YOUR_USER_AGENT_STRING')
    options.add_argument('--version_main=108')

    driver = uc.Chrome(options=options)
    try:
        driver.get(url)
        content = driver.page_source
        cookies = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in driver.get_cookies()])
        soup = BeautifulSoup(content, 'html.parser')
        return soup,cookies
    finally:
        time.sleep(2)
        driver.close()
        driver.quit()


url='https://spj.science.org/index/plantphenomics'
soup,cookies = get_driver_content(url)

headers = {
    'Cookie': f"{cookies}",
    #'User-Agent': 'YOUR_USER_AGENT_STRING'
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

last_url='https://spj.science.org/doi/10.34133/plantphenomics.0153'

new_soup=get_soup(last_url)
print(new_soup)