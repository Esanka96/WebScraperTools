import time

from bs4 import BeautifulSoup
import undetected_chromedriver as uc

def get_driver_content(url, cookies):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'

    options = uc.ChromeOptions()
    #options.add_argument('--headless')
    # options.add_argument('--incognito')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-software-rasterizer')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--window-size=1920,1080')
    options.add_argument(f'--user-agent={user_agent}')

    driver = uc.Chrome(options=options)
    driver.get(url)
    time.sleep(5)
    for cookie_name, cookie_value in cookies.items():
        driver.add_cookie({"name": cookie_name, "value": cookie_value})

    driver.get(url)
    time.sleep(5)
    content = driver.page_source
    cookies = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in driver.get_cookies()])
    soup = BeautifulSoup(content, 'html.parser')
    return soup, cookies

request_cookies={
    'GeoScienceWorldMachineID': '638475566012738969',
    'fpestid': 'f6tdgLTO5-uu-D79o3BwgcCJ8LIF5rYe6uzYtjoq9QujxAeEBDCLFb5WQ0DZ1DA7wo7mWA',
    '_ga': 'GA1.1.1487530923.1711959819',
    '_gid': 'GA1.3.569889817.1711959819',
    '_cc_id': '23c309b2b916c241c5354943d7a590ab',
    'panoramaId_expiry': '1712564622863',
    'panoramaId': '0a62239d6889f74214825d16dbaf185ca02cf678ef814ebd2813a55b670875f8',
    'panoramaIdType': 'panoDevice',
    '_hjSessionUser_2619384': 'eyJpZCI6ImM4ZTc4YjNmLTIzYmItNTkyMi1iZDcwLWY5YzFmNWMyMzQyZSIsImNyZWF0ZWQiOjE3MTE5NTk4MjU0NzYsImV4aXN0aW5nIjp0cnVlfQ==',
    'hubspotutk': '31fbd733f95a4abb67792c123cf2d8b4',
    'GDPR_24_.geoscienceworld.org': 'true',
    'TheDonBot': 'D47BD6096350C06E91E5E85FFD4A95DF',
    'GSW_SessionId': 'gyjp0c2zr4to30bzz5irddko',
    '_gat_UA-28112735-4': '1',
    '_gat_UA-28112735-1': '1',
    '_gat_UA-50143594-1': '1',
    '_gat_UA-28112735-5': '1',
    '_gat_UA-76340245-2': '1',
    '_gat_UA-1008571-9': '1',
    '_gat_UA-1008571-10': '1',
    '_gat_UA-1008571-11': '1',
    '_gat_UA-1008571-12': '1',
    '_gat_UA-1008571-15': '1',
    '_gat_UA-1008571-16': '1',
    '_gat_UA-1008571-17': '1',
    '_gat_UA-1008571-18': '1',
    '_ga_YVB7JQBY6Z': 'GS1.1.1711999347.5.0.1711999347.0.0.0',
    '_hjSession_2619384': 'eyJpZCI6IjNmMWM2NWVkLTY4OTEtNDliOS1hNDFhLTVkYTNkNGI5M2Q0NyIsImMiOjE3MTE5OTkzNDc5MDEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=',
    '_ga_11RK1D9N56': 'GS1.3.1711999348.5.0.1711999348.0.0.0',
    '_ga_MKZCHDYBTN': 'GS1.3.1711999348.5.0.1711999348.0.0.0',
    '_ga_781B8JFM4R': 'GS1.3.1711999348.5.0.1711999348.0.0.0',
    '_ga_KZ8XM8M5S3': 'GS1.3.1711999348.5.0.1711999348.0.0.0',
    '_ga_5FBFHZKYCW': 'GS1.3.1711999349.5.0.1711999349.0.0.0',
    '_ga_YY6XD0X474': 'GS1.3.1711999349.5.0.1711999349.0.0.0',
    '_ga_RBDZFVMYBJ': 'GS1.3.1711999349.5.0.1711999349.0.0.0',
    '_ga_LK2NSTY4C0': 'GS1.3.1711999349.5.0.1711999349.0.0.0',
    '_ga_2ZJXB7SCK6': 'GS1.3.1711999349.5.0.1711999349.0.0.0',
    '_ga_HP48M3E3R7': 'GS1.3.1711999349.5.0.1711999349.0.0.0',
    '__hstc': '147277928.31fbd733f95a4abb67792c123cf2d8b4.1711959837613.1711973459982.1711999352182.5',
    '__hssrc': '1',
    '__hssc': '147277928.1.1711999352182'
}

url='https://pubs.geoscienceworld.org/aapgbull/issue/108/11'
soup, cookies = get_driver_content(url, request_cookies)
print(soup)






