import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver
chromedriver.install()


url = "https://julkaisut.valtioneuvosto.fi/handle/10024/166152"
pdf_url = "https://julkaisut.valtioneuvosto.fi/bitstream/handle/10024/166152/STM_2025_5_J.pdf?sequence=1&isAllowed=y"

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

        options.add_argument('--headless')
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
    print("driver is loading.")

    time.sleep(5)

    count = 0
    max_count = 40

    while count < max_count:
        if BeautifulSoup(driver.page_source, "html.parser").find("div", class_="simple-item-view-rights table"):
            break
        time.sleep(5)
        count += 1

    content = driver.page_source

    soup = BeautifulSoup(content, 'html.parser')

    cookies = driver.get_cookies()
    cookie_header = ";".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])

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
    "cookie": f"{cookie_header}",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://julkaisut.valtioneuvosto.fi/handle/10024/166152",
    "sec-ch-ua": '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"140.0.7339.128"',
    "sec-ch-ua-full-version-list": '"Chromium";v="140.0.7339.128", "Not=A?Brand";v="24.0.0.0", "Google Chrome";v="140.0.7339.128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"15.0.0"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}

response = requests.get(pdf_url, headers=headers)

if response.status_code == 200:
    with open("STM_2025_5_J.pdf", "wb") as f:
        f.write(response.content)
    print("PDF downloaded successfully!")
else:
    print(f"Failed to download PDF. Status code: {response.status_code}")

