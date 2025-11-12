import requests
import time
from bs4 import BeautifulSoup
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
        driver.close()

api_key = "a03589ed562de14589af1d772c2b41bb"

url='https://journals.biologists.com/jeb/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
response_code = response.status_code
main_soup = BeautifulSoup(response.content, 'html.parser')

data_site_key = main_soup.find("div", {"id": "captcha"})["data-captchakey"]
request_url = "http://2captcha.com/in.php?key=" + str(api_key) + "&method=userrecaptcha&googlekey=" + str(
    data_site_key) + "&pageurl=" + url + ""
page = requests.get(request_url)
ok_key = str(page.text).replace("OK|", "")
print("resolving captcha key..")
respond_url = "http://2captcha.com/res.php?key=" + str(api_key) + "&action=get&id=" + str(ok_key) + ""

time.sleep(15)
page = requests.get(respond_url).text
while str(page).__contains__("CAPCHA_NOT_READY"):
    print("captcha still not ready..")
    time.sleep(10)
    page = requests.get(respond_url).text
code = str(page).replace("OK|", "")
time.sleep(2)

data = {
    "g-recaptcha-response": code,
}

response = requests.post(url, data=data, headers=headers)
soup,cookies = get_driver_content(url)
print(soup)