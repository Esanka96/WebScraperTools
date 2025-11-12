import time

from bs4 import BeautifulSoup
import undetected_chromedriver as uc

def get_driver_content(url, cookies):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
    options = uc.ChromeOptions()
    # options.add_argument('--headless')
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
    driver.get(url)
    time.sleep(5)
    for cookie_name, cookie_value in cookies.items():
        driver.add_cookie({"name": cookie_name, "value": cookie_value})

    driver.get(url)
    time.sleep(5)
    content = driver.page_source
    cookies = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in driver.get_cookies()])

    driver.close()
    driver.quit()
    soup = BeautifulSoup(content, 'html.parser')
    return soup, cookies

cookie = {
    "cookieConsent": "ALL",
    "sp": "45d06899-d316-4bf8-999e-b654d410c396",
    "_pk_id.1.b39f": "04c102f9cd33a177.1752846601.",
    "_sp_ses.5ade": "*",
    "_pk_ses.1.b39f": "1",
    "userLocale": "en",
    "localeChangeDate": "2025-07-18T15:36:24.874Z",
    "COPID": "WG44q5eJ5IkRm_zjpGufwaV_p5GVFVHwxYOgTGHsGkKtNiI4IJ7rNIw5d4u1eS3gFpLEORcbD09ONoUTVWgLww==",
    "datadome": "y4QbTcauKGcHkfkk3RW_DzHTJOdrhlBcd~eSwD3U6m1APYLJ3m7C96BSeQ4k8UcLaLTu88Ktd2N9DWy9d6bgjisJCeaRTinyWGJq2wchr~O_4u3rN6C6eGnaCWIDXtRU",
    "_sp_id.5ade": "f539729b-6b02-4386-a8e5-d4513c0303b7.1751382144.3.1752853874.1752846616.188d4d1c-4386-4395-98ef-ef3515b2f50d.31f4ff08-4218-4b02-8677-13335ecfe8f3.2c9c634c-790c-4e13-b992-7ab47f69ddb4.1752852446063.17"
}


url='https://www.canlii.org/en/sk/laws/regu/rrs-c-s-15.1-reg-10/latest/rrs-c-s-15.1-reg-10.html'
soup, cookies = get_driver_content(url, cookie)
print(soup.find("div",attrs={"id":"title-container"}).get_text(strip=True))







