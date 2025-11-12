import re
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import chromedriver_autoinstaller as chromedriver
import time
import os
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import pandas as pd
import tempfile

#chromedriver.install()

download_path = os.path.join(tempfile.gettempdir(), 'Ref_download')
if not os.path.exists(download_path):
    os.makedirs(download_path)

new_path="Out"
if not os.path.exists(new_path):
    os.makedirs(new_path)

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

def get_driver_pdf(url, new_filename,download_path,request_cookies):
    driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    # options.add_argument(
    #     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    for cookie_name, cookie_value in request_cookies.items():
        driver.add_cookie({"name": cookie_name, "value": cookie_value})
    driver.get(url)
    time.sleep(60)
    content = driver.page_source
    pdf_soup = BeautifulSoup(content, 'html.parser')
    print(pdf_soup)

#"https://pubs.geoscienceworld.org//sepm/jsedres/article-pdf/94/2/179/6316713/10.2110_jsr.2023.060.pdf"
#'https://journals.aai.org/immunohorizons/article-pdf/8/3/254/1654599/ih2300108.pdf'
#"https://www.iieta.org/download/file/fid/122816"
#"https://peerj.com/articles/matsci-32.pdf"
#"https://journals.biologists.com/jeb/article-pdf/227/5/jeb246275/3380012/jeb246275.pdf"
#"https://journals.aai.org/jimmunol/article-pdf/212/7/1075/1654412/ji2300336.pdf"
pdf_link="http://jsedres.sepmonline.org/content/current"
get_driver_pdf(pdf_link,new_path,download_path,request_cookies)
