import requests
from bs4 import BeautifulSoup
import os
import re
from datetime import datetime
import pandas as pd
from tenacity import retry, stop_after_attempt, wait_fixed

getSoup=lambda url:(BeautifulSoup(requests.get(url,verify=False).content),"html.parser")

@retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
def download_pdf(url, out_path):
    with requests.get(url,headers=headers, allow_redirects=True,stream=True) as r:
        r.raise_for_status()
        with open(out_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)


out_path='Out'
if not os.path.exists(out_path):
    os.makedirs(out_path)
out_folder=os.path.join(out_path,'New.pdf')

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
    "accept-encoding": "gzip, deflate",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "connection": "keep-alive",
    #"cookie": "ASP.NET_SessionId=f3ew2ywrsizx1acg5d3zjsfa",
    "host": "gdnykx.cnjournals.org",
    "pragma": "no-cache",
    "referer": "http://gdnykx.cnjournals.org/gdnykxen/ch/reader/issue_browser.aspx",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}



pdf_link="http://gdnykx.cnjournals.org/gdnykxen/ch/reader/create_pdf.aspx?file_no=202409005&year_id=2024&quarter_id=9&falg=1"
# print(requests.get(pdf_link,headers=headers))
# pdf_content = requests.get(pdf_link,headers=headers,verify=False).content
# with open(out_folder, 'wb') as file:
#     file.write(pdf_content)
# print(requests.get(pdf_link).status_code)
download_pdf(pdf_link, out_folder)
