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

# request_cookies = {
#     "ci_session": "sc6nkagk2k928rn21adpbljeo6o9pisi",
#     "_gid": "GA1.2.1513321116.1760004491",
#     "_gat_gtag_UA_148594354_1": "1",
#     "_ga_HNJ983YT3Y": "GS2.1.s1760004491$o2$g1$t1760004536$j15$l0$h0",
#     "_ga": "GA1.1.1433030013.1758260779"
# }

request_cookies = {
    'IWA_PublishingMachineID': '638491186796925668',
    '_ga': 'GA1.2.892686197.1713521884',
    '_gid': 'GA1.2.1313269268.1713521884',
    'fpestid': 'eh9u8XUlgdwuY7RUwBCYJv4NZVGOKeP548CWt1y_bFcLNWRt7tUehqHRQCwwsjI1bzLnNw',
    '_cc_id': 'c98eea9794bffe9e84dcd4916e261382',
    'panoramaId_expiry': '1714126683937',
    'panoramaId': '87bb27088c11dbcbf1612371515e16d53938c438922298f84a6f843eb4291467',
    'panoramaIdType': 'panoIndiv',
    'hum_iwap_visitor': '98fc3c8c-f2ea-4750-8fe8-42302f336a62',
    '__stripe_mid': 'debea6e4-2d7d-4d84-aeb3-37410dc7dbe192f50c',
    'IWA_SessionId': 'b0y5gtz4zk0y0gh5xrgouqwm',
    '__stripe_sid': 'f79e02a8-ef2f-4a96-9c7b-3381a4c74abd83cdba',
    '_gat_UA-10590794-3': '1',
    '_gat_UA-76340245-2': '1',
    '_ga_CY814T2KFP': 'GS1.2.1713550821.2.1.1713551342.60.0.0'
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

url = "https://pdfcoffee.com/np0017962014-pt-unlocked-pdf-free.html"

current_soup=use_drive(url,request_cookies)