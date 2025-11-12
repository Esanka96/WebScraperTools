import requests
from bs4 import BeautifulSoup

headers = {
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


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "cookie": "_gid=GA1.3.969398396.1756184300;",
              #"waap_id=DGv/+xn0iZnMDdfBjQYq93eTpPoq472z3+iX9XyBFojOiNcJY6IdYwaVlrixyVqPYdcRgnFqsf+LjbWwzuDB2B0KKh7CcCpFg2t8vIJj34F7wuheyz38DAEPmwa14it5noS+ZQiCItOCdy5OUOTLq6IpAry3LQuTR8j06VcgHxaAD2MAolfS7bJYdmPJr2swQ2pKChdH5HMhxk6/YM5zHO8nTMDw1g73ypAF2nkUNKoj1AGq2NvNW2a1VLD8jpMAIdGPBhB/yG39RYxvh9T4B9+bHiWS+JcFzBI_;",
              #"deviceChannel=Default;",
              #"_gat=1;",
              #"_ga_F5VXQ9Z7N5=GS2.1.s1755763851$o10$g0$t1755763851$j60$l0$h0;",
              #"_ga=GA1.1.824627959.1754379508; ",
              #"WSS_FullScreenMode=false",
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
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}

payload = { 'api_key': 'ff906ae22292945e7a28d09bb8093107', 'url': 'https://main.knesset.gov.il/pages/default.aspx' }
res = requests.get('https://api.scraperapi.com/', params=payload,headers=headers)
soup = BeautifulSoup(res.content, "html.parser")
print(soup)
