import time

from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup

ua = UserAgent()
headers = {
    "User-Agent": ua.random,  # randomly selected user-agent
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com"
}


for i in range(1,20):

    url = "https://projecteuclid.org/journals/journal-of-commutative-algebra/current"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)
    break

