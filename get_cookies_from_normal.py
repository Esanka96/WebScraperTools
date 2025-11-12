import requests
from bs4 import BeautifulSoup

def get_soup(url):
    response = requests.get(url,headers=headers)
    cookie=response.cookies
    print(cookie)
    # token=cookie.get("wkxt3_csrf_token").replace("-","")
    # return token

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

url='https://www.actasc.cn/homeNav?lang=en'
cookies=get_soup(url)
print(cookies)

