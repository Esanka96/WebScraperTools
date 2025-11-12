from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://example.com")

x, y = 400, 250

dot_script = f"""
var dot = document.createElement('div');
dot.id = 'red-dot';
dot.style.position = 'absolute';
dot.style.left = '{x}px';
dot.style.top = '{y}px';
dot.style.width = '0.1rem';
dot.style.height = '0.1rem';
dot.style.borderRadius = '50%';
dot.style.backgroundColor = 'red';
dot.style.zIndex = '9999';
document.body.appendChild(dot);
"""

driver.execute_script(dot_script)

time.sleep(5)

actions = ActionChains(driver)
actions.move_by_offset(x, y).click().perform()

time.sleep(3)
driver.quit()
