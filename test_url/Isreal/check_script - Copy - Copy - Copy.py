import time
import random
import requests
from bs4 import BeautifulSoup

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Gecko/20100101 Firefox/117.0",
    "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/117.0",
]

def get_session():
    s = requests.Session()
    s.headers.update({
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "cookie": "_gid=GA1.1.859665377.1756445510;",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "referer": "https://main.knesset.gov.il/pages/default.aspx",
        "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": random.choice(USER_AGENTS)
    })
    return s

url = "https://main.knesset.gov.il/pages/default.aspx"

for i in range(20):
    try:
        if i % 5 == 0:
            session = get_session()

        res = session.get(url, timeout=20)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, "html.parser")

        viewstate_gen = soup.find("input", {"id": "__VIEWSTATEGENERATOR"})

        print(viewstate_gen["value"])

        time.sleep(random.randint(8, 15))

    except Exception as e:
        print("Request failed:", e)
        time.sleep(random.randint(8, 15))
