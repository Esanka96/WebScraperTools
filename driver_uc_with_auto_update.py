import time
import os
import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver
chromedriver.install()

driver = None

def initiate_driver():
    global driver
    check = 0
    while check < 10:
        try:
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'

            options = uc.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--incognito')
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-software-rasterizer')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-infobars')
            options.add_argument('--disable-extensions')
            options.add_argument('--disable-popup-blocking')
            options.add_argument('--window-size=1920,1080')
            options.add_argument(f'--user-agent={user_agent}')

            driver = uc.Chrome(options=options)

            print(driver.capabilities['chrome']['chromedriverVersion'])

            check = 10
        except:
            if not check < 9:
                message = "Error in the Chrome driver. Please update your Google Chrome version."
                error_list.append(message)
                common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,
                                                     len(completed_list),
                                                     ini_path, attachment, current_date, current_time, Ref_value)
            check += 1

initiate_driver()
