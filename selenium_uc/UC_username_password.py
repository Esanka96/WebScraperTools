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
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver
chromedriver.install()

url='https://www.ajronline.org/'
options = uc.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--incognito')

driver = uc.Chrome(options=options)
driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
login_link="https://www.ajronline.org"+soup.find("a",class_="loginBar__username")["href"]
driver.get(login_link)

username_input = driver.find_element(By.ID, 'ctl01_TemplateBody_WebPartManager1_gwpciNewContactSignInCommon_ciNewContactSignInCommon_signInUserName')
username_input.send_keys('EB732976')

password_input = driver.find_element(By.ID, 'ctl01_TemplateBody_WebPartManager1_gwpciNewContactSignInCommon_ciNewContactSignInCommon_signInPassword')
password_input.send_keys('732976')

sign_in_button = driver.find_element(By.ID, 'ctl01_TemplateBody_WebPartManager1_gwpciNewContactSignInCommon_ciNewContactSignInCommon_SubmitButton')
sign_in_button.click()

current_url=None
while current_url!="https://www.ajronline.org/":
    current_url=driver.current_url
    time.sleep(1)

currentUrl="https://www.ajronline.org/toc/ajr/current"
driver.get(currentUrl)

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
print(soup)

driver.close()
driver.quit()








