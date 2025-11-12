import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver
chromedriver.install()


url = "https://anvisalegis.datalegis.net/action/ActionDatalegis.php?acao=abrirTextoAto&link=S&tipo=RDC&numeroAto=00000974&seqAto=000&valorAno=2025&orgao=RDC/DC/ANVISA/MS&codTipo=&desItem=&desItemFim=&cod_modulo=134&cod_menu=9451"

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
        if BeautifulSoup(driver.page_source, "html.parser").find("form", attrs={"name":"formGerarLink"}):
            break
        time.sleep(5)
        count += 1

    content = driver.page_source

    soup = BeautifulSoup(content, 'html.parser')
    print(soup)

    cookies = driver.get_cookies()
    cookie_header = ";".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])

    driver.close()
    driver.quit()

except Exception as error:
    message = "Unable to bypass Cloudflare."
    print(message)


