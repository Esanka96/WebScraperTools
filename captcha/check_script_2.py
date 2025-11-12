import os
import re
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver
import random

request_cookies = {
    "cookieConsent": "ALL",
    "sp": "45d06899-d316-4bf8-999e-b654d410c396",
    "_pk_id.1.b39f": "04c102f9cd33a177.1752846601.",
    "userLocale": "en",
    "localeChangeDate": "2025-07-18T15:36:24.874Z",
    "expandResults": "true",
    "framedResults": "false",
    "_sp_ses.5ade": "*",
    "_pk_ses.1.b39f": "1",
    "datadome": "QtHz98At5660F~TsDr8VXoU1Bf3Y8Rli39hh1T0Arr6WhFDmoHakfsDe3~nofGcfgt24lp1Iprbbxn4jRGjXLJU9SuQZJ59hhzSpk1GMsaMIk8f9Xce_atJcuEtI3LfU",
    "lexbox-api.jsessionid": "89DC138D0C9CEF3E2383FB0F492D0F6A",
    "_sp_id.5ade": "f539729b-6b02-4386-a8e5-d4513c0303b7.1751382144.6.1760543758.1760539855.2b40eff6-6867-4376-917d-43fa6fee7375.d31dc1b7-7c4f-4788-a5f0-99e167921786.5b91788f-f6c0-46b1-a66c-42bb2bc43027.1760543440263.3"
}

def use_drive(url,request_cookies):
    driver.get(url)
    time.sleep(5)
    for cookie_name, cookie_value in request_cookies.items():
        driver.add_cookie({"name": cookie_name, "value": cookie_value})

    driver.get(url)
    time.sleep(5)
    content = driver.page_source
    uc_soup = BeautifulSoup(content, 'html.parser')
    return uc_soup

check = 0
while check < 10:
    try:
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'

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
        options.add_argument('--window-size=1920,1080')
        options.add_argument(f'--user-agent={user_agent}')

        driver = uc.Chrome(options=options)

        check = 10
    except:
        if not check < 9:
            message = "Error in the Chrome driver. Please update your Google Chrome version."
            print(message)
        check += 1

url = "https://www.canlii.org/"

current_soup=use_drive(url,request_cookies)