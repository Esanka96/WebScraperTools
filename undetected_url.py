import re
from bs4 import BeautifulSoup
import captcha_main
import time
import os
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import pandas as pd
import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver
chromedriver.install()

url='https://academic.oup.com/g3journal/article/14/10/jkae153/7712987'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
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
options.add_argument('--version_main=108')

driver = uc.Chrome(options=options)
for i in range(100):
    driver.get(url)
#time.sleep(40)
# content = driver.page_source
# soup = BeautifulSoup(content, 'html.parser')
# driver.close()
# driver.quit()
#
# print(soup)






