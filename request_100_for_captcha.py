import requests
import cloudscraper
from bs4 import BeautifulSoup

request_cookies = {
    'IWA_PublishingMachineID': '638491186796925668',
    '_ga': 'GA1.2.892686197.1713521884',
    '_gid': 'GA1.2.1313269268.1713521884',
    'fpestid': 'eh9u8XUlgdwuY7RUwBCYJv4NZVGOKeP548CWt1y_bFcLNWRt7tUehqHRQCwwsjI1bzLnNw',
    '_cc_id': 'c98eea9794bffe9e84dcd4916e261382',
    'panoramaId_expiry': '1714126683937',
    'panoramaId': '87bb27088c11dbcbf1612371515e16d53938c438922298f84a6f843eb4291467',
    'panoramaIdType': 'panoIndiv',
    'hum_iwap_visitor': '98fc3c8c-f2ea-4750-8fe8-42302f336a62',
    '__stripe_mid': 'debea6e4-2d7d-4d84-aeb3-37410dc7dbe192f50c',
    'IWA_SessionId': 'b0y5gtz4zk0y0gh5xrgouqwm',
    '__stripe_sid': 'f79e02a8-ef2f-4a96-9c7b-3381a4c74abd83cdba',
    '_gat_UA-10590794-3': '1',
    '_gat_UA-76340245-2': '1',
    '_ga_CY814T2KFP': 'GS1.2.1713550821.2.1.1713551342.60.0.0'
}

scraper = cloudscraper.create_scraper()
#scraper.cookies.update(request_cookies)
firstUrl = "https://portlandpress.com/"

headers1 = {
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

scraper.get(firstUrl, headers=headers1)

secondUrl = "https://portlandpress.com/clinsci/issue"

headers2 = {
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

scraper.get(secondUrl, headers=headers2)

for i in range(100):
    try:
        response = scraper.get("https://portlandpress.com/clinsci/issue")
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup.find("span", class_="volume issue").text.strip())
    except:
        print("captcha available")
