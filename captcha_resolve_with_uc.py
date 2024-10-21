import time

from bs4 import BeautifulSoup
import undetected_chromedriver as uc

def get_driver_content(url, cookies):
    options = uc.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-software-rasterizer')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--user-agent=YOUR_USER_AGENT_STRING')
    options.add_argument('--version_main=108')

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

# cookie = {
#     'The_Company_of_BiologistsMachineID': '638505741362209925',
#     'fpestid': '8vNK_m__2BcaJLTA_nWIiDKhF8UZAz5411b5OSXAbKBA5WO0Gz3iRVl-458ZIf1htrWnNg',
#     '__stripe_mid': 'c3b18f06-03d3-4a03-a426-802ba209e20d0f4d57',
#     '_cc_id': 'cafdec109ff312a1c2e42977d4df533a',
#     'OptanonAlertBoxClosed': '2024-05-06T06:35:45.512Z',
#     'COB_SessionId': '3gxogrz20cyxvbveji01rojo',
#     '__cf_bm': '.Lxulmwnwcor39pg3W1w86VU_gAxeD2EEcPNb4yV.gg-1719374137-1.0.1.1-fjtBoItry6MJ.UK4GR6bnwjGhP2cqOGL3kbCNCc23K.IQdq4Uh7aV9BywjP6R0NKkMObrN92FrB94nuqTxjZ5w',
#     'cf_clearance': 'uvU1fsoJMUW5Ywy8sMbhXFUV29blLuRJUAKS_DR9R_s-1719374140-1.0.1.1-YAVqb.MCUhJltJa1RgTJsEhzMRcrDjF2nHYJ_TWvyEUfKja.2FgWpknLhU3hBiou1WjbiWR9SVaNct0JWAPIOw',
#     'panoramaId_expiry': '1719978942096',
#     'panoramaId': '53f6b4c4b73d554d5c6a325e0eb416d53938eadfba7b839999e0a28806200879',
#     'panoramaIdType': 'panoIndiv',
#     '_gid': 'GA1.2.1587264678.1719374194',
#     '__stripe_sid': '870db40a-d5a4-4e85-b15a-498a372c840c024a29',
#     'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Jun+26+2024+09%3A31%3A51+GMT%2B0530+(India+Standard+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=5436df06-d8f6-414a-be74-4477e0f35dc5&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0003%3A1%2CC0004%3A1%2CC0002%3A1%2CC0001%3A1&geolocation=LK%3B1&AwaitingReconsent=false',
#     '_gat_UA-57233518-6': '1',
#     '_ga_YXBDEHVL2V': 'GS1.1.1719374193.5.1.1719374512.0.0.0',
#     '_ga': 'GA1.1.468755934.1714977344',
#     '__gads': 'ID=d7dc8a1f0e6edb6c:T=1714977341:RT=1719374460:S=ALNI_MYX1uR5YvG39Rjt7HFvLdZa2dEObw',
#     '__gpi': 'UID=00000e0d984f80c4:T=1714977341:RT=1719374460:S=ALNI_MZpJvMIjHlpqvLv1kBYEUZpJOFIig',
#     '__eoi': 'ID=b571390403ad6f60:T=1714977341:RT=1719374460:S=AA-AfjaErBnPrUkhX2htosl2_2aL'
# }

cookie = {
    "guardret":"QxtaCkVdFVsLL2wbWwNWNgJUVUkVXwIPBVRlZX5YB1YCcE4ZGkEVXwcJB01yLWxVAFkCOFpOGk1eCFZLQwA9JGxVA1kBcEMECA4CXQoPBE1yLGxVClsGaVRMGgMFXAFFGxpyICcCVx1HJBtFGgMGUgENAlBgY3tXC1YKaVRNGgMPUwQUFRhybnxWABMfPlRBUVRSFkdZWhFybn9YAFsGdEYCDQAHVQUUFRlybnZXAkIRPFQPCgAFGB9DFRU5OSscRg9eNVQPCQ4FUAYJB1ZlbX5dAUIRPVQPAAAHSRFBFVtibXwSb0IRJwJbGgMCVx8aRA05MCsdEFQGd04ZGklWAlZnQAg0ICZNCF8BfUYZGklWAlZnXwQ5MyYbEFQGcEdI",
    "guardok":"bfJpQlpHtb9sw7GBsq8DAPGje32yamu4q79JNJo7mlMt3ssza8yZ++fJasnoWb7Rg2S0eDVaBGWOZ4nXeB//2g==",
    "ASP.NET_SessionId":"2givcdp0oy2n5p313bovbcw3"
}


url='https://www.surface-techj.com/bmjsen/ch/index.aspx'
soup, cookies = get_driver_content(url, cookie)
print(soup)






