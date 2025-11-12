import requests
from bs4 import BeautifulSoup
import urllib3
import ssl
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager

class UnsafeTLSAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        ctx = ssl.create_default_context()
        ctx.options |= ssl.OP_LEGACY_SERVER_CONNECT
        kwargs['ssl_context'] = ctx
        return super().init_poolmanager(*args, **kwargs)

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "connection": "keep-alive",
    "host": "ordspub.epa.gov",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

session = requests.Session()
session.mount("https://", UnsafeTLSAdapter())

def get_soup(url):
    try:
        response = session.get(url, headers=headers)
        print(f"⏳ Please wait, content is loading...")
        if response.status_code != 200:
            raise Exception(f"⚠️ Failed to retrieve page: {url} [status code: {response.status_code}]")

        print("✅ Status code 200 received. Procedure continues")
        return BeautifulSoup(response.content, 'html.parser')
    except requests.exceptions.RequestException as e:
        raise Exception(f"⚠️ Request error while accessing {url}: {e}")

url ="https://comptox.epa.gov/dashboard/chemical-lists/PFASOECD"

soup = get_soup(url).find_all("script")

print(soup[1])