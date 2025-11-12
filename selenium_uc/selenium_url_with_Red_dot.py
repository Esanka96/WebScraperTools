from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
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

driver = webdriver.Chrome(options=options)

driver.get("https://example.com")

x, y = 500, 300

script = f"""
var dot = document.createElement('div');
dot.style.position = 'absolute';
dot.style.left = '{x}px';
dot.style.top = '{y}px';
dot.style.width = '0.1px';          // smaller width
dot.style.height = '0.1px';         // smaller height
dot.style.backgroundColor = 'red';
dot.style.borderRadius = '50%';
dot.style.zIndex = '9999';
dot.style.pointerEvents = 'none';
document.body.appendChild(dot);
"""

driver.execute_script(script)

time.sleep(5)
driver.quit()
