import requests
from selenium import webdriver
from bs4 import BeautifulSoup

def get_cookies():
    options=webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome()
    driver.get("https://recyt.fecyt.es/index.php/AEDIP/login?source=%2Findex.php%2FAEDIP%2Findex")
    username_input = driver.find_element("id", "username")
    password_input = driver.find_element("id", "password")
    username_input.send_keys("eselvier-aedipr")
    password_input.send_keys("eselvier")
    login_button = driver.find_element("xpath", "//button[@class='submit' and @type='submit']")
    login_button.click()
    driver.implicitly_wait(5)
    cookies = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in driver.get_cookies()])
    driver.quit()
    return cookies

cookies=get_cookies()


headers = {
    "Cookie": f"{cookies}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
}

new_response=requests.get('https://recyt.fecyt.es/index.php/AEDIP/issue/archive',headers=headers)
soup=BeautifulSoup(new_response.content,'html.parser')
print(soup)

