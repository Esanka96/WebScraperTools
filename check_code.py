from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()

# Enable performance logging (for capturing network logs)
caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}

# Pass the capabilities to ChromeOptions
chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})


# Initialize the WebDriver with options and service
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the desired URL
driver.get('https://www.futuribles.com/en/')

# Retrieve the performance logs
logs = driver.get_log('performance')

# Process the logs to extract response headers
for log in logs:
    try:
        log_json = json.loads(log["message"])["message"]
        if "Network.responseReceived" in log_json["method"]:
            response = log_json["params"]["response"]
            headers = response.get("headers", {})

            # Print key-value pairs of response headers
            for key, value in headers.items():
                print(f"{key}: {value}")
    except Exception as e:
        pass

# Close the browser
driver.quit()