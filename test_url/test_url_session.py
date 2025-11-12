import requests
from bs4 import BeautifulSoup


def get_session(firstLink, secondLink):
    try:
        session = requests.session()

        firstHeaders = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "cache-control": "no-cache",
            "connection": "keep-alive",
            "host": "www.retsinformation.dk",
            "pragma": "no-cache",
            "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }

        session.get(firstLink, headers=firstHeaders)

        secondHeaders = {
            "accept": "application/json",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "cache-control": "no-cache",
            "connection": "keep-alive",
            "content-length": "19",
            "content-type": "application/json",
            "host": "www.retsinformation.dk",
            "origin": "https://www.retsinformation.dk",
            "pragma": "no-cache",
            "referer": "https://www.retsinformation.dk/eli/lta/2024/291",
            "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }

        content=session.post(secondLink,headers=secondHeaders, json=data)
        soup = BeautifulSoup(content.content, "html.parser")

        print(soup)

    except requests.RequestException as e:
        print("Error fetching URL:", e)
        return None


firstLink = 'https://www.retsinformation.dk/eli/lta/2024/291'
secondLink = "https://www.retsinformation.dk/api/document/eli/lta/2024/291"

data = {'isRawHtml': False}

soup = get_session(firstLink, secondLink)
