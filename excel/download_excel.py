import requests
from bs4 import BeautifulSoup
import os
import re
from datetime import datetime
import pandas as pd

out_path='Out'
if not os.path.exists(out_path):
    os.makedirs(out_path)
out_folder=os.path.join(out_path,'New.xlsx')


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}


pdf_link="https://edlists.org/export/list/1?page&_format=xlsx"
pdf_content = requests.get(pdf_link,headers=headers).content
with open(out_folder, 'wb') as file:
    file.write(pdf_content)

print("downloading ok!")

