from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import shutil
import os

download_dir = os.path.join(os.getcwd(), "Downloads")

options = Options()
#options.add_argument('--headless')
options.add_argument("--disable-popup-blocking")
options.add_argument("--start-maximized")
options.add_argument('--window-size=1920,1080')
options.add_argument(f'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')

prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)

driver.get("https://pdfcoffee.com/qdownload/np0017962014-pt-unlocked-pdf-free.html")
time.sleep(5)


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

def prepare_and_wait_for_downloads(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        for f in os.listdir(path):
            file_path = os.path.join(path, f)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"⚠️ Could not delete {file_path}: {e}")

    print("🧹 Folder cleaned. Waiting for new download...")

    seconds = 0
    while True:
        files = os.listdir(path)
        if files and not any(fname.endswith(".tmp") for fname in files):
            print("✅ Download completed!")
            break

        time.sleep(1)
        seconds += 1
        if seconds > 120:
            print("⚠️ Timeout waiting for download.")
            break

prepare_and_wait_for_downloads(download_dir)

