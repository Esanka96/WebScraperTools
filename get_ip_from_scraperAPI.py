import os
import re
import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.iplt20.com/'
curl = f"http://api.scraperapi.com?api_key=4ccf9c7f4ab628f9ed6ea00b373cc39c&url={url}"
response = requests.get(curl)


