import requests
from bs4 import BeautifulSoup

getSoup = lambda url : BeautifulSoup(requests.get(url,headers=headers).content, 'html.parser')

headers = {

    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}



url='https://academic.oup.com/g3journal/article/14/10/jkae153/7712987'

for i in range(100):
    try:
        current_soup = getSoup(url)
        print(current_soup.find("div",class_="volume trailing-comma").get_text(strip=True))
        #print(current_soup.find("span",class_="volume issue").text.strip())
    except:
        print("captcha available")
