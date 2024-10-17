import requests
from bs4 import BeautifulSoup


def get_session(Article_link, url, headers):
    try:
        session = requests.session()

        mainheaders = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.9,da;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            #'Cookie': '_ga=GA1.2.1173015132.1713518685; _gid=GA1.2.420389513.1713518685; OptanonAlertBoxClosed=2024-04-19T09:30:09.219Z; OJSSID=cpjtm2gnsc34p4202lvb90g8q4; _ga_FQN9GYLHXQ=GS1.2.1713519009.1.1.1713520783.0.0.0; _ga_HHVL7DJC16=GS1.2.1713519009.1.1.1713520783.60.0.0; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Apr+19+2024+15%3A29%3A43+GMT%2B0530+(India+Standard+Time)&version=202401.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=40f6d461-1415-482e-a5bc-a403f5041179&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=%3B&AwaitingReconsent=false',
            'Host': 'recyt.fecyt.es',
            'Pragma': 'no-cache',
            'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        }


        first_page = session.get(Article_link, headers=mainheaders)
        id = BeautifulSoup(first_page.content, 'html.parser').find('input', {'name': 'csrfToken'}).get('value')
        pay_load = {"csrfToken": id,
                    "source": "/index.php/AEDIP/issue/archive",
                    "username": "eselvier-aedipr",
                    "password": "eselvier",
                    "remember": "1"}

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.9,da;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Length': '142',
            'Content-Type': 'application/x-www-form-urlencoded',
            #'Cookie': 'OJSSID=usivpv6m83fipddvcmbmotg0j1; _ga=GA1.2.1173015132.1713518685; _gid=GA1.2.420389513.1713518685; OptanonAlertBoxClosed=2024-04-19T09:30:09.219Z; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Apr+19+2024+15%3A00%3A09+GMT%2B0530+(India+Standard+Time)&version=202401.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=40f6d461-1415-482e-a5bc-a403f5041179&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; _ga_FQN9GYLHXQ=GS1.2.1713519009.1.0.1713519009.0.0.0; _ga_HHVL7DJC16=GS1.2.1713519009.1.0.1713519009.60.0.0',
            'Host': 'recyt.fecyt.es',
            'Origin': 'https://recyt.fecyt.es',
            'Pragma': 'no-cache',
            'Referer': 'https://recyt.fecyt.es/index.php/AEDIP/login?source=%2Findex.php%2FAEDIP%2Fissue%2Farchive',
            'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        }

        login_response = session.post(url, headers=headers, data=pay_load)
        response = session.get(Article_link, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        cookies_main = login_response.cookies
        cookie_str = '; '.join([f"{cookie.name}={cookie.value}" for cookie in cookies_main])

        headers_main = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.9,da;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Cookie': cookie_str,
            'Host': 'recyt.fecyt.es',
            'Pragma': 'no-cache',
            'Referer': 'https://recyt.fecyt.es/index.php/AEDIP/login?source=%2Findex.php%2FAEDIP%2Fissue%2Farchive',
            'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        }

        res2 = session.get('https://recyt.fecyt.es/index.php/AEDIP/issue/archive', headers=headers_main)
        soup2 = BeautifulSoup(res2.content, "lxml")

        print(soup)

    except requests.RequestException as e:
        print("Error fetching URL:", e)
        return None


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9,da;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'recyt.fecyt.es',
    'Pragma': 'no-cache',
    'Referer': 'https://recyt.fecyt.es/index.php/AEDIP/login?source=%2Findex.php%2FAEDIP%2Fissue%2Farchive',
    'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

Article_link = 'https://recyt.fecyt.es/index.php/AEDIP/issue/archive'
url = "https://recyt.fecyt.es/index.php/AEDIP/login/signIn"

soup = get_session(Article_link, url, headers)
