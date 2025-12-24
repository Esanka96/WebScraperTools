import time
import cloudscraper
import requests
from bs4 import BeautifulSoup
import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
warnings.simplefilter("ignore")

import undetected_chromedriver as uc

class WebCloudScraper:
    def __init__(self, headers=None, timeout=30):
        self.headers = headers or {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Priority": "u=0, i",
            "Sec-Ch-Ua-Arch": '"x86"',
            "Sec-Ch-Ua-Bitness": '"64"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Model": '""',
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Ch-Ua-Platform-Version": '"15.0.0"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
        }
        self.timeout = timeout
        self.verify = True

        self.session = None
        self.cloud_session = None
        self.driver = None

        self.create_new_session()
        self.create_new_cloud_session()

    def create_new_session(self):
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def create_new_cloud_session(self):
        self.cloud_session = cloudscraper.create_scraper()
        self.cloud_session.headers.update(self.headers)

    def handle_response(self,response):
        content_type = response.headers.get("Content-Type", "").lower()
        if "json" in content_type:
            return response.json()
        else:
            return BeautifulSoup(response.content, "html.parser")

    def get_soup(self, url, headers=None,timeout=None,verify=None, max_retries=10, delay=3):
        print("⏳ Fetching data using Request...")
        headers = self.headers if headers is None else headers
        timeout = self.timeout if timeout is None else timeout
        verify = self.verify if verify is None else verify

        for attempt in range(1, max_retries + 1):
            try:
                response = self.session.get(url, headers=headers,timeout=timeout,verify=verify)
                response.raise_for_status()
                print("✅ Request successful; content obtained")
                return self.handle_response(response)
            except Exception as e:
                print(f"⚠️ Attempt {attempt} failed: {e}")
                if attempt == max_retries:
                    raise Exception(f"⚠️ Request failed to fetch data")
                time.sleep(delay)

    def post_soup(self, url, data=None, json=None, headers=None, timeout=None, verify=None, max_retries=10, delay=3):
        headers = self.headers if headers is None else headers
        timeout = self.timeout if timeout is None else timeout
        verify = self.verify if verify is None else verify

        for attempt in range(1, max_retries + 1):
            try:
                response = self.session.post(url,data=data,json=json,headers=headers,timeout=timeout,verify=verify)
                response.raise_for_status()
                print("✅ Request successful; content obtained")
                return self.handle_response(response)
            except Exception as e:
                print(f"⚠️ Attempt {attempt} failed: {e}")
                if attempt == max_retries:
                    raise Exception(f"⚠️ Post request failed to fetch data")
                time.sleep(delay)

    def get_cloudscraper_soup(self, url, headers=None,timeout=None,verify=None, max_retries=10, delay=3):
        print("⏳ Fetching data using CloudScraper...")
        headers = self.headers if headers is None else headers
        timeout = self.timeout if timeout is None else timeout
        verify = self.verify if verify is None else verify

        for attempt in range(1, max_retries + 1):
            try:
                response = self.cloud_session.get(url, headers=headers,timeout=timeout,verify=verify)
                response.raise_for_status()
                print("✅ CloudScraper successfully retrieved content")
                return self.handle_response(response)
            except Exception as e:
                print(f"⚠️ Attempt {attempt} failed: {e}")
                if attempt == max_retries:
                    raise Exception(f"⚠️ CloudScraper failed to fetch data")
                time.sleep(delay)

    def post_cloudscraper_soup(self, url, data=None, json=None, headers=None, timeout=None, verify=None, max_retries=10, delay=3):
        headers = self.headers if headers is None else headers
        timeout = self.timeout if timeout is None else timeout
        verify = self.verify if verify is None else verify

        for attempt in range(1, max_retries + 1):
            try:
                response = self.cloud_session.post(url,data=data,json=json,headers=headers,timeout=timeout,verify=verify)
                response.raise_for_status()
                print("✅ CloudScraper successfully retrieved content")
                return self.handle_response(response)
            except Exception as e:
                print(f"Attempt {attempt} failed: {e}")
                if attempt == max_retries:
                    raise Exception(f"⚠️ CloudScraper failed to fetch data")
                time.sleep(delay)

    def get_undetected_soup(self, url,max_wait_time = 200):
        print("⏳ Fetching data using Undetected ChromeDriver...")
        self.init_driver()

        self.cloudflare_resolve(url,max_wait_time)

        html = self.driver.page_source
        print("✅ Undetected ChromeDriver successfully retrieved content")
        return BeautifulSoup(html, "html.parser")

    def get_cookie_from_driver(self):
        try:
            if not self.driver:
                print("⚠️ Cookie search failed")
                return None

            cookies = self.driver.get_cookies()
            cookie_header = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
            return cookie_header
        except Exception as error:
            raise Exception(f"⚠️ Failed to retrieve cookie")

    def cookie_update_undetected(self, url,max_wait_time = 200):
        print("⏳ Fetching cookie using Undetected ChromeDriver...")
        self.init_driver()

        self.cloudflare_resolve(url,max_wait_time)

        self.cookie_for_driver()
        print("✅ Cookie captured successfully")

    def cookie_update_undetected_with_click(self, url,max_wait_time = 200):
        print("⏳ Fetching cookie using Undetected ChromeDriver(Click Method)...")
        self.init_driver()

        self.cloudflare_resolve_with_click(url,max_wait_time)

        self.cookie_for_driver()
        print("✅ Cookie captured successfully")

    def cookie_for_driver(self):
        try:
            if not self.driver:
                print("⚠️ Cookie search failed")
                return None

            cookies = self.driver.get_cookies()
            cookie_dict = {cookie["name"]: cookie["value"] for cookie in cookies}

            self.session.cookies.clear()
            self.cloud_session.cookies.clear()

            self.session.cookies.update(cookie_dict)
            self.cloud_session.cookies.update(cookie_dict)

            print("✅ Cloudflare cookies updated")
        except Exception as error:
            raise Exception(f"⚠️ Failed to retrieve cookie")

    def init_driver(self):
        self.create_new_session()
        self.create_new_cloud_session()

        if self.driver is None:
            user_agent = self.get_user_agent()

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
                    options.add_argument('--window-size=1920,1080')
                    options.add_argument(f'--user-agent={user_agent}')
                    self.driver = uc.Chrome(options=options)

                    check = 5
                except:
                    if not check < 4:
                        message = "⚠️ Undetected_chrome driver issue detected"
                        print(message)
                        raise Exception(f"{message}")
                    check += 1

    def cloudflare_resolve(self,url,max_wait_time):
        try:
            self.driver.get(url)
            time.sleep(5)

            count = 0
            max_count = int(max_wait_time/5)
            cloudflare_resolved = False

            while count < max_count:
                soup = BeautifulSoup(self.driver.page_source, "html.parser")
                title = soup.title.string.strip() if soup.title else ""

                remaining_seconds = (max_count - count) * 5
                print(
                    f"\r⏳ Waiting for Cloudflare challenge to pass... "
                    f"{remaining_seconds}s remaining",
                    end="",
                    flush=True
                )

                if "Just a moment" not in title:
                    print("\r✅ Cloudflare challenge passed successfully!            ")
                    time.sleep(5)
                    cloudflare_resolved = True
                    break

                time.sleep(5)
                count += 1

            if not cloudflare_resolved:
                message = "⚠️ Undetected ChromeDriver unable to bypass Cloudflare"
                raise Exception(message)

        except Exception as error:
            message = "⚠️ Undetected ChromeDriver unable to bypass Cloudflare"
            raise Exception(f"{message}")

    def cloudflare_resolve_with_click(self,url,max_wait_time):
        try:
            self.driver.get(url)
            time.sleep(10)
            x, y = 525, 290

            actions = ActionChains(self.driver)
            actions.move_by_offset(x, y).click().perform()
            time.sleep(5)

            count = 0
            max_count = int(max_wait_time/5)
            cloudflare_resolved = False

            while count < max_count:
                soup = BeautifulSoup(self.driver.page_source, "html.parser")
                title = soup.title.string.strip() if soup.title else ""

                remaining_seconds = (max_count - count) * 5
                print(
                    f"\r⏳ Waiting for Cloudflare challenge to pass... "
                    f"{remaining_seconds}s remaining",
                    end="",
                    flush=True
                )

                if "Just a moment" not in title:
                    print("\r✅ Cloudflare challenge passed successfully!            ")
                    time.sleep(5)
                    cloudflare_resolved = True
                    break

                time.sleep(5)
                count += 1

            if not cloudflare_resolved:
                message = "⚠️ Failed to resolve Cloudflare using the Undetected ChromeDriver click method"
                raise Exception(message)
        except Exception as error:
            message = "⚠️ Failed to resolve Cloudflare using the Undetected ChromeDriver click method"
            raise Exception(f"{message}")

    def get_user_agent(self):
        try:
            import chromedriver_autoinstaller as chromedriver
            chromedriver.install()

            options = uc.ChromeOptions()
            options.add_argument(f"--headless=new")
            driver = uc.Chrome(options=options)
            driver.get("https://www.example.com")
            user_agent = driver.execute_script("return navigator.userAgent;")
            driver.close()
            driver.quit()

            self.headers["User-Agent"] = user_agent.replace("Headless", "")
            self.session.headers.update({"User-Agent": self.headers["User-Agent"]})
            self.cloud_session.headers.update({"User-Agent": self.headers["User-Agent"]})

            return user_agent.replace("Headless","")
        except:
            message = "⚠️ Undetected_chrome driver issue detected"
            print(message)
            raise Exception(f"{message}")

    def driver_close(self):
        if self.driver:
            self.driver.close()
            self.driver.quit()
            self.driver = None
