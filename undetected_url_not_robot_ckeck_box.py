from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://publications.aap.org/pediatrics/article-pdf/doi/10.1542/peds.2023-062461/1584817/peds.2023-062461.pdf")
click_button = driver.find_element("id", "captcha").click()
time.sleep(2)
login_button = driver.find_element("id", "btnSubmit").click()
time.sleep(2)
driver.implicitly_wait(5)