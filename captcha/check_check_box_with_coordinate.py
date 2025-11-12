from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options()
#options.add_argument('--headless')
options.add_argument('--incognito')
options.add_argument('--disable-gpu')
options.add_argument('--disable-software-rasterizer')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--disable-popup-blocking')
options.add_argument('--window-size=1920,1080')
options.add_argument(f'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')

driver = webdriver.Chrome(options=options)

driver.get("https://pdfcoffee.com/qdownload/np0017962014-pt-unlocked-pdf-free.html")
time.sleep(5)

# element = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-success.btn-block")
# element.click()
# time.sleep(35)

x, y = 988, 506

script = f"""
var dot = document.createElement('div');
dot.style.position = 'absolute';
dot.style.left = '{x}px';
dot.style.top = '{y}px';
dot.style.width = '20px';          // smaller width
dot.style.height = '20px';         // smaller height
dot.style.backgroundColor = 'red';
dot.style.borderRadius = '50%';
dot.style.zIndex = '9999';
dot.style.pointerEvents = 'none';
document.body.appendChild(dot);
"""

driver.execute_script(script)

time.sleep(5)
actions = ActionChains(driver)
actions.move_by_offset(x, y).click().perform()

time.sleep(10)
