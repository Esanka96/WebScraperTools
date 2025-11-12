import requests
from bs4 import BeautifulSoup
import cloudscraper

def getSoup(url):
    #response = requests.get(url,headers=headers)
    session.cookies.update(request_cookies)
    response = session.get(url, headers=headers)
    soup= BeautifulSoup(response.content, 'html.parser')
    return soup

request_cookies={
    'American_Association_of_ImmunologistsMachineID': '638471601269158797',
    'fpestid': 'uj4xHuJZCmsEO4iwaCml_ZkpQFn5g5saJ4PWcjuRSSLLuOlaM_8XgtiSo8KUh7FqKXfODQ',
    '_ga': 'GA1.1.1738412850.1711563329',
    '_cc_id': '23c309b2b916c241c5354943d7a590ab',
    'panoramaId_expiry': '1712168129750',
    'panoramaId': 'f172d411e6629317a72b7b3d0265185ca02cd0398a246c61e4507a03ae330588',
    'panoramaIdType': 'panoDevice',
    '__gpi': 'UID=00000d6e75e9420f:T=1711563329:RT=1711569659:S=ALNI_MYnqJqt7ok2paUm1nGOX71B0ZffsQ',
    'TheDonBot': '93CD1E864CFC6333E47A0976D607D384',
    '_ga_G5TCNFJCYP': 'GS1.1.1711734015.2.0.1711734015.0.0.0',
    'AAI_SessionId': 'epl2u5ihy1zrrzyar0bq0w4f',
    '__gads': 'ID=6fda084ce091ab7e:T=1711563329:RT=1711946941:S=ALNI_Ma1p7ggsV0Uk_PmHTTPGLWi9m1M0w',
    '__eoi': 'ID=d4f6ab1a31868add:T=1711563329:RT=1711946941:S=AA-AfjZwpT1cyKFeLlJ7WwhSyOfC',
    'GDPR_54_journals.aai.org': 'true',
    '_ga_333EE1C4XR': 'GS1.1.1711946940.7.1.1711946990.0.0.0'
}

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "Sec-Ch-Ua-Arch": "\"x86\"",
    "Sec-Ch-Ua-Bitness": "\"64\"",
    "Sec-Ch-Ua-Full-Version": "\"126.0.6478.127\"",
    "Sec-Ch-Ua-Full-Version-List": "\"Not/A)Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"126.0.6478.127\", \"Google Chrome\";v=\"126.0.6478.127\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Model": "\"\"",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Ch-Ua-Platform-Version": "\"15.0.0\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}



url='https://journals.aai.org/jimmunol/issue/213/10'
session = cloudscraper.create_scraper()
current_soup = getSoup(url)
pdf_link="https://journals.aai.org/jimmunol/article-pdf/213/10/1569/1664688/ji2400470.pdf"
with open("out.pdf","wb") as file:
    file.write(session.get(pdf_link).content)

# for i in range(100):
#     try:
#         session = cloudscraper.create_scraper()
#         current_soup = getSoup(url)
#         print(current_soup.find("span",class_="volume issue").get_text(strip=True))
#         #print(current_soup.find("span",class_="volume issue").text.strip())
#     except:
#         print("captcha available")
