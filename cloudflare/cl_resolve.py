import cloudscraper
from bs4 import BeautifulSoup
import re
import os
import requests
import time
from cl_bypass import get_cf_clearance_info_sync

scraper = cloudscraper.create_scraper()

url = "https://emb.gov.ph/"
def getSoup(url, cookies, useragent):
    headers_new = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Cookie": cookies,
        "Priority": "u=0, i",
        #"Referer": "https://anvisalegis.datalegis.net/",
        "Sec-Ch-Ua-Arch": "x86",
        "Sec-Ch-Ua-Bitness": "64",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Model": "",
        "Sec-Ch-Ua-Platform": "Windows",
        "Sec-Ch-Ua-Platform-Version": "19.0.0",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": useragent
    }
    print("⏳ Please wait, content is loading...")
    response = scraper.get(url,headers=headers_new)
    soup= BeautifulSoup(response.content, 'html.parser')
    return soup

try:
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"

    max_attempts = 5
    attempt = 0
    cf_clearance_cookies = None

    print("Working on Cloudflare challenge...")

    while attempt < max_attempts:
        cl_info = get_cf_clearance_info_sync(url, headed=False, user_agent=user_agent)

        if cl_info:
            for domain, info_list in cl_info.items():
                if info_list:
                    cf_clearance_cookies = info_list[0]["cookies"]
                    break

        if cf_clearance_cookies:
            print("Successfully retrieved cf clearence cookies. Cloudflare challenge success...")
            break

        attempt += 1
        print(f"Attempt {attempt} failed, retrying in 3 seconds...")
        time.sleep(3)

    if not cf_clearance_cookies:
        print("Cloudflare challange failed. Continue with browser bypass...")
    else:
        cookie_header = "; ".join(f"{c['name']}={c['value']}" for c in cf_clearance_cookies if 'name' in c and 'value' in c)

    soup = getSoup(url, cookie_header, user_agent)
    print(soup)

except Exception as e:
    print("Cloudflare failed!")



