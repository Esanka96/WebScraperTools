import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"

options.add_argument("--headless=new")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument(f"user-agent={user_agent}")

driver = webdriver.Chrome(options=options)
driver.get("https://comptox.epa.gov/dashboard/chemical-lists/PFASOECD")
time.sleep(20)

try:
    wait = WebDriverWait(driver, 15)

    # 1️⃣ First click the button
    first_button = wait.until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/main/div/div[4]/section/div[1]/div/div[3]/div/span[1]/div/span/div/span/button'))
    )
    first_button.click()
    print("✅ First button clicked.")

    # Optional delay to let dropdown/menu appear
    time.sleep(2)

    # 2️⃣ Then click the second element (like a menu item)
    second_link = wait.until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/main/div/div[4]/section/div[1]/div/div[3]/div/span[1]/div/span/div/div/div/a[2]'))
    )
    second_link.click()
    print("✅ Second element clicked.")

    time.sleep(10)  # Give time for action to complete (e.g., download or page transition)

except Exception as e:
    print("❌ Error during clicking sequence:", e)

finally:
    driver.quit()
