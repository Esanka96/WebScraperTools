import time
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Initialize undetected Chrome
options = uc.ChromeOptions()
options.add_argument("--start-maximized")
driver = uc.Chrome(options=options)

# Open the page
driver.get("https://www.canlii.org/")
time.sleep(5)  # Wait for page to load

print(driver.page_source)

# Locate the slider element
slider = driver.find_element(By.CLASS_NAME, "slider")  # slider bar
target = driver.find_element(By.CLASS_NAME, "sliderTarget")  # where it needs to go

# Get slider width
slider_width = slider.size['width']

# Use ActionChains to drag the slider
actions = ActionChains(driver)
actions.click_and_hold(slider).perform()
time.sleep(0.2)

# Move slider gradually (mimicking human behavior)
for i in range(slider_width):
    actions.move_by_offset(1, 0).perform()
    time.sleep(0.01)

# Release the slider
actions.release().perform()

time.sleep(2)  # wait for verification
