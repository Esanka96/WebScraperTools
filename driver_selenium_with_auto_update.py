import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = None

def initiate_driver():
    global driver
    check = 0
    while check < 5:
        try:
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'

            options = Options()
            options.add_argument('--headless=new')  # New headless mode for better compatibility
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-software-rasterizer')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-infobars')
            options.add_argument('--disable-extensions')
            options.add_argument('--disable-popup-blocking')
            options.add_argument(f'--user-agent={user_agent}')

            # prefs = {
            #     "download.default_directory": os.path.abspath(temPdfOut),
            #     "download.prompt_for_download": False,
            #     "download.directory_upgrade": True,
            #     "safebrowsing.enabled": True
            # }
            # options.add_experimental_option('prefs', prefs)

            # Automatically update and get ChromeDriver path
            service = Service(ChromeDriverManager().install())

            # Start the WebDriver
            driver = webdriver.Chrome(service=service, options=options)

            check = 5  # Exit loop on success
            print(driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0])

        except Exception as e:
            if check >= 4:
                print(f"An error occurred in the Selenium driver: {e}")
            check += 1

initiate_driver()
