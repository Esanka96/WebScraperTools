import re
import requests
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import time
import os
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import pandas as pd
import chromedriver_autoinstaller as chromedriver
import json

session = requests.session()
chromedriver.install()

download_dir = os.path.join(os.getcwd(), "downloads")

if not os.path.exists(download_dir):
    os.makedirs(download_dir)

for i in range(10):
    options = uc.ChromeOptions()
    #options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--disable-software-rasterizer')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-infobars')
    # options.add_argument('--disable-extensions')
    # options.add_argument('--disable-popup-blocking')
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36')

    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True,
        "plugins.plugins_disabled": ["Chrome PDF Viewer"]
    }
    options.add_experimental_option("prefs", prefs)

    driver = uc.Chrome(options=options, version_main=141)


    def get_cookies(url):
        driver.get(url)
        time.sleep(5)

        count = 0
        max_count = 40

        while count < max_count:
            if BeautifulSoup(driver.page_source, "html.parser").find("footer", class_="bootstrap"):
                break
            time.sleep(5)
            count += 1

        try:
            accept_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "understandCookieConsent"))
            )
            accept_button.click()
            time.sleep(5)
            print("✅ Cookie consent accepted!")
        except Exception as e:
            print("⚠️ Could not find or click cookie button:", e)

        cookies = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in driver.get_cookies()])
        # driver.close()
        # driver.quit()
        return cookies

    def get_soup(url):
        response = session.get(url,headers=headers)
        soup= BeautifulSoup(response.content, 'html.parser')
        return soup

    first_url = "https://www.justice.gc.ca/eng/"

    driver.get(first_url)

    Article_link = 'https://www.canlii.org/'

    cookies=get_cookies(Article_link)

    driver.get("https://www.canlii.org/en/sk/laws/regu/rrs-c-s-15.1-reg-10/latest/rrs-c-s-15.1-reg-10.html")

    driver.get("https://www.canlii.org/en/sk/laws/regu/rrs-c-s-15.1-reg-10/latest/rrs-c-s-15.1-reg-10.pdf")
    time.sleep(10)

    driver.close()
    driver.quit()

    # headers = {
    #     "Cookie": f"{cookies}",
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    #     "Accept-Encoding": "gzip, deflate, br, zstd",
    #     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    #     "Cache-Control": "no-cache",
    #     "Referer":"https://www.canlii.org/",
    #     "Pragma": "no-cache",
    #     "Priority": "u=0, i",
    #     "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    #     "Sec-Ch-Ua-Arch": "\"x86\"",
    #     "Sec-Ch-Ua-Bitness": "\"64\"",
    #     "Sec-Ch-Ua-Full-Version": "\"126.0.6478.127\"",
    #     "Sec-Ch-Ua-Full-Version-List": "\"Not/A)Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"126.0.6478.127\", \"Google Chrome\";v=\"126.0.6478.127\"",
    #     "Sec-Ch-Ua-Mobile": "?0",
    #     "Sec-Ch-Ua-Model": "\"\"",
    #     "Sec-Ch-Ua-Platform": "\"Windows\"",
    #     "Sec-Ch-Ua-Platform-Version": "\"15.0.0\"",
    #     "Sec-Fetch-Dest": "document",
    #     "Sec-Fetch-Mode": "navigate",
    #     "Sec-Fetch-Site": "none",
    #     "Sec-Fetch-User": "?1",
    #     "Upgrade-Insecure-Requests": "1",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    # }
    #
    # url='https://www.canlii.org/'
    # soup = get_soup(url)
    #
    # url2 = "https://www.canlii.org/en/sk/laws/regu/rrs-c-s-15.1-reg-10/latest/rrs-c-s-15.1-reg-10.html"
    # soup2 = get_soup(url2)
    #
    # pdf_link = "https://www.canlii.org"+soup2.find("a",attrs={"id":"pdf-link"})["href"]
    #
    # pdf_content = session.get(pdf_link,headers=headers).content
    # with open(f"Out_{i+1}.pdf", 'wb') as file:
    #     file.write(pdf_content)






