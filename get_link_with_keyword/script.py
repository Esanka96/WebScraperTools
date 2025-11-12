import requests
import os
import re
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import quote_plus
from datetime import datetime

error_list = []

try:
    with open('keywords.txt', 'r', encoding='utf-8') as file:
        keyword_list = file.read().strip().splitlines()
except Exception as error:
    error_list.append(str(error))

for sin_key in keyword_list:
    link = f"https://www.finlex.fi/fi/haku?type=EXTENDED&exact=%22{sin_key}%22&limit=20&sort=relevance&page=1&keywords=%22{sin_key}%22&language=fin"
    print(link)