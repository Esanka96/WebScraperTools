import random
import string
import os
import requests
from bs4 import BeautifulSoup
import cloudscraper

scraper = cloudscraper.create_scraper()

DOWNLOAD_HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Priority": "u=0, i",
        "Sec-Ch-Ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        "Sec-Ch-Ua-Arch": '"x86"',
        "Sec-Ch-Ua-Bitness": '"64"',
        "Sec-Ch-Ua-Full-Version": '"134.0.6998.89"',
        "Sec-Ch-Ua-Full-Version-List": '"Chromium";v="134.0.6998.89", "Not:A-Brand";v="24.0.0.0", "Google Chrome";v="134.0.6998.89"',
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


def generate_session_id(length=8):
    """Generate a random session ID for proxy."""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


def download_page(url):
    session_id = generate_session_id()
    proxy_info = {
        "login": f"oc-32c783969ae23d019b04ce6b2b8961be5a3a64239ec449db503d98aed0046e42-country-US-session-{session_id}",
        "password": "zdm1s1d0fdlg",
        "host": "proxy.oculus-proxy.com",
        "port": "31112"
    }
    proxy_auth = f"{proxy_info['login']}:{proxy_info['password']}"
    proxy_url = f"http://{proxy_auth}@{proxy_info['host']}:{proxy_info['port']}"
    proxies = {
        "http": proxy_url,
        "https": proxy_url
    }

    response = scraper.get(url, headers=DOWNLOAD_HEADERS, proxies=proxies, timeout=10)
    response.raise_for_status()

    print(response.status_code)
    soup= BeautifulSoup(response.content, 'html.parser')
    return soup


url = "https://main.knesset.gov.il/pages/default.aspx"
#url = "https://www.iplt20.com/"

soup = download_page(url)

print(soup)

