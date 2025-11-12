import requests
from bs4 import BeautifulSoup
import os
import re
from datetime import datetime
import pandas as pd
from reportlab.pdfgen import canvas

def get_soup(url):
    curl=f"http://api.scraperapi.com?api_key=040ef1032ba19287c218fb774df19c4e&url={url}"
    pdf_content = requests.get(curl,headers=headers).content
    #pdf_content = requests.get(url,headers=headers).content
    print(pdf_content)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

url=('https://jmvfh.utpjournals.press/doi/pdf/10.3138/jmvfh.10.1.ed01')

soup=get_soup(url)


