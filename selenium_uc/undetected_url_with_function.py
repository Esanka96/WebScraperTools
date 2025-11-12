from bs4 import BeautifulSoup
import time
import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver
chromedriver.install()

url="https://projecteuclid.org/journals/journal-of-commutative-algebra/current"

def initiate_driver():
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
            options.add_argument(f'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36')

            driver = uc.Chrome(options=options)
            return driver

        except:
            if not check < 4:
                raise Exception("Error in driver")
            check += 1

def get_content_from_captcha(url):
    driver.get(url)

    time.sleep(5)

    count = 0
    max_count = 10

    while count < max_count:
        if BeautifulSoup(driver.page_source, "html.parser").find("div", class_="flex flexHCenter"):
            break
        time.sleep(1)
        count += 1

    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def quit_driver():
    driver.close()
    driver.quit()


driver = initiate_driver()
get_content_from_captcha(url)
quit_driver()






