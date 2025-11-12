import requests
from bs4 import BeautifulSoup

getSoup = lambda url : BeautifulSoup(requests.get(url,headers=headers).content, 'html.parser')

headers = {

    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}



url='https://dapre.presidencia.gov.co/dapre/paginas/busqueda.aspx?k=cambio%20clim%C3%A1tico'

for i in range(100):
    try:
        current_soup = getSoup(url)
        print(current_soup)
        #print(current_soup.find("div",attrs={"id":"title-container"}).get_text(strip=True))
    except:
        print("captcha available")
