from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

options = Options()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
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

driver = webdriver.Chrome(options=options)

driver.get("https://www.canlii.org/")

time.sleep(10)

content = driver.page_source

soup = BeautifulSoup(content,"html.parser")

print(soup)

driver.close()
driver.quit()
