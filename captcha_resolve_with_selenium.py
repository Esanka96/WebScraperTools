from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# Instantiate the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Load the target page
captcha_page_url = "https://research.aota.org/crawlprevention/governor?content=%2fajot"
driver.get(captcha_page_url)

# Solve the Captcha
print("Solving Captcha")
solver = TwoCaptcha("a03589ed562de14589af1d772c2b41bb")
response = solver.recaptcha(sitekey='6LcrtosaAAAAADRnMjagCVGiuXgoXFWysds7VKsG', url=captcha_page_url)
code = response['code']
print(f"Successfully solved the Captcha. The solve code is {code}")

# Set the solved Captcha
recaptcha_response_element = driver.find_element(By.ID, 'captcha')
driver.execute_script(f'arguments[0].setAttribute("data-response", "{code}");', recaptcha_response_element)

# Submit the form (assuming the form submission mechanism remains unchanged)
submit_btn = driver.find_element(By.ID, 'btnSubmit')
submit_btn.click()


# Pause the execution so you can see the screen after submission before closing the driver
input("Press enter to continue")
driver.close()
