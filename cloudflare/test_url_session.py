import requests
from bs4 import BeautifulSoup
import cloudscraper

def get_session(firstLink, secondLink):
    try:
        session = cloudscraper.create_scraper()

        firstHeaders = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Priority": "u=0, i",
            "Sec-Ch-Ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
            "Sec-Ch-Ua-Arch": '"x86"',
            "Sec-Ch-Ua-Bitness": '"64"',
            "Sec-Ch-Ua-Full-Version": '"134.0.6998.89"',
            "Sec-Ch-Ua-Full-Version-List": '"Chromium";v="134.0.6998.89", "Not:A-Brand";v="24.0.0.0", "Google Chrome";v="134.0.6998.89"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Model": '""',
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Ch-Ua-Platform-Version": '"15.0.0"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
        }

        response = session.get(firstLink, headers=firstHeaders)

        print(response.status_code)
        print(response.cookies)

        secondHeaders = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "cache-control": "no-cache",
            "connection": "keep-alive",
            "content-length": "69",
            "content-type": "application/x-www-form-urlencoded",
            "cookie": "JSESSIONID=F4FC72D34B7F8A8E28F4C11AB92125BC",
            "host": "webprod.hc-sc.gc.ca",
            "origin": "https://webprod.hc-sc.gc.ca",
            "pragma": "no-cache",
            "referer": "https://webprod.hc-sc.gc.ca/nhpid-bdipsn/",
            "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
        }

        content=session.post(secondLink,headers=secondHeaders, data=payload)
        soup = BeautifulSoup(content.content, "html.parser")

        print(content.cookies)
        print(content.status_code)
        print(soup)

    except requests.RequestException as e:
        print("Error fetching URL:", e)
        return None


firstLink = 'https://webprod.hc-sc.gc.ca/nhpid-bdipsn'
secondLink = "https://webprod.hc-sc.gc.ca/nhpid-bdipsn/searchIngred"

payload = {
    "_csrf": "bcb61238-eee8-4a9e-9c2a-8f303c50cbc9",
    "searchTxt": "aa",
    "searchRole": "-1"
}

soup = get_session(firstLink, secondLink)
