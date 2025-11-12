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

url = "https://projecteuclid.org/"


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
            errors.append(message)
        check += 1

try:
    driver.get(url)

    time.sleep(5)

    count = 0
    max_count = 40

    while count < max_count:
        if BeautifulSoup(driver.page_source, "html.parser").find("a",string="Advanced Search"):
            break
        time.sleep(5)
        count += 1

    cookies = driver.get_cookies()
    cookie_header = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])


    driver.close()
    driver.quit()

except Exception as error:
    message = "Unable to bypass Cloudflare."
    print(message)
    errors.append(message)

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "cookie": cookie_header,
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup)
