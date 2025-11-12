import time
from bs4 import BeautifulSoup
import requests
import pdfplumber
import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver
chromedriver.install()

url = "https://www.nhc.gov.cn/yzygj/c100068/202406/50e0b5ab36a745599fe2708b218edaff.shtml"


check = 0
while check < 5:
    try:
        options = uc.ChromeOptions()

        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-software-rasterizer')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-popup-blocking')
        options.add_argument(f'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36')

        driver = uc.Chrome(options=options)

        check = 5
    except:
        if not check < 4:
            message = "An error occurred in the Selenium driver."
        check += 1

try:
    driver.get(url)

    time.sleep(5)

    count = 0
    max_count = 40

    while count < max_count:
        if BeautifulSoup(driver.page_source, "html.parser").find("div",class_="footer"):
            break
        time.sleep(5)
        count += 1

    content = driver.page_source

    soup = BeautifulSoup(content, 'html.parser')
    print(soup)


    # cookies = driver.get_cookies()
    # cookie_header = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
    #
    # print(cookie_header)
    #
    # driver.close()
    # driver.quit()

except Exception as error:
    message = "Unable to bypass Cloudflare."
    print(message)
