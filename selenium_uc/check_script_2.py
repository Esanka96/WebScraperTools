import re
import requests
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

session = requests.session()
chromedriver.install()
#options.add_argument('--headless')
# options.add_argument('--incognito')
# options.add_argument('--disable-gpu')
# options.add_argument('--disable-software-rasterizer')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-infobars')
# options.add_argument('--disable-extensions')
# options.add_argument('--disable-popup-blocking')
for i in range(10):
    options = uc.ChromeOptions()
    #options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-software-rasterizer')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36')

    driver = uc.Chrome(options=options)
    def get_cookies(url):
        driver.get(url)
        #time.sleep(50)

        time.sleep(5)

        count = 0
        max_count = 40

        while count < max_count:
            if BeautifulSoup(driver.page_source, "html.parser").find("footer", class_="bootstrap"):
                break
            time.sleep(5)
            count += 1

        print(driver.page_source)
        #time.sleep(10)

        cookies = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in driver.get_cookies()])
        driver.close()
        driver.quit()
        return cookies

    def get_soup(url):
        response = session.get(url,headers=headers)
        soup= BeautifulSoup(response.content, 'html.parser')
        return soup

    first_url = "https://www.justice.gc.ca/eng/"

    driver.get(first_url)
    #time.sleep(10)

    Article_link = 'https://www.canlii.org/'

    cookies=get_cookies(Article_link)

    #time.sleep(30)
    #cookies=get_cookies("https://www.canlii.org/en/sk/laws/regu/rrs-c-s-15.1-reg-10/latest/rrs-c-s-15.1-reg-10.html")
    #time.sleep(15)
    print(cookies)

    headers = {
        "Cookie": f"{cookies}",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Referer":"https://www.canlii.org/",
        "Pragma": "no-cache",
        "Priority": "u=0, i",
        "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "Sec-Ch-Ua-Arch": "\"x86\"",
        "Sec-Ch-Ua-Bitness": "\"64\"",
        "Sec-Ch-Ua-Full-Version": "\"126.0.6478.127\"",
        "Sec-Ch-Ua-Full-Version-List": "\"Not/A)Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"126.0.6478.127\", \"Google Chrome\";v=\"126.0.6478.127\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Model": "\"\"",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Ch-Ua-Platform-Version": "\"15.0.0\"",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }

    url='https://www.canlii.org/'
    soup = get_soup(url)

    #time.sleep(20)
    url2 = "https://www.canlii.org/en/sk/laws/regu/rrs-c-s-15.1-reg-10/latest/rrs-c-s-15.1-reg-10.html"
    soup2 = get_soup(url2)
    print(soup2)
    #time.sleep(25)
    pdf_link = "https://www.canlii.org"+soup2.find("a",attrs={"id":"pdf-link"})["href"]

    pdf_content = session.get(pdf_link,headers=headers).content
    with open(f"Out_{i+1}.pdf", 'wb') as file:
        file.write(pdf_content)






