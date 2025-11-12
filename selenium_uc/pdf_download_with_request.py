import time
from bs4 import BeautifulSoup
import requests
import pdfplumber
import pandas as pd

import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver
chromedriver.install()


url = "https://www.liverpooluniversitypress.co.uk/"

def getSoup(url):
    response = requests.get(url,headers=headers)
    print(response.status_code)
    soup= BeautifulSoup(response.content, 'html.parser')
    return soup

def get_user_agent():
    options = uc.ChromeOptions()
    options.add_argument(f"--headless=new")
    driver = uc.Chrome(options=options)
    driver.get("https://www.example.com")
    user_agent = driver.execute_script("return navigator.userAgent;")
    driver.close()
    driver.quit()

    return user_agent.replace("Headless","")

user_agent = get_user_agent()

check = 0
while check < 5:
    try:
        options = uc.ChromeOptions()

        #options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-software-rasterizer')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-popup-blocking')
        options.add_argument(f'--user-agent={user_agent}')

        driver = uc.Chrome(options=options)

        check = 5
    except:
        if not check < 4:
            message = "An error occurred in the Selenium driver."
        check += 1

try:
    driver.get(url)
    print("Wait until the PDF is downloaded")

    time.sleep(5)

    count = 0
    max_count = 40

    while count < max_count:
        if BeautifulSoup(driver.page_source, "html.parser").find("div", class_="footer__menu__row"):
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

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "cookie": cookie_header,
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"134.0.6998.36"',
    "sec-ch-ua-full-version-list": '"Chromium";v="134.0.6998.36", "Not:A-Brand";v="24.0.0.0", "Google Chrome";v="134.0.6998.36"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"15.0.0"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": user_agent
}

soup = getSoup(url)

print(soup)