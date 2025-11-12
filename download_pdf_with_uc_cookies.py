from datetime import datetime
import os
import requests
from bs4 import BeautifulSoup
import time
import shutil

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# import undetected_chromedriver as uc
# import chromedriver_autoinstaller as chromedriver
# chromedriver.install()

out_path='Out'
if not os.path.exists(out_path):
    os.makedirs(out_path)
out_folder=os.path.join(out_path,'New.pdf')

url = "https://dlt.ri.gov/regulation-and-safety/occupational-safety/right-know-guidelines-employers-register"
pdf_link = "https://dlt.ri.gov/sites/g/files/xkgbur571/files/documents/pdf/wrs/HazardousABC.pdf"

# options = uc.ChromeOptions()
# options.add_argument('--disable-gpu')
# options.add_argument('--disable-software-rasterizer')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-infobars')
# options.add_argument('--disable-extensions')
# options.add_argument('--disable-popup-blocking')
# driver = uc.Chrome(options=options)


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'

options = webdriver.ChromeOptions()
#options.add_argument("--headless=new") # Run in headless mode (no UI)
options.add_argument("--disable-gpu")  # Disable GPU acceleration
options.add_argument("--no-sandbox")  # Disable sandboxing (useful in Linux)
options.add_argument("--window-size=1920,1080")  # Set window size
options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid detection
options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Remove automation flag
options.add_experimental_option("useAutomationExtension", False)


driver = webdriver.Chrome(options=options)



driver.get(url)
print("Wait until the PDF is downloaded")

time.sleep(5)

count = 0
max_count=20

while count<max_count:
    if BeautifulSoup(driver.page_source,"html.parser").find("div",class_="qh__site-branding"):
        break
    time.sleep(5)
    count += 1

cookies = driver.get_cookies()
cookie_header = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])

pdf_headers = {
    "cookie": cookie_header,

}

print(cookie_header)

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
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}


response = requests.get(pdf_link, headers=headers)
with open(out_folder, 'wb') as f:
    f.write(response.content)


print("PDF file has been successfully downloaded")

driver.close()
driver.quit()