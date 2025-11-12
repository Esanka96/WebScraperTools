from bs4 import BeautifulSoup
import time
import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver
chromedriver.install()

url="https://dapre.presidencia.gov.co/dapre/paginas/busqueda.aspx?k=cambio%20clim%C3%A1tico"
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'
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

driver.get(url)
print("Wait until the PDF is downloaded")
time.sleep(10)

content = driver.page_source

soup = BeautifulSoup(content, 'html.parser')

print(driver.get_cookies())

driver.close()
driver.quit()







