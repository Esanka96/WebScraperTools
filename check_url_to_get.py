import requests
from bs4 import BeautifulSoup
import urllib.parse

def get_soup(url):
    response = requests.get(url,headers=headers)
    soup= BeautifulSoup(response.content, 'html.parser')
    return soup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

url='https://jcdronline.org/issue.php?volume=Volume%2015%20&issue=Issue%201&year=2024'

current_soup=get_soup(url)

All_articles = get_soup(url).find('span',class_='journalfont').findAll('li')
for sin_art in All_articles:
    Article_link = 'https://jcdronline.org/'+sin_art.find('a').get('href')
    print(Article_link)