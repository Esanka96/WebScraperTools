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
    "_gid": "GA1.3.900864029.1755590555",
    "waap_id": "HYCbhqZVaTdRZZUQFKS72ECQqfbnLecv2ry1V9gujbc39OW9dqL8wWQKm66/E4BCrxxi1My/3tFKStCLtHdcGSDkt27pos0rRwYAnZgql3GjAz/PDnDd10Ls3VI7t/aHqV9M2wsGH2/ZJ3lCEZBDxfcMLmXEb8itlZogHpxIRTbtb4o5/JBmCZOMBxGqE060fRGFkmwsknEJZQ0PAmVs6ckQTJJf/qouCt5jjbchyriSkdtV36sKI8/EbqtESQPq7cYJ62AEUvyt7FqBVJTCDwXJ9DtFNRrYvBI_",
    "deviceChannel": "Default",
    "_gat": "1",
    "_ga_F5VXQ9Z7N5": "GS2.1.s1755837936$o11$g0$t1755837936$j60$l0$h0",
    "_ga": "GA1.1.824627959.1754379508",
    "WSS_FullScreenMode": "false"
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

url = "https://main.knesset.gov.il/pages/default.aspx"

current_soup=use_drive(url,request_cookies)