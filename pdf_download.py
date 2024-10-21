import requests
from bs4 import BeautifulSoup
import os
import re
from datetime import datetime
import pandas as pd
from tenacity import retry, stop_after_attempt, wait_fixed

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


headers = {

    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}



pdf_link="https://www.ajnr.org/content/ajnr/45/10/1495.full.pdf"
# pdf_content = requests.get(pdf_link,headers=headers).content
# with open(out_folder, 'wb') as file:
#     file.write(pdf_content)

download_pdf(pdf_link, out_folder)
