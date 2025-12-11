import requests
from bs4 import BeautifulSoup
import warnings
warnings.simplefilter("ignore")

class WebScraper:
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
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
        }
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.verify = True

    def get_soup(self, url, headers=None,timeout=None,verify=None):
        headers = self.headers if headers is None else headers
        timeout = self.timeout if timeout is None else timeout
        verify = self.verify if verify is None else verify

        try:
            response = self.session.get(url, headers=headers,timeout=timeout,verify=verify)
            response.raise_for_status()

            content_type = response.headers.get("Content-Type", "").lower()
            if "json" in content_type:
                return response.json()
            else:
                return BeautifulSoup(response.content, "html.parser")
        except Exception as e:
            raise Exception(f"Error in get_soup: {e}")

    def post_soup(self, url, data=None, json=None, headers=None, timeout=None, verify=None):
        headers = self.headers if headers is None else headers
        timeout = self.timeout if timeout is None else timeout
        verify = self.verify if verify is None else verify

        try:
            response = self.session.post(url,data=data,json=json,headers=headers,timeout=timeout,verify=verify)
            response.raise_for_status()

            content_type = response.headers.get("Content-Type", "").lower()
            if "json" in content_type:
                return response.json()
            else:
                return BeautifulSoup(response.content, "html.parser")
        except Exception as e:
            raise Exception(f"Error in post_soup: {e}")