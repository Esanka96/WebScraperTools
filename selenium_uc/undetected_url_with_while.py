from bs4 import BeautifulSoup
import time
import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver
chromedriver.install()

#url='https://chemicaldata.gov.vn/o_a/chat/public-list?page=3510&pageSize=50&sort=CasNumber-asc'
url="https://www.nmpa.gov.cn/xxgk/ggtg/hzhpggtg/jmhzhptg/20210528174051160.html"
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
options = uc.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-software-rasterizer')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--disable-popup-blocking')
options.add_argument(f'--user-agent={user_agent}')
options.add_argument('--version_main=108')

driver = uc.Chrome(options=options)
# driver.get(url)
# time.sleep(100)

try:
    driver.get(url)
    print("Wait until the PDF is downloaded")

    time.sleep(5)

    count = 0
    max_count = 40

    while count < max_count:
        if BeautifulSoup(driver.page_source, "html.parser").find("h2", class_="title"):
            break
        time.sleep(5)
        count += 1

    content = driver.page_source

    soup = BeautifulSoup(content, 'html.parser')
    print(soup)


    driver.close()
    driver.quit()
except:
    pass






