import requests
from bs4 import BeautifulSoup
import os
import re
from datetime import datetime
import pandas as pd
import json
import urllib.parse

def get_soup(url):
    response = requests.post(url, headers=headers,json=payload)
    response_code=response.status_code
    return response.json()
    #soup= BeautifulSoup(response.content, 'html.parser')
    #return soup

# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
#     "Cache-Control": "no-cache",
#     "Pragma": "no-cache",
#     "Priority": "u=0, i",
#     "Sec-Ch-Ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
#     "Sec-Ch-Ua-Arch": '"x86"',
#     "Sec-Ch-Ua-Bitness": '"64"',
#     "Sec-Ch-Ua-Full-Version": '"134.0.6998.89"',
#     "Sec-Ch-Ua-Full-Version-List": '"Chromium";v="134.0.6998.89", "Not:A-Brand";v="24.0.0.0", "Google Chrome";v="134.0.6998.89"',
#     "Sec-Ch-Ua-Mobile": "?0",
#     "Sec-Ch-Ua-Model": '""',
#     "Sec-Ch-Ua-Platform": '"Windows"',
#     "Sec-Ch-Ua-Platform-Version": '"15.0.0"',
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "none",
#     "Sec-Fetch-User": "?1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
# }

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    #"cookie": "ASP.NET_SessionId=5xapibz22iyykmxocwzqhwws; sl-session=QK+IHQALA2lpFxV7RwsTNw==; _ga=GA1.1.678374677.1761721497; _gcl_au=1.1.1110222648.1761721497; uuid=435db4a5; _ga_DVTQR7BVGN=GS2.1.s1761721497$o1$g1$t1761722249$j60$l0$h1240737372",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://bio-protocol.org/",
    "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-site",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
}



payload = {
    "protocol_id_version":"5468"
}


url='https://journal-api.bio-protocol.org/v1/journal/pdfReader/meta'

soup = get_soup(url)["data"]["protocol"]["pdf_url"]

print(soup)





